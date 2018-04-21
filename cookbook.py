'''
* 东方航空
* 20180419
* by nicefeiniu
'''
import requests
import json
import time
from air_ticket.database import Databases


url = r'http://www.ceair.com/otabooking/flight-search!doFlightSearch.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer': 'http://www.ceair.com/booking/ctu-sha-180502_CNY.html',
    'Connection': 'keep-alive'
    }

datas = {'searchCond': '{"adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","tripType":"OW","recommend":false,"page":"0","sortType":"a","sortExec":"a","segmentList":[{"deptCd":"CTU","arrCd":"SHA","deptDt":"2018-05-02","deptAirport":"","arrAirport":"","deptCdTxt":"成都","arrCdTxt":"上海","deptCityCode":"CTU","arrCityCode":"SHA"}]}'}

proxies = {'https': 'http://192.168.56.40:3128'}
resp = requests.post(url, headers=headers, proxies=proxies, data=datas)
# 所有信息
productInfo = json.loads(resp.text)['airResultDto']
# 航班信息
productUnits = productInfo['productUnits']
for pu in productUnits:
    # 仓位
    productCode = pu['productInfo']['productCode']
    # print(snk)
    flights = pu['oriDestOption'][0]
    # 航班号
    airCode = flights['flightNumberGroup']
    # 价格
    productPrice = flights['score']['p']
    # 出发机场代码
    depAir = flights['flights'][0]['departureAirport']['code']
    # 到达机场代码
    arrAir = flights['flights'][0]['arrivalAirport']['code']
    # 出发时间
    depTime = flights['flights'][0]['departureDateTime'][-5:].replace(':', '')
    # 到达时间
    arrTime = flights['flights'][0]['arrivalDateTime'][-5:].replace(':', '')
    # 出发年月日
    date = flights['flights'][0]['departureDateTime'][0:11].replace('-', '')
    print('航班信息:'+airCode, date, depAir,depTime,arrAir,arrTime, productCode, productPrice)

    # d = Databases()
    # d.insert_db(airCode,depAir,arrAir,int(productPrice),int(date),int(depTime),int(arrTime),int(2018042115),productCode,int(0))



d = Databases()
d.insert_db('mu8738','CTU','CKG',200,20180421,2244,2344,2018042115,'safs',0)
