import unittest

from bs4 import BeautifulSoup

from moc_prices_source.engines import get_prices
from moc_prices_source.plugins.engines.press.infodolar import (
    usd_ars_ccl_infodolar,
    usd_ars_infodolar,
)


class FakeEngine:
    def __init__(self, name, results):
        self.name = name
        self.results = iter(results)
        self.calls = 0
        self._clean_output_values()

    def _clean_output_values(self):
        self._price = None
        self._error = None

    def __call__(self):
        self.calls += 1
        result = next(self.results)
        if isinstance(result, Exception):
            raise result
        self._price = result
        self._error = None

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'price': self._price,
            'error': self._error,
            'ok': not bool(self._error),
        }


class GetPricesTests(unittest.TestCase):
    def test_exception_fails_only_its_engine_without_exposing_details(self):
        broken = FakeEngine('broken', [ValueError('secret query token')])
        healthy = FakeEngine('healthy', [42])

        prices = get_prices(engines_list=[broken, healthy])

        self.assertEqual(broken.calls, 1)
        self.assertEqual(prices[0]['price'], None)
        self.assertFalse(prices[0]['ok'])
        self.assertEqual(prices[0]['error'], 'Engine error (ValueError)')
        self.assertEqual(prices[1]['price'], 42)
        self.assertTrue(prices[1]['ok'])

    def test_empty_price_recovers_on_one_retry(self):
        engine = FakeEngine('recovering', [None, 42])

        prices = get_prices(engines_list=[engine])

        self.assertEqual(engine.calls, 2)
        self.assertEqual(prices[0]['price'], 42)
        self.assertTrue(prices[0]['ok'])

    def test_persistent_empty_price_stops_after_one_retry(self):
        engine = FakeEngine('empty', [None, None])

        prices = get_prices(engines_list=[engine])

        self.assertEqual(engine.calls, 2)
        self.assertFalse(prices[0]['ok'])
        self.assertEqual(prices[0]['error'], 'No price after retry')


class InfodolarTests(unittest.TestCase):
    def test_invalid_price_is_reported_as_format_error(self):
        html = BeautifulSoup(
            '<table id="CompraVenta">'
            '<td class="colCompraVenta">N/A</td>'
            '<td class="colCompraVenta">$1.234,56</td>'
            '</table>',
            'lxml',
        )

        for module in (usd_ars_infodolar, usd_ars_ccl_infodolar):
            with self.subTest(engine=module.__name__):
                engine = module.Engine()
                self.assertIsNone(engine._scraping(html))
                self.assertEqual(engine.error, 'Response format error')


if __name__ == '__main__':
    unittest.main()
