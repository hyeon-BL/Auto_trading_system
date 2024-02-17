import pyupbit
import pandas as pd
import time
from datetime import datetime

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=200)

how = {
    'open':'first', # 시가는 처음 값
    'high':'max', # 고가는 최대값
    'low':'min', # 저가는 최소값
    'close':'last', # 종가는 마지막 값
    'volume':'sum' # 거래량은 합계
}

f = df.resample('2T').apply(how) # 2분봉으로 변환
print(f)
dfs = []



# interval 늘리기
start = '2019-01-01'
last = datetime.now()
while True:
    df = pyupbit.get_ohlcv("KRW-BTC", to=last)
    last = df.index[0]
    dfs.append(df)

    if start in df.index:
        break
    time.sleep(0.1)
result = pd.concat(dfs).sort_index()
print(result)