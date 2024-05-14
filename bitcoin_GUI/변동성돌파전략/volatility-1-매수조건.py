import pyupbit
import time

def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker)
    volatility = (df.iloc[-2, 1] - df.iloc[-2, 2]) * k
    target = df.iloc[-1, 0] + volatility
    return target

def buy_crypto_currency(ticker, price):
    krw = upbit.get_balance("KRW")
    unit = (krw*0.7) / price
    upbit.buy_market_order(ticker, unit)




with open("upbit.txt") as f:
    lines = f.readlines()
    access = lines[0].strip()
    secret = lines[1].strip()
    upbit = pyupbit.Upbit(access, secret)


target = get_target_price("KRW-BTC", 0.5)

hold_flag = False # 매수 상태를 나타내는 flag

while True:
    price = pyupbit.get_current_price("KRW-BTC")
    if target <= price and hold_flag == False:
        print("매수!")
        hold_flag = True

    print("현재가: ", price)
    time.sleep(1)