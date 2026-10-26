import unittest
from unittest.mock import patch

from moc_prices_source import server


class CoinPairValueTests(unittest.TestCase):

    def setUp(self):
        self.client = server.app.test_client()
        with server.app.app_context():
            server.cache.clear()

    def test_failed_only_sub_coinpair_reports_zero_sources_without_500(self):
        def get_price_with_failed_source(*args, detail, **kwargs):
            detail['prices'] = [{
                'coinpair': 'RIF/USDT(MA)',
                'ok': False,
                'description': 'test source',
                'error': 'unavailable',
            }]
            return 1

        with patch.object(server, 'get_price', get_price_with_failed_source):
            response = self.client.get(
                '/api/coinpairs/get_value_simple?coinpair=ISLIQ_ROC')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 1)

    def test_cached_value_is_not_shared_between_coinpairs(self):
        prices = {'BTC/USD': 100, 'RIF/USD': 2}

        def get_price_by_coinpair(coinpairs, detail, **kwargs):
            return prices[coinpairs]

        with patch.object(server, 'get_price', get_price_by_coinpair):
            for coinpair, price in prices.items():
                response = self.client.get(
                    '/api/coinpairs/get_value_simple',
                    query_string={'coinpair': coinpair})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), price)


class HashMethodTests(unittest.TestCase):

    @staticmethod
    def _args(coinpair):
        return str((('coinpair', coinpair),)).encode()

    def test_interleaved_calls_keep_their_own_key(self):
        hash_method = server.HashMethod('coinpair', pre='test')

        # flask-caching calls hash_method(x) and then .hexdigest(); another
        # request may hash in between on the same shared instance.
        btc = hash_method(self._args('BTC/USD'))
        rif = hash_method(self._args('RIF/USD'))

        self.assertIn('btc/usd', btc.hexdigest())
        self.assertIn('rif/usd', rif.hexdigest())
        self.assertNotEqual(btc.hexdigest(), rif.hexdigest())


class MainTests(unittest.TestCase):

    def test_debug_refuses_non_loopback_host(self):
        with patch.object(server.app, 'run') as app_run:
            with self.assertRaises(SystemExit):
                server.main(host='0.0.0.0', debug=True)
        app_run.assert_not_called()

    def test_debug_allows_loopback_host(self):
        with patch.object(server.app, 'run') as app_run:
            server.main(host='127.0.0.1', port=7989, debug=True)
        app_run.assert_called_once_with(
            debug=True, host='127.0.0.1', port=7989)

    def test_production_uses_gunicorn(self):
        with patch.object(server, 'run_gunicorn') as run_gunicorn, \
             patch.object(server.app, 'run') as app_run:
            server.main(host='0.0.0.0', port=7989, debug=False)
        run_gunicorn.assert_called_once_with('0.0.0.0', 7989)
        app_run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
