import time, sys
import configparser
import pymysql

'''
   * 日期时间，int型（date, depTime, arrTime, seaTime）
   * 如 2018041018
   * 后期好依据这个排序
'''
def database_mysql(airdatas):
    print(airdatas)
    conf = configparser.ConfigParser()
    try:
        # 读取配置文件
        conf.read('config.ini')
    except Exception as err:
        print('ERROR CONFIG: %s' % err)
        sys.exit(1)
    try:
        # 读取信息，链接MYSQL数据库
        conf = conf['MYSQL']
        conn = pymysql.connect(host=conf['Host'], user=conf['UserName'], password=conf['PassWord'],
                                    db=conf['DataBase'], port=int(conf['Port']))
        # 获取指针
        cur = conn.cursor()
    except  Exception as err:
        print("数据库连接错误！！请查案账号密码数据库名"+"ERROR CONNECT: %s" % err)
        sys.exit(1)

    # 插入
    for ad in airdatas:
        try:
            sql_insert = "INSERT INTO eastern_prices(aircode,depair,arrair,deptime,arrtime,flydate,seardate,productcode,price,types) VALUES('{aircode}','{depair}','{arrair}','{deptime}','{arrtime}','{flydate}','{searchdate}','{productcode}','{price}', {types});" .format(aircode=ad[0],depair=ad[1],arrair=ad[2],deptime=ad[3],arrtime=ad[4],flydate=ad[5],searchdate=ad[6],productcode=ad[7],price=ad[8],types=ad[9])
            print(sql_insert)
            cur.execute(sql_insert)
        except Exception as err:
            print('插入错误'+str(err))
            continue
    # 提交
    try:
        conn.commit()
    except Exception as err:
        print("提交错误"+str(err))
    finally:
        conn.close()
