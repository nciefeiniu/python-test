import time, sys
import configparser
import pymysql

'''
   * 日期时间，int型（date, depTime, arrTime, seaTime）
   * 如 2018041018
   * 后期好依据这个排序
'''
class Data:
    def __Connect(self):
        conf = configparser.ConfigParser()
        try:
            conf.read('config.ini')
        except Exception as err:
            print('ERROR CONFIG: %s' % err)
            sys.exit(1)
        conf = conf['MYSQL']
        # 链接mysql数据库，使用pymysql
        try:
            self.conn = pymysql.connect(host=conf['Host'], user=conf['UserName'], password=conf['PassWord'], db=conf['DataBase'], port=int(conf['Port']))
            self.cur = self.conn.cursor()
        except  Exception as err:
            print("ERROR CONNECT: %s" % err)
            sys.exit(1)
        return self.cur

    def insert_db(self,code: str, depAir: str, arrAir: str, minPrice: int, date: int, depTime: int, arrTime: int, seaTime: int):
        # print(type(conf['Port']))
        sql_insert = "INSERT INTO `ticket_prices`.`qunar_min_prices` (`aircode`, `depair`, `arrair`, `deptime`, `arrtime`, `date`, `seardate`, `minprice`) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (code,depAir,arrAir,depTime,arrTime,date,seaTime,minPrice)
        print(sql_insert)
        try:
            cur = self.__Connect()
            cur.execute(sql_insert)
            self.conn.commit()
        except Exception as err:
            print("ERROR INSERT: %s" % err)
            sys.exit(1)
        finally:
            cur.close()
            self.conn.close()



d = Data()
d.insert_db('CA1254','PVG','CNG',456,20180411,2244,2344,2018041121)


