from decimal import Decimal, InvalidOperation


def ars_price(text):
    value = text.strip().replace('$', '').replace(' ', '').replace('.', '').replace(',', '.')
    try:
        price = Decimal(value)
    except InvalidOperation:
        return None
    return price if price.is_finite() and price > 0 else None


def ars_quote(html, label):
    for tile in html.find_all('div', class_='tile cotizacion_value'):
        fields = [s.strip().lower() for s in tile.parent.strings if s.strip()]
        if len(fields) >= 5 and fields[0] == label and fields[1] == 'compra' and fields[3] == 'venta':
            buy, sell = ars_price(fields[2]), ars_price(fields[4])
            if buy is not None and sell is not None:
                return (buy + sell) / 2
    return None
