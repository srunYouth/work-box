# coding: utf-8

__author__ = 'srun'

import sys
from flask import make_response, jsonify
from flask_cors import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import tiWorker
import json

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

db_connect_string = 'mysql+mysqldb://root:root@127.0.0.1/ti?charset=utf8'

reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask

app = Flask(__name__)
CORS(app, supports_credentials=True)

def getsession():
    engine = create_engine(db_connect_string, echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session

@app.route('/tiWorker', methods=['GET'])
def inspectVersions():
    session = getsession()
    map = dict(msg= "请求成功!")
    try:

        list = session.execute("select * from ti_worker").fetchall()
        res = session.query(tiWorker).all()
        print res
        for i in res:
            print type(i), type(res)
        # _list = []
        # for i in list:
        #     d = dict(
        #         id=i['id'],
        #         name=i['name'],
        #         phoneNum=i['phoneNum'],
        #         address=i['address'],
        #         experience=i['experience']
        #     )
        #     _list.append(d)
        print json.dumps(res)
        # return jsonify(res)
    except Exception as ex:
        print " error: ===== %s" % ex
        map["msg"] = "请求失败! %s" % ex
    finally:
        session.close()
    return jsonify(map)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, threaded=True, debug=True)



