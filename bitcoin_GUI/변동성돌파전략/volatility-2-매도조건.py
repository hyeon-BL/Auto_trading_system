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


target = get_target_price("KRW-BTC", 0.5)

hold_flag = False # 매수 상태를 나타내는 flag

while True:
    price = pyupbit.get_current_price("KRW-BTC")
    if target <= price and hold_flag == False:
        print("매수!")
        hold_flag = True

    now = datetime.datetime.now()
    morning = datetime.datetime(now.year, now.month, now.day, 8, 59, 50) # 아침 9시
    if morning <= now <= morning + datetime.timedelta(seconds=10) and hold_flag == True:
        sell_crypto_currency("KRW-BTC", price)
        target = get_target_price("KRW-BTC", 0.5)
        hold_flag = False
        if hold_flag == True:
            print("매도!")
            hold_flag = False
    print("현재가: ", price)
    time.sleep(1)