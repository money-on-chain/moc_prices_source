import unittest
from io import StringIO
from unittest.mock import patch

from moc_prices_source.my_envs import Envs, TypeBase, URL


class URLTests(unittest.TestCase):

    def test_url_is_a_validated_string_and_type_base(self):
        value = URL('https://example.com:8443/path?query=value')

        self.assertIsInstance(value, str)
        self.assertIsInstance(value, TypeBase)
        self.assertEqual(
            str(value),
            'https://example.com:8443/path?query=value',
        )

    def test_url_rejects_missing_scheme_host_and_invalid_port(self):
        invalid_urls = (
            'example.com/path',
            'https:///path',
            'https://example.com:not-a-port',
            'https://example.com:70000',
            'https://example.com/a path',
            'http://user:secret@%zz:8080',
            'http://user:secret@☃.example.com:8080',
            'ftp://proxy.example.com:21',
            'file://proxy.example.com/path',
            'socks5://proxy.example.com:1080',
        )

        for value in invalid_urls:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    URL(value)

    def test_url_allows_empty_and_whitespace_only_values(self):
        for value in ('', '   '):
            with self.subTest(value=value):
                url = URL(value)

                self.assertEqual(str(url), '')
                self.assertEqual(url.masked, '')
                self.assertFalse(url)

    def test_masked_url_hides_credentials_path_and_query(self):
        value = URL(
            'http://user:secret@proxy.example.com:8080/private?token=x'
        )

        self.assertEqual(
            value.masked,
            'http://***:***@proxy.example.com:8080',
        )


class EnvsURLTests(unittest.TestCase):

    def test_url_default_is_intentionally_not_cast(self):
        default = 'http://proxy.example.com:8080'
        envs = Envs(load_envfile_on_first_get=False)

        with patch.dict('os.environ', {}, clear=True):
            value = envs('TEST_PROXY', default, envs.types.url)

        self.assertIs(type(value), str)
        self.assertEqual(value, default)

    def test_environment_url_equal_to_default_is_cast_and_masked(self):
        proxy_url = (
            'http://user:secret@proxy.example.com:8080/private?token=x'
        )
        default = URL(proxy_url)
        envs = Envs(load_envfile_on_first_get=False)

        with patch.dict('os.environ', {'TEST_PROXY': proxy_url}, clear=True):
            value = envs('TEST_PROXY', default, envs.types.url)

        rendered = str(envs)

        self.assertIsInstance(value, URL)
        self.assertNotIn('user', rendered)
        self.assertNotIn('secret', rendered)
        self.assertNotIn('/private', rendered)
        self.assertNotIn('token=x', rendered)
        self.assertIn('http://***:***@proxy.example.com:8080', rendered)

    def test_empty_url_environment_value_means_disabled(self):
        envs = Envs(load_envfile_on_first_get=False)

        with patch.dict('os.environ', {'TEST_PROXY': ''}):
            value = envs('TEST_PROXY', None, envs.types.url)

        self.assertIsInstance(value, URL)
        self.assertEqual(str(value), '')
        self.assertFalse(value)

    def test_url_keeps_runtime_value_and_uses_masked_display(self):
        proxy_url = 'http://user:secret@proxy.example.com:8080/private?token=x'
        envs = Envs(load_envfile_on_first_get=False)

        with patch.dict('os.environ', {'TEST_PROXY': proxy_url}):
            value = envs('TEST_PROXY', None, envs.types.url)

        rendered = str(envs)

        self.assertIsInstance(value, URL)
        self.assertEqual(str(value), proxy_url)
        self.assertNotIn('user', rendered)
        self.assertNotIn('secret', rendered)
        self.assertNotIn('/private', rendered)
        self.assertNotIn('token=x', rendered)
        self.assertIn('http://***:***@proxy.example.com:8080', rendered)

    def test_repeated_url_lookup_preserves_cast_and_masking(self):
        proxy_url = 'http://user:secret@proxy.example.com:8080/private?token=x'
        envs = Envs(load_envfile_on_first_get=False)

        with patch.dict('os.environ', {'TEST_PROXY': proxy_url}):
            first = envs('TEST_PROXY', None, envs.types.url)
            second = envs('TEST_PROXY')

        rendered = str(envs)

        self.assertIsInstance(first, URL)
        self.assertIsInstance(second, URL)
        self.assertIs(envs.cast_of('TEST_PROXY'), URL)
        self.assertEqual(envs.value_of('TEST_PROXY'), first)
        self.assertNotIn('user', rendered)
        self.assertNotIn('secret', rendered)
        self.assertNotIn('/private', rendered)
        self.assertNotIn('token=x', rendered)
        self.assertIn('http://***:***@proxy.example.com:8080', rendered)

    def test_invalid_url_error_does_not_expose_credentials(self):
        proxy_url = 'http://user:secret@proxy.example.com:not-a-port'
        envs = Envs(load_envfile_on_first_get=False)
        stderr = StringIO()

        with patch.dict('os.environ', {'TEST_PROXY': proxy_url}):
            with patch('moc_prices_source.my_envs.stderr', stderr):
                with self.assertRaises(SystemExit):
                    envs('TEST_PROXY', None, envs.types.url)

        error = stderr.getvalue()
        self.assertNotIn('user', error)
        self.assertNotIn('secret', error)
        self.assertIn("TEST_PROXY: '***'", error)


if __name__ == '__main__':
    unittest.main()
