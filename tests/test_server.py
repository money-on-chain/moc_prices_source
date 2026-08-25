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


if __name__ == '__main__':
    unittest.main()
