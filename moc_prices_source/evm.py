from __future__ import annotations
import requests, json
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple
from eth_utils import keccak, to_checksum_address
from web3 import Web3 as Web3base
from web3 import HTTPProvider
try:
    from eth_abi import decode as abi_decode
except ImportError:
    from eth_abi.abi import decode_abi as abi_decode
try:
    from eth_abi import encode as abi_encode
except ImportError:
    from eth_abi.abi import encode_abi as abi_encode
from urllib.parse import urlparse
from .cli import get_env



class Web3(Web3base):
    """ Override Original Web3 """

    def is_connected(self) -> bool:
        try:
            return super().is_connected()
        except AttributeError:
            return super().isConnected()

    @staticmethod
    def to_checksum_address(value):
        try:
            return Web3base.to_checksum_address(value)
        except:
            return Web3base.toChecksumAddress(value)


class OneShotHTTPProvider(HTTPProvider):
    def make_request(self, method, params):
        payload = {"jsonrpc": "2.0",
                   "method": method,
                   "params": params,
                   "id": 1}
        headers = {"Content-Type": "application/json",
                   "Connection": "close"}
        with requests.Session() as s:
            resp = s.post(self.endpoint_uri,
                          headers=headers,
                          data=json.dumps(payload))
            resp.raise_for_status()
            return resp.json()


@dataclass(frozen=True)
class FunctionSpecData:
    name: str
    inputs: Tuple[str, ...]
    outputs: Tuple[str, ...]

    @property
    def canonical_sig(self) -> str:
        return f"{self.name}({','.join(self.inputs)})"
    
    @property
    def selector(self) -> bytes:
        return keccak(text=self.canonical_sig)[:4]

    @staticmethod
    def _normalize_arg(abi_type: str, value: Any) -> Any:
        t = abi_type.strip()

        if t.endswith("]"):
            if not isinstance(value, (list, tuple)):
                raise TypeError(f"ABI type {t} expects list/tuple")
            base = t[: t.rfind("[")]
            return [_normalize_arg(base, v) for v in value]

        if t == "address":
            if not isinstance(value, str):
                raise TypeError("address must be hex string")
            return to_checksum_address(value)

        if t == "bool":
            if isinstance(value, bool):
                return value
            if isinstance(value, int):
                return bool(value)
            if isinstance(value, str):
                return value.lower() in {"true", "1", "yes", "y"}
            raise TypeError(f"Cannot coerce {value!r} to bool")

        if t.startswith("uint") or t.startswith("int"):
            if isinstance(value, int):
                return value
            if isinstance(value, str):
                return int(value, 16) if value.startswith("0x") else int(value)
            raise TypeError(f"Cannot coerce {value!r} to int")

        if t == "bytes":
            if isinstance(value, (bytes, bytearray)):
                return bytes(value)
            if isinstance(value, str) and value.startswith("0x"):
                return bytes.fromhex(value[2:])
            raise TypeError(f"Cannot coerce {value!r} to bytes")

        if t.startswith("bytes"):
            if isinstance(value, (bytes, bytearray)):
                return bytes(value)
            if isinstance(value, str) and value.startswith("0x"):
                return bytes.fromhex(value[2:])
            raise TypeError(f"Cannot coerce {value!r} to {t}")

        if t == "string":
            return str(value)

        return value

    def normalize_args(self, *args) -> List[Any]:
        if len(args) != len(self.inputs):
            raise ValueError(
                "Argument count mismatch: "
                f"expected {len(self.inputs)}, got {len(args)}"
            )
        return [self._normalize_arg(t, v) for t, v in zip(self.inputs, args)]

    def encode_args(self, *args) -> bytes:
        norm_args = self.normalize_args(*args)
        return abi_encode(list(self.inputs), norm_args) if self.inputs else b""

    def make_calldata(self, *args) -> bytes:
        return self.selector + self.encode_args(*args)
    
    def __str__(self):
        return f"{self.canonical_sig}({','.join(self.outputs)})"

    def decode_outputs(self, result: bytes) -> Any:
        if not self.outputs:
            return None
        decoded = abi_decode(list(self.outputs), result)
        if len(decoded) == 1:
            return decoded[0]
        return decoded


class FunctionSpec(FunctionSpecData):

    @staticmethod
    def _split_types(type_list: str) -> Tuple[str, ...]:
        s = type_list.strip()
        if not s:
            return ()

        out: List[str] = []
        buf: List[str] = []
        depth = 0
        for ch in s:
            if ch == "," and depth == 0:
                t = "".join(buf).strip()
                if t:
                    out.append(t)
                buf = []
                continue
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            buf.append(ch)

        tail = "".join(buf).strip()
        if tail:
            out.append(tail)
        return tuple(out)

    def __init__(self, fn_spec: str):        
        s = fn_spec.strip()

        i1 = s.find("(")
        if i1 <= 0:
            raise ValueError(f"Invalid fn_spec (missing inputs): {fn_spec!r}")

        name = s[:i1].strip()
        if not name:
            raise ValueError(f"Invalid fn_spec (empty name): {fn_spec!r}")

        depth = 0
        end_inputs = None
        for idx in range(i1, len(s)):
            if s[idx] == "(":
                depth += 1
            elif s[idx] == ")":
                depth -= 1
                if depth == 0:
                    end_inputs = idx
                    break
        if end_inputs is None:
            raise ValueError(f"Invalid fn_spec (unclosed inputs): {fn_spec!r}")

        inputs_str = s[i1 + 1 : end_inputs]
        rest = s[end_inputs + 1 :].strip()

        if not rest.startswith("("):
            raise ValueError(f"Invalid fn_spec (missing outputs): {fn_spec!r}")

        depth = 0
        end_outputs = None
        for idx in range(len(rest)):
            if rest[idx] == "(":
                depth += 1
            elif rest[idx] == ")":
                depth -= 1
                if depth == 0:
                    end_outputs = idx
                    break
        if end_outputs is None:
            raise ValueError(f"Invalid fn_spec (unclosed outputs): {fn_spec!r}")

        outputs_str = rest[1:end_outputs]
        trailing = rest[end_outputs + 1 :].strip()
        if trailing:
            raise ValueError(f"Invalid fn_spec (extra trailing text): {fn_spec!r}")

        super().__init__(
            name=name,
            inputs=self._split_types(inputs_str),
            outputs=self._split_types(outputs_str),
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(str(self))})"


class EVMConnectionError(RuntimeError):
    pass


class EVMCallError(RuntimeError):
    pass


addr_zero = '0x0000000000000000000000000000000000000000'


class Address(str):

    def __new__(cls, addr: str | int):

        if addr is None:
            raise ValueError('addr is None')
        
        if hasattr(addr, 'address'):
            addr = addr.address

        if isinstance(addr, int):

            addr = hex(addr)[2:]
            addr = addr[-40:]
            addr = "0" * (40-len(addr)) + addr

        else:

            addr = str(addr).strip()

            if addr.startswith('0x'):
                addr = addr[2:]

            try:
                int(addr, 16)
            except:
                raise ValueError('addr is not hexa')

            if len(addr) != 40:
                raise ValueError('addr has less o more than 40 digits')

        addr = '0x' + addr.lower()

        return super().__new__(cls, addr)


class URI(str):

    def __new__(cls, uri: str):

        if uri is None:
            raise ValueError('uri is None')
        
        ok = False
        try:
            data = urlparse(uri)
            ok = all([
                data.scheme,
                data.netloc
            ])
        except Exception:
            pass
        
        if ok:
            return super().__new__(cls, uri)
        else:
            raise ValueError(f"{repr(uri)} is not a valid URI")


class EVM():

    def __init__(self,
                 rpc_uri_or_web3_obj: str | Web3,
                 block_identifier: str | int = 'latest'):
        if isinstance(rpc_uri_or_web3_obj, str):
            self.web3 = Web3(OneShotHTTPProvider(rpc_uri_or_web3_obj))
        elif isinstance(rpc_uri_or_web3_obj, Web3):
            self.web3 = rpc_uri_or_web3_obj
        else:
            raise ValueError('Invalid RPC URI or Web3 object')
        self.block_identifier = block_identifier
    
    def is_connected(self) -> bool:
        return self.web3.is_connected()
    
    @property
    def block_identifier(self) -> str | int:
        return self._block_identifier

    @block_identifier.setter
    def block_identifier(self, value: str | int ):

        if isinstance(value, str):
            if value.strip().lower() in ['latest', 'last', 'now']:
                self._block_identifier = 'latest'
                return            
            else:
                value = int(value)

        if isinstance(value, int) and value>1:
            self._block_identifier = value
            return
        
        raise ValueError("is not 'latest' or integer > 0")

    @property
    def latest(self) -> bool:
        return self._block_identifier=='latest'

    def connection_check(self):
        if not self.web3.is_connected():
            raise EVMConnectionError(f"Cannot connect to {self.web3.provider}")        

    def call(self,
        contract_address: str,
        fn_spec: str | FunctionSpec,
        *args: Any,
        block_identifier: Optional[str | int] = None,
        from_address: Optional[str] = None,
        gas: Optional[int] = None) -> Any:
        """Perform an eth_call"""

        self.connection_check()

        if block_identifier is None:
            block_identifier = self.block_identifier  

        if isinstance(fn_spec, str):
            fn_spec = FunctionSpec(fn_spec)
        
        if not isinstance(fn_spec, FunctionSpec):
            raise ValueError("'fn_spec' is not str or FunctionSpec")
        
        tx = {
            "to": to_checksum_address(Address(contract_address)),
            "data": fn_spec.make_calldata(*args),
        }

        if from_address:
            tx["from"] = to_checksum_address(Address(from_address))
        
        if gas:
            tx["gas"] = gas

        try:
            result = self.web3.eth.call(tx, block_identifier=block_identifier)
        except Exception as e:
            raise EVMCallError(f"eth_call failed: {e}") from e

        return fn_spec.decode_outputs(result)


def get_addr_env(env_name: str, default_addr:str) -> str:
    return get_env(env_name, Address(default_addr), cast=Address)


def get_uri_env(env_name: str, default_addr: Optional[str] = '') -> str:
    return get_env(env_name, default_addr, cast=URI)


def get_node_rpc_uri_env(env_name: str = 'NODE_RPC_URI',
                         default_addr: str = 'rootstock') -> str:
    return get_env(env_name, default_addr,
        cast=URI,
        alias={
            'rootstock': 'https://public-node.rsk.co',
            'rsk': 'rootstock',
            'rsk_mainnet': 'rootstock'
            })
