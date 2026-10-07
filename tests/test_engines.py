import unittest
from decimal import Decimal

from bs4 import BeautifulSoup

from moc_prices_source.engines import get_prices
from moc_prices_source.plugins.engines.press.dolarhoy._parse import ars_price
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
        for module, label in ((usd_ars_infodolar, 'Dólar Blue'),
                              (usd_ars_ccl_infodolar, 'Dólar CCL')):
            for price in ('N/A', 'NaN', 'Infinity', '0', '-1'):
                with self.subTest(engine=module.__name__, price=price):
                    html = BeautifulSoup(
                        f'<table id="CompraVenta"><tr>'
                        f'<td class="colNombre">{label}</td>'
                        f'<td class="colCompraVenta">{price}</td>'
                        '<td class="colCompraVenta">$1.234,56</td>'
                        '</tr></table>',
                        'lxml',
                    )
                    engine = module.Engine()
                    self.assertIsNone(engine._scraping(html))
                    self.assertEqual(engine.error, 'Response format error')

    def test_valid_price_in_matching_row(self):
        for module, label in ((usd_ars_infodolar, 'Dólar Blue'),
                              (usd_ars_ccl_infodolar, 'Dólar CCL')):
            with self.subTest(engine=module.__name__):
                html = BeautifulSoup(
                    f'<table id="CompraVenta"><tr>'
                    f'<td class="colNombre">{label}</td>'
                    '<td class="colCompraVenta">$1.200,00</td>'
                    '<td class="colCompraVenta">$1.400,00</td>'
                    '</tr></table>',
                    'lxml',
                )
                self.assertEqual(module.Engine()._scraping(html),
                                 {'price': Decimal('1300.00')})


class DolarHoyTests(unittest.TestCase):
    def test_non_finite_price_is_rejected(self):
        for price in ('NaN', 'Infinity', '-Infinity'):
            with self.subTest(price=price):
                self.assertIsNone(ars_price(price))

    def test_valid_price_is_parsed(self):
        self.assertEqual(ars_price('$1.234,56'), Decimal('1234.56'))


if __name__ == '__main__':
    unittest.main()
