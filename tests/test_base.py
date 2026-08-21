import unittest
from unittest.mock import Mock, patch

from requests import Response, exceptions

from moc_prices_source.plugins.base import Base


class BaseRequestTests(unittest.TestCase):

    @staticmethod
    def _response():
        response = Response()
        response.status_code = 200
        response._content = b'{"price": 1}'
        response.url = 'https://example.com/prices'
        return response

    def test_request_uses_url_proxy_for_http_and_https(self):
        proxy_url = 'http://proxy.example.com:8080'

        for method in ('get', 'post'):
            with self.subTest(method=method):
                engine = Base()
                engine._redis = None
                engine._method = method
                engine._uri = 'https://example.com/prices'
                engine._url_proxy = proxy_url

                rq = Mock()
                getattr(rq, method).return_value = self._response()

                result = engine._request(rq)

                self.assertEqual(result, {'price': 1})
                getattr(rq, method).assert_called_once_with(
                    url='https://example.com/prices',
                    timeout=engine.timeout,
                    verify=engine._ssl_verify,
                    proxies={
                        'http': proxy_url,
                        'https': proxy_url,
                    },
                )

    def test_empty_url_proxy_does_not_fall_back_to_default_proxy(self):
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = ''

        rq = Mock()
        rq.get.return_value = self._response()

        with patch(
            'moc_prices_source.plugins.base.default_proxy',
            'http://default-proxy.example.com:8080',
        ):
            result = engine._request(rq)

        self.assertEqual(result, {'price': 1})
        rq.get.assert_called_once_with(
            url='https://example.com/prices',
            timeout=engine.timeout,
            verify=engine._ssl_verify,
            proxies={
                'http': None,
                'https': None,
                'all': None,
            },
        )

    def test_unconfigured_proxy_disables_environment_proxies(self):
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = None

        rq = Mock()
        rq.get.return_value = self._response()

        environment = {
            'HTTP_PROXY': 'http://ambient-proxy.example.com:8080',
            'HTTPS_PROXY': 'http://ambient-proxy.example.com:8080',
            'ALL_PROXY': 'http://ambient-proxy.example.com:8080',
        }
        with patch.dict('os.environ', environment, clear=True):
            with patch('moc_prices_source.plugins.base.default_proxy', None):
                result = engine._request(rq)

        self.assertEqual(result, {'price': 1})
        rq.get.assert_called_once_with(
            url='https://example.com/prices',
            timeout=engine.timeout,
            verify=engine._ssl_verify,
            proxies={
                'http': None,
                'https': None,
                'all': None,
            },
        )

    def test_unset_url_proxy_uses_default_proxy(self):
        proxy_url = 'http://default-proxy.example.com:8080'
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = None

        rq = Mock()
        rq.get.return_value = self._response()

        with patch('moc_prices_source.plugins.base.default_proxy', proxy_url):
            result = engine._request(rq)

        self.assertEqual(result, {'price': 1})
        rq.get.assert_called_once_with(
            url='https://example.com/prices',
            timeout=engine.timeout,
            verify=engine._ssl_verify,
            proxies={
                'http': proxy_url,
                'https': proxy_url,
            },
        )

    def test_proxy_request_error_does_not_expose_credentials(self):
        proxy_url = (
            'http://user:supersecret@proxy.example.com:8080/'
            'private?token=x'
        )
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = proxy_url

        rq = Mock()
        rq.get.side_effect = exceptions.InvalidURL(
            f'Failed to parse: {proxy_url}'
        )

        result = engine._request(rq)
        serialized = engine.as_json

        self.assertIsNone(result)
        self.assertIn(
            'http://***:***@proxy.example.com:8080',
            str(engine.error),
        )
        for secret in ('user', 'supersecret', '/private', 'token=x'):
            with self.subTest(secret=secret):
                self.assertNotIn(secret, str(engine.error))
                self.assertNotIn(secret, serialized)

    def test_proxy_http_error_preserves_upstream_status(self):
        proxy_url = (
            'http://user:supersecret@proxy.example.com:8080/'
            'private?token=x'
        )
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = proxy_url

        response = self._response()
        response.status_code = 429
        response.reason = 'Too Many Requests'
        rq = Mock()
        rq.get.return_value = response

        result = engine._request(rq)
        error = str(engine.error)

        self.assertIsNone(result)
        self.assertIn('upstream returned HTTP 429', error)
        self.assertIn('http://***:***@proxy.example.com:8080', error)
        for secret in ('user', 'supersecret', '/private', 'token=x'):
            with self.subTest(secret=secret):
                self.assertNotIn(secret, error)

    def test_proxy_transport_error_does_not_expose_credentials(self):
        proxy_url = (
            'http://user:supersecret@proxy.example.com:8080/'
            'private?token=x'
        )
        engine = Base()
        engine._redis = None
        engine._uri = 'https://example.com/prices'
        engine._url_proxy = proxy_url

        rq = Mock()
        rq.get.side_effect = exceptions.ProxyError(
            f'Cannot connect to proxy {proxy_url}'
        )

        result = engine._request(rq)
        error = str(engine.error)

        self.assertIsNone(result)
        self.assertIn('ProxyError: request through proxy', error)
        self.assertIn('http://***:***@proxy.example.com:8080', error)
        for secret in ('user', 'supersecret', '/private', 'token=x'):
            with self.subTest(secret=secret):
                self.assertNotIn(secret, error)


if __name__ == '__main__':
    unittest.main()
