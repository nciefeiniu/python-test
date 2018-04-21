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


proxies = {'https': 'http://192.168.56.40:3128'}
resp = requests.get('https://httpbin.org/ip', proxies=proxies)
print('test')
print(resp.text)