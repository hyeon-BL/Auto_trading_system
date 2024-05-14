import pyupbit
import time
import datetime

def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker)
    volatility = (df.iloc[-2, 1] - df.iloc[-2, 2]) * k
    target = df.iloc[-1, 0] + volatility
    return target

def buy_crypto_currency(ticker, price):
    krw = upbit.get_balance("KRW")
    unit = (krw*0.7) / price # 70% 매수
    return upbit.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker, price):
    unit = upbit.get_balance(ticker)
    return upbit.sell_market_order(ticker, unit) # 시장가 매도

with open("upbit.txt") as f:
    lines = f.readlines()
    access = lines[0].strip()
    secret = lines[1].strip()
    upbit = pyupbit.Upbit(access, secret)