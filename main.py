from binance.client import Client


class BinanceConnection:
    def __init__(self, file):
        self.connect(file)

    """ Creates Binance client """

    def connect(self, file):
        lines = [line.rstrip('\n') for line in open(file)]
        key = lines[0]
        secret = lines[1]
        self.client = Client(key, secret)


if __name__ == '__main__':
    filename = 'C:\\Users\\Public\\Projects\\my-bot\\credentials.txt'
    connection = BinanceConnection(filename)

    symbol = 'BTCUSDT'
    interval = '5m'
    limit = 500

    try:
        klines = connection.client.get_klines(symbol=symbol, interval=interval, limit=limit)
    except Exception as exp:
        print(exp.status_code, flush=True)
        print(exp.message, flush=True)

    open = [float(entry[1]) for entry in klines]
    high = [float(entry[2]) for entry in klines]
    low = [float(entry[3]) for entry in klines]
    close = [float(entry[4]) for entry in klines]

    last_closing_price = close[-1]

    previous_closing_price = close[-2]

    print(symbol, 'anlık kapanış fiyatı', last_closing_price, ', bir önceki kapanış fiyatı', previous_closing_price)
