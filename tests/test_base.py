import unittest
from unittest.mock import Mock, patch

from requests import Response

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


if __name__ == '__main__':
    unittest.main()
