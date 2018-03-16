# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from daliulian import settings

class DaliulianPipeline(object):
    def __init__(self):
        #连接数据库
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            #插入到tv_name表
            #检查是否已经存在
            self.cursor.execute("""select * from tv_name where name=%s""", item['name'])
            repetition = self.cursor.fetchone()
            if repetition:
                print('Already exists in the database')
                self.cursor.execute("""select id from tv_name where name=%s""", item['name'])
                new_id = self.cursor.fetchone()[0]
            else:
                print('ok')
                self.cursor.execute("""insert into tv_name(name, f_url) VALUE(%s, %s) """, (item['name'], item['link']))
                # 获取自增ID,插入到tv_urls表
                new_id = self.cursor.lastrowid
            self.connect.commit()

            #去重
            for i in [item['baidu_link'],item['ed2k_link'],item['magnet_link'],item['thunder_link']]:
                if i is not None:
                    for k, v in i.items():
                        self.cursor.execute("""select * from tv_urls where url=%s""", v)
                        repetition = self.cursor.fetchone()
                        if repetition:
                            print('Already exists in the database')
                            continue
                        else:
                            print('ok')
                            self.cursor.execute("""insert into tv_urls(url_name, url, nid) VALUE(%s, %s, %s) """, (k, v, new_id))
                        self.connect.commit()
                else:
                    print("There is nothing inside")
        except Exception as error:
            print(error)
        return item

