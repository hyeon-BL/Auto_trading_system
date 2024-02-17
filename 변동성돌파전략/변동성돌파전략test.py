import pyupbit
import numpy as np
import datetime
import cufflinks as cf
import pandas as pd

# OHLCV(open, high, low, close, volume) 당일 시가, 고가, 저가, 종가, 거래량 데이터
ddf = pyupbit.get_ohlcv("KRW-BTC", count=200)
price = {'Buy':[], 'Sell':[]}
seed = 100000
num = 0


# 매수일
def buy(today, yesterday):
    global buy_price, price, seed, bday, num
    rise1 = (yesterday.iloc[0]['close'] - yesterday.iloc[0]['open'])/yesterday.iloc[0]['open']
    rise2 = (today.iloc[0]['close'] - today.iloc[0]['open'])/today.iloc[0]['open']
    if rise1 > 0 and rise2 >= rise1 * 0.5 and seed >= 50000:
        bday = today
        print('''
    {}일 {}에 50000원 매수
              '''.format(list(today.index)[0], list(today['close'])[0]))
        buy_price = 50000
        price['Buy'].append(buy_price)
        seed -= 50000
        num += 1


# 매도일
def sell(today, yesterday):
    global sell_price, price, seed,bday, sday, num, ddf
    fall1 = (yesterday.iloc[0]['close'] - yesterday.iloc[0]['open'])/yesterday.iloc[0]['open']
    fall2 = (today.iloc[0]['close'] - today.iloc[0]['open'])/today.iloc[0]['open']
    if fall1 < 0 and fall2 <= fall1 * 0.5 and num >= 1:
        sday = today
        rate = (sday.iloc[0]['close'] - bday.iloc[0]['close'])/bday.iloc[0]['close']
        sell_price = 50000 *(1+rate)
        print('''
    {}일 {}에 {}원 매도
              '''.format(list(today.index)[0], list(today['close'])[0], sell_price))
        price['Sell'].append(sell_price)
        seed += sell_price
        num -= 1


cf.go_offline(connected=True)
qf=cf.QuantFig(ddf,title='BTC',legend='top',name='Buy')
qf.iplot()




for d in list(ddf.index):
    try :
        buy(ddf.loc[[d]], ddf.loc[[yesterday]])
        sell(ddf.loc[[d]], ddf.loc[[yesterday]])
    except NameError:
        print('시작')
    yesterday = d

print('총 수익: {}'.format(sum(price['Sell'])-sum(price['Buy'])))
print(len(price['Buy']), len(price['Sell']))
print('단순수익률: {} %'.format((ddf.iloc[199,3]-ddf.iloc[0,3])/ddf.iloc[0,3] * 100))