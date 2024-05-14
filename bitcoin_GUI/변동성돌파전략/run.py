from volatility import *


target = get_target_price("KRW-BTC", 0.5)

hold_flag = False # 매수 상태를 나타내는 flag

while True:
    price = pyupbit.get_current_price("KRW-BTC")
    if target <= price and hold_flag == False:
        ret = buy_crypto_currency("KRW-BTC", price)
        print("매수!", ret)
        hold_flag = True

    now = datetime.datetime.now()
    morning = datetime.datetime(now.year, now.month, now.day, 8, 59, 50) # 아침 9시
    if morning <= now <= morning + datetime.timedelta(seconds=10):
        if hold_flag == True:
            ret = sell_crypto_currency("KRW-BTC", price)
            print("매도!", ret)
        target = get_target_price("KRW-BTC", 0.5)
        hold_flag = False


    print("현재가: ", price)
    time.sleep(1)