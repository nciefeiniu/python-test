import requests
import json
import time
from datetime import timedelta, datetime
from air_ticket.headers import get_header
from air_ticket.database import database_mysql

# 爬取的数据
airdatas = []
# 出发的日期列表
searchday = [(datetime.today() + timedelta(days=daysNum)).__format__('%Y-%m-%d') for daysNum in range(1,30)]


for sd in searchday:
    # 请求网站
    url = r'http://www.ceair.com/otabooking/flight-search!doFlightSearch.shtml'
    # 请求数据
    datas = {'searchCond': '{"adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","tripType":"OW","recommend":false,"page":"0","sortType":"a","sortExec":"a","segmentList":[{"deptCd":"CTU","arrCd":"SHA","deptDt":"%s","deptAirport":"","arrAirport":"","deptCdTxt":"成都","arrCdTxt":"上海","deptCityCode":"CTU","arrCityCode":"SHA"}]}' % sd}
    # 请求头
    headers = get_header(1)
    headers['Referer'] = 'http://www.ceair.com/booking/ctu-sha-180522_CNY.html'
    # 代理
    proxies = {'http': 'http://140.143.96.219:3128'}
    try:
        resp = requests.post(url, headers=headers, data=datas, timeout=20)
        # 所有信息
        productInfo = json.loads(resp.text)['airResultDto']
        # 航班信息
        productUnits = productInfo['productUnits']
    except Exception as err:
        print("信息出错："+str(err))
        continue
    # 测试代理ip
    for pu in productUnits:
        # 仓位
        productcode = pu['productInfo']['productCode']
        # print(snk)
        flights = pu['oriDestOption'][0]
        # 航班号
        aircode = flights['flightNumberGroup']
        # 价格
        productprice = flights['score']['p']
        # 出发机场代码
        depair = flights['flights'][0]['departureAirport']['code']
        # 到达机场代码
        arrair = flights['flights'][0]['arrivalAirport']['code']
        # 出发时间
        deptime = flights['flights'][0]['departureDateTime'][-5:].replace(':', '')
        # 到达时间
        arrtime = flights['flights'][0]['arrivalDateTime'][-5:].replace(':', '')
        # 出发年月日
        date = flights['flights'][0]['departureDateTime'][0:11].replace('-', '').strip()
        airdatas.append([aircode,depair,arrair,deptime,arrtime,date,20180423,productcode,productprice,0])
    # time.sleep(10)

database_mysql(airdatas)

# for d in airdatas:
#     print(d)