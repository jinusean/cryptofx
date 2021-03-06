import sys

import requests


def main():
    amount = 1
    default_symbols = ['BTC', 'USD']

    args = sys.argv[1:]

    symbols = []

    for arg in args:
        if arg in ['-h', '--help']:
            return print('cryptofx [amount] [from=btc] [to=usd]')
        try:
            amount = float(arg)
        except:
            symbols.append(arg.upper())

    if len(symbols) == 0:
        symbols = default_symbols
    elif len(symbols) == 1:
        symbols.append(default_symbols[-1])

    fsym = symbols[0]
    tsym = symbols[1]

    url = f'https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsym}'

    res = requests.get(url)
    try:
        if res.status_code == 200:
            result = res.json()
            if 'Response' in result:
                # error has occurred
                return print(result['Message'])

            conversion = result[tsym]
            value = amount * conversion
            value = int(value) if value.is_integer() else f'{value:f}'.rstrip('0')
            print(f'{value} {tsym}')
        else:
            print(res.status_code, res.reason)
    except Exception as e:
        print('Exception occurred', file=sys.stderr)
        print(e, file=sys.stderr)
        print()
        print('Response:')
        print(res.status_code, res.reason)


if __name__ == '__main__':
    main()
