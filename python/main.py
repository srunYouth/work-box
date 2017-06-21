# coding: utf-8
__author__ = 'srun'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

db_connect_string = 'mysql+mysqldb://root:root@127.0.0.1/ti?charset=utf8'


class dispose(object):
    def getsession(self):
        engine = create_engine(db_connect_string, echo=True)
        db_session = sessionmaker(bind=engine)
        session = db_session()
        return session


class init():

    def __init__(self, tableName, field):
        self.tableName = tableName  # 要修改的表
        self.field = field  # 要修改的字段
        self.param = None  # 参数集
        self.id = None  #   ID
        self.city = None  # 城市
        self.province = None  # 省
        self.county = None  # 区县
        self.isOk = []  # 成功记录
        self.error = []  # 错误记录

    def getResult (self):
        session =  dispose().getsession()
        try:
            sql = """select * from %s """ % self.tableName
            result = session.execute(sql).fetchall()
            return result
        except Exception as ex:
            print "error : {%s}" % ex
        finally:
            session.close()

    def setParam(self):
        session = dispose().getsession()
        try:
            sql = """ update %s tp set % = '%s' where id =  '%s' """ % (self.tableName, self.field, self.city, self.id)
            val = session.execute(sql)
            session.commit()
            if val is not None:
                self.isOk.append(self.id)
        except Exception as ex:
            print "error : {%s}" % ex
            self.error.append(self.id)
        finally:
            session.close()

    def action(self):
        for i in self.getResult():
            self.city = `i[self.field]`.split("/")[1]
            self.id = i["id"]
            self.setParam()


model = init("ti_customer", "cityId")
model.action()
print "insert ok :  %s"  % model.isOk
print "insert error :  %s" % model.error
