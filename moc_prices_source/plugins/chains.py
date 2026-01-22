from ..namespaces import AutoNamespace
from ..evm import EVM, get_multicall_addr_env, get_node_rpc_uri_env

chain = AutoNamespace()

chain.rsk_mainnet.env.multicall_addr.name = 'MULTICALL_ADDR'
chain.rsk_mainnet.env.multicall_addr.default = 'rootstock'
chain.rsk_mainnet.env.node_rpc_uri.name = 'NODE_RPC_URI'
chain.rsk_mainnet.env.node_rpc_uri.default = 'rootstock'

chain.rsk_testnet.env.multicall_addr.name = 'MULTICALL_ADDR_TESTNET'
chain.rsk_testnet.env.multicall_addr.default = 'rootstock_testnet'
chain.rsk_testnet.env.node_rpc_uri.name = 'NODE_RPC_URI_TESTNET'
chain.rsk_testnet.env.node_rpc_uri.default = 'rootstock_testnet'

for obj in chain:

    obj.multicall_addr = get_multicall_addr_env(
        env_name = obj.env.multicall_addr.name,
        default_addr = obj.env.multicall_addr.default)

    obj.node_rpc_uri = get_node_rpc_uri_env(
        env_name = obj.env.node_rpc_uri.name,
        default_uri = obj.env.node_rpc_uri.default)

    obj.evm = EVM(obj.node_rpc_uri, multicall_addr=obj.multicall_addr)

chain.freeze()
