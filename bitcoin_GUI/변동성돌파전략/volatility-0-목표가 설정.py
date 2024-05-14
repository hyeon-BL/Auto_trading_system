import pyupbit

def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker)
    volatility = (df.iloc[-2, 1] - df.iloc[-2, 2]) * k
    target = df.iloc[-1, 0] + volatility
    return target

target = get_target_price("KRW-BTC", 0.5)
print(target)