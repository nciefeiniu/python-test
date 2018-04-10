import time, sys
import configparser
import pymysql

class Data:
    def __init__(self, **info):
        '''
        * 日期时间，int型（date, depTime, arrTime, seaTime）
        * 如 2018041018
        * 后期好依据这个排序
        '''
        self.depAir = info['depAir']
        self.arrAir = info['arrAir']
        self.minPrice = int(info['minPrice'])
        self.code = info['code']
        self.date = int(info['date'])
        self.depTime = int(info['depTime'])
        self.arrTime = int(info['arrTime'])
        self.seaTime = int(time.strftime('%Y%m%d%H',time.localtime()))

    def __Connect(self):
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        conf = conf['MYSQL']
        # 链接mysql数据库，使用pymysql
        try:
            self.conn = pymysql.connect(host=conf['Host'], user=conf['UserName'], password=conf['PassWord'], db=conf['DataBase'], port=int(conf['Port']))
            cur = self.conn.cursor()
        except  Exception as err:
            print("ERROR CONNECT: %s" % err)
            sys.exit(1)
        return cur

    def insert_db(self):
        # print(type(conf['Port']))
        sql_insert = "INSERT INTO `ticket_prices`.`qunar_min_prices` (`aircode`, `depair`, `arrair`, `deptime`, `arrtime`, `date`, `seardate`, `minprice`) VALUES('{0.code}', '{0.depAir}', '{0.arrAir}', '{0.depTime}', '{0.arrTime}', '{0.date}', '{0.seaTime}', '{0.minPrice}');".format(self)
        print(sql_insert)
        try:
            cur = self.__Connect()
            cur.execute(sql_insert)
            cur.close()
            self.conn.commit()
            self.conn.close()
        except Exception as err:
            print("ERROR INSERT: %s" % err)
            sys.exit(1)




d = Data(depAir='PNY', arrAir='PGV', minPrice=875, code='MU5431', date=20180410, depTime=2135, arrTime=2335, seaTime=2018041021)
d.insert_db()


