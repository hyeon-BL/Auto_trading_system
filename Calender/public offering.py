from urllib.request import urlopen
from bs4 import BeautifulSoup
# from github import Github, Issue
import datetime
from pytz import timezone
from dateutil.parser import parse
import os
import re

KST = timezone('Asia/Seoul')
today = datetime.datetime.now(KST)
print(today)


site = 'http://www.ipostock.co.kr'
res = urlopen(site + '/sub03/ipo06.asp')
soup = BeautifulSoup(res, 'html.parser')
day = soup.select('.days')
date = [d.select('strong') for d in day]


def search_stock(s):
    category = {3: '수요예측', 4: '청약', 6: '환불', 7: '상장'}
    raw = s.get('src')
    stock = re.search(r'ipo[0-9]', raw).group()
    return category[int(stock[-1])]


calender = {}
for d in date:
    try:
        t = d[0].get_text()
        calender[t] = [[], []]
        print(t, '일', '공모주')
        stock = day[date.index(d)].select('a')
        img = day[date.index(d)].select('img')
        for i in img:
            calender[t][0].append(search_stock(i))
        for s in stock:
            calender[t][1].append(s.get('title'))
    except:
        print('공모주 없음')
print(calender)



# GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
# REPO_NAME = "crawler-study-gathering"
# repo = Github(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
# if issue_body != '' and REPO_NAME == repo.name:
#     res = repo.create_issue(title=issue_title, body=issue_body)
#     print(res)