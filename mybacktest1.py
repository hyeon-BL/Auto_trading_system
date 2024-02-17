import pyupbit
import numpy as np
from datetime import datetime
import pandas as pd

# OHLCV(open, high, low, close, volume) 당일 시가, 고가, 저가, 종가, 거래량 데이터
ddf = pyupbit.get_ohlcv("KRW-BTC", count=90)
price = {'Buy':[], 'Sell':[]}
num = 0
seed = 100000
bstep = 1
sstep = 1


# 매수일
def buy(today, yesterday):
    global buy_price, price, seed, bstep, bday, num
    rise1 = (yesterday.iloc[0]['close'] - yesterday.iloc[0]['open'])/yesterday.iloc[0]['open']
    rise2 = (today.iloc[0]['close'] - today.iloc[0]['open'])/today.iloc[0]['open']
    if bstep == 1 and rise1 > 0 and rise2 >= rise1 * 0.5 and seed >= 30000:
        bday = today
        print('''
첫번째 시나리오
    {}일 {}에 30000원 1차 매수
              '''.format(list(today.index)[0], list(today['close'])[0]))
        buy_price = 30000
        price['Buy'].append(buy_price)
        bstep += 1
        seed -= 30000
        num +=1

    elif bstep == 2 and rise1 > 0 and rise2 >= rise1 * 0.5 and seed >= 40000:
        bday = today
        print('''
두번째 시나리오
    {}일 {}에 40000원 2차 매수
            '''.format(list(today.index)[0], list(today['close'])[0]))
        buy_price = 40000
        price['Buy'].append(buy_price)
        bstep += 1
        seed -= 40000
        num += 1

    elif bstep == 3 and rise1 > 0 and rise2 >= rise1 * 0.5 and seed >= 30000:
        bday = today
        print('''
세번째 시나리오
    {}일 {}에 30000원 3차 매수
              '''.format(list(today.index)[0], list(today['close'])[0]))
        buy_price = 30000
        price['Buy'].append(buy_price)
        bstep += 1
        seed -= 30000
        num +=1
    
    elif bstep == 4:
        bstep = 1




# 매도일
def sell(today, yesterday):
    global sell_price, price, seed, sstep, bday, sday, num
    fall1 = (yesterday.iloc[0]['close'] - yesterday.iloc[0]['open'])/yesterday.iloc[0]['open']
    fall2 = (today.iloc[0]['close'] - today.iloc[0]['open'])/today.iloc[0]['open']
    if sstep == 1 and fall1 < 0 and fall2 <= fall1 * 0.5 and num>0:
        sday = today
        rate = (sday.iloc[0]['open']*(1 + fall1*0.5) - bday.iloc[0]['close'])/bday.iloc[0]['close']
        sell_price = 30000 *(1+rate)
        print('''
첫번째 시나리오
    {}일 {}에 {}원 1차 매도
              '''.format(list(today.index)[0], list(today['close'])[0], sell_price))
        price['Sell'].append(sell_price)
        sstep += 1
        seed += sell_price
        num -= 1

    elif sstep == 2 and fall1 < 0 and fall2 <= fall1 * 0.5 and num>0:
        sday = today
        rate = (sday.iloc[0]['open']*(1 + fall1*0.5) - bday.iloc[0]['close'])/bday.iloc[0]['close']
        sell_price = 40000 *(1+rate/100)
        print('''
두번째 시나리오
    {}일 {}에 {}원 2차 매도
            '''.format(list(today.index)[0], list(today['close'])[0], sell_price))
        price['Sell'].append(sell_price)
        sstep += 1
        seed += sell_price
        num -= 1

    elif sstep == 3 and fall1 < 0 and fall2 <= fall1 * 0.5 and num>0:
        sday = today
        rate = (sday.iloc[0]['open']*(1 + fall1*0.5) - bday.iloc[0]['close'])/bday.iloc[0]['close']
        sell_price = 30000 *(1+rate/100)
        print('''
세번째 시나리오
    {}일 {}에 {}원 3차 매도
              '''.format(list(today.index)[0], list(today['close'])[0], sell_price))
        price['Sell'].append(sell_price)
        sstep += 1
        seed += sell_price
        num -=1
    
    elif sstep == 4:
        sstep = 1










for d in list(ddf.index):
    try :
        buy(ddf.loc[[d]], ddf.loc[[yesterday]]) # yesterday 수정해야 함(세번째 매수일 기준 매도 금액이 책정됨)
        sell(ddf.loc[[d]], ddf.loc[[yesterday]])
    except NameError:
        print('시작')
    yesterday = d

print('총 수익: {}'.format(sum(price['Sell'])-sum(price['Buy'])))
print(len(price['Buy']), len(price['Sell']))





# mdf = pyupbit.get_ohlcv("KRW-BTC", count=3, interval='month')
# wdf = pyupbit.get_ohlcv("KRW-BTC", count=4, interval='week')
# target1 = mdf['close'].min()
# target2 = wdf['close'].min()
# print(target1, target2)
# print(mdf)
# print(wdf)

# def demand(date, day): #date : 비교 일수, day : 가장 낮았던 날
#     global buy_price
#     buy_price = {}
#     price = date.iloc[0]['open']
#     when = list(date.index)[0]
#     if when > list(day.index)[0] and price >= day.iloc[0]['close']:
#         print(when, '일자 ', price, '에 매수', sep='')
#         buy_price[when] = price

# for d in list(ddf.index):
#     demand(ddf.loc[[d]], mdf.loc[mdf['close']==target1]) # []를 붙여야 데이터프레임으로 가져올 수 있음!!!
#     if len(buy_price) != 0:
#         break
    
# def supply(df):
    



# # 변동성 돌파 기준 범위 계산, (고가 - 저가) * k값
# df['range'] = (df['high'] - df['low']) * 0.5

# # target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
# df['target'] = df['open'] + df['range'].shift(1)

# # np.where(조건문, 참일때 값, 거짓일때 값)
# df['ror'] = np.where(df['high'] > df['target'],
#                      df['close'] / df['target'],
#                      1)

# # 누적 곱 계산(cumprod) -> 누적 수익률
# df['hpr'] = df['ror'].cumprod()

# # Draw Down 계산(누적 최대값과 현재 HPR 차이 / 누적 최대값 * 100)
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# # MDD 계산
# print("MDD(%): ", df['dd'].max())
# df.to_excel("dd.xlsx")