import time

class Data:
    def __init__(self, **info):
        '''
        * 日期时间，int型（date, depTime, arrTime, seaTime）
        * 如 2018041018
        * 后期好依据这个排序
        '''
        self.minPrice = info['minPrice']
        self.code = info['code']
        self.date = info['date']
        self.depTime = info['depTime']
        self.arrTime = info['arrTime']
        self.seaTime = time.strftime('%Y%m%d%H',time.localtime())

    def __get__(self, instance, owner):
        print('test')
        return self


da = Data(minPrice=982, code='tv9845', date=20180410, depTime=2204, arrTime=2359)
print(da.seaTime)