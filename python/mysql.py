# coding: utf-8
__author__ = 'srun'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

db_connect_string = 'mysql+mysqldb://root:root@127.0.0.1/ti?charset=utf8'


def getsession():
    engine = create_engine(db_connect_string, echo=True)
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session

session = getsession()


def underline_to_camel(underline_format):
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format


def show(tableName):
    _tableName = underline_to_camel(str(tableName))
    sql = "desc %s " % tableName
    result = session.execute(sql).fetchall()

    # for i in result:
    #     print """%s = Column('%s', String(45))""" % (i[0], i[0])
    new_path_filename = "F:\\sql\\%s.groovy" % _tableName
    f = open(new_path_filename, 'w')
    f.write("class %s { " % _tableName + "\n")

    src_path_filename = "F:\\template\\SysCitysSpec.groovy"
    _text = open(src_path_filename).readlines()
    _text[8] = "@TestFor(%s)\n" % _tableName
    _text[9] = "class %sSpec extends Specification {" % _tableName
    new_src_path_filename = "F:\\src\\%sSpec.groovy" % _tableName
    s = open(new_src_path_filename, 'w')
    s.writelines(_text)

    for i in result:
        a = str(i[1]).split("(")
        if a[0] == "varchar":
            f.write("    %s %s " % ("String", str(i[0]).lower()))
        elif a[0] == "int":
            f.write("    %s %s " % ("Integer", str(i[0]).lower()))
        elif a[0] == "datetime":
            f.write("    %s %s " % ("String", str(i[0]).lower()))
        elif a[0] == "bit":
            f.write("    %s %s " % ("Integer", str(i[0]).lower()))
        elif a[0] == "char":
            f.write("    %s %s " % ("String", str(i[0]).lower()))
        elif a[0] == "text":
            f.write("    %s %s " % ("String", str(i[0]).lower()))
        elif a[0] == "double":
            f.write("    %s %s " % ("Double", str(i[0]).lower()))
        else:
            f.write("    %s %s " % (i[1], str(i[0]).lower()))
        f.write("\n")
    f.write("    static constraints = { \n } \n")
    f.write("}")
    f.close()

tableNames = [
"sys_citys",
"sys_file_group",
"sys_files",
"ti_customer",
"ti_designate_order",
"ti_designate_order_products",
"ti_flow_path_terms",
"ti_installation_team",
"ti_installed_flow_path",
"ti_installed_progress_adjunct_history",
"ti_installed_progress_exception_history",
"ti_installed_progress_submission_history",
"ti_installed_progress_submission_terms",
"ti_order_products",
"ti_partner",
"ti_partner_contract",
"ti_product_series",
"ti_resource_partner_settlement_history",
"ti_resources_products",
"ti_submission_order",
"ti_worker",
"ti_worker_designate_history",
"ti_wechatmediatasks"]


# for j in session.execute("show tables").fetchall():
#     show(j[0])
for j in tableNames:
    show(j)

# show("ti_worker")

# print str("IsMySql").lower()

