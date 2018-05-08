# import datetime
# import time
#
# print(time.localtime(time.time()))
# tim = time.strftime('%Y%m%d%H', time.localtime(time.time()))
# print(type(tim))
# tim = int(tim)
# print(type(tim))
# print(tim)

# ti = datetime.date.today()
# print(format(ti, '%Y%m%d%H'))

import requests
proxies = {'http': 'http://140.143.96.219:3128'}
resp = requests.get('https://httpbin.org/ip', proxies=proxies)
print(resp.text)

#
# from air_ticket.database import Databases
#
# d = Databases()
# d.insert_db('mu8738', 'CTU', 'CKG', 200, 20180421, 2244, 2344, 2018042115, 'safs', 0)

# from _datetime import datetime, timedelta
# import random
#
# t = datetime.today()
# print(t)
# print(t + timedelta(days=30))
#
# searchDay = [(datetime.today() + timedelta(days=daysNum)).__format__('%Y-%m-%d') for daysNum in range(1,60)]
# for sd in searchDay:
#     print("sasfasf %s" % sd)

