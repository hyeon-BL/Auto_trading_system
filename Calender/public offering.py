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

def isDateInRange(created_at):
    suffix_KST = '.000001+09:00'
    created_at = parse(created_at + suffix_KST)
    yesterday = today - datetime.timedelta(1)
    return today > created_at and created_at > yesterday

site = 'http://www.ipostock.co.kr'
res = urlopen(site + '/sub03/ipo06.asp')
soup = BeautifulSoup(res, 'html.parser')
day = soup.select('.days')
print(day)
date = [d.select('strong') for d in day]
print(date)


def search_stock(s):
    category = {3: '수요예측', 4: '청약', 6: '환불', 7: '상장'}
    raw = s.get('src')
    stock = re.search(r'ipo[0-9]', raw).group()
    return category[int(stock[-1])]


calender = [[], []]
for d in date:
    try:
        print(d[0].get_text(), '일', '공모주')
        stock = day[date.index(d)].select('a')
        img = day[date.index(d)].select('img')
        for i in img:
            calender[0].append(search_stock(i))
        for s in stock:
            calender[1].append(s.get('title'))
    except:
        print('공모주 없음')
print(calender, len(calender[0]), len(calender[1]))
# issue_body = ''

# for row in article_list:
#     title = row.select('h5 > a')[0]
#     published_at = row.select('div.date-created span.timeago')[0].get_text()
#     item = published_at + " " +  str(title).replace('href="','href="' + site).replace("\n", "").replace('  ', '').strip() + '<br/>\n'
#     if '마감' not in str(title) and isDateInRange(published_at):
#         issue_body += item
#     else: 
#         print('[filtered] ', item)

# print('----------------------------------------------------------------------')

# issue_title = "스터디 모집 글 모음(%s)" % (today.strftime("%Y년 %m월 %d일 %H시"))
# print(issue_title)
# print(issue_body)

# GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
# REPO_NAME = "crawler-study-gathering"
# repo = Github(GITHUB_TOKEN).get_user().get_repo(REPO_NAME)
# if issue_body != '' and REPO_NAME == repo.name:
#     res = repo.create_issue(title=issue_title, body=issue_body)
#     print(res)