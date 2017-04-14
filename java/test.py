# coding: utf-8

# class A():
#     a = 1
#
# class B(A):
#     b = 2
#     def test(self):
#         c = self.b +  self.a
#
#         print c
#
# bb = B()
# bb.test()
#
# lt = [
#     'SERID',
#     'USERNO',
#     'UNAME',
#     'UTEL',
#     'N1',
#     'N2',
#     'N3',
#     'N4',
#     'REMARK',
#     'SDATE',
#     'STIME',
#     'CALLNUM',
#     'CALLID',
#     'HWCALLID',
#     'ANJSTR'
# ]
#
# for a in range(len(lt)):
#     print """this.getFormHM().put("%s", %s)""" % (lt[a], lt[a])
#     print """this.set%s((String) this.getFormHM().get("%s"));""" % (lt[a], lt[a])
#
# undefined = "undefined"
# d = dict(ANJSTR= "6", CALLID= "4", CALLNUM= "3", HWCALLID= "5", N1= "",
#  N2= undefined, N3= undefined, N4= undefined, REMARK= "",
#  UNAME= "", USERNO= "1", UTEL= "2")
#
#
# for key in d:
#     print """String %s = request.getParameter("%s");""" % (key, key)
#
# print d
#
# a = [
#         {
#             "USERNO": "3", "N4": "7", "N1": "6", "SDATE": "4", "STIME": "g", "N2": "54",
#             "UTEL": "5", "CALLNUM": "g", "HWCALLID": "1480486143-10", "ANJSTR": "g", "STIF_FLAG": "3",
#             "UNAME": "4", "CALLTYPE": "2", "END_TIME": "2016-11-30 14:51:14", "SERID": "2",
#             "START_TIME": "2016-11-30 14:50:09", "N3": "7", "REMARK": "7777", "ID": "11100320161130140910",
#             "CALLID": "1110031611301409102880"
#         }
#      ]
#
# for i in a:
#     for key in i:
#         print key
#
# STIF_FLAG; // 满意度
# CALLTYPE; // 服务类型
# START_TIME; // 通话开始时间
# ID; // 客户id
# END_TIME; // 通话结束时间
#
# a = dict(ANJSTR="6", CALLID="4", CALLNUM="3", HWCALLID="5", N1="1001",
#          N2="1001004", N3="100100403", N4="10010040301", REMARK="省际工单EMS/速递揽...",
#          UNAME="", USERNO="1", UTEL="")
#
# for key in a:
#     print """String %s  = request.getParameter("%s");""" % (key, key)
# t = ['SERID', 'USERNO', 'UNAME', 'UTEL', 'N1', 'N2', 'N3', 'N4', 'REMARK',
#      'SDATE', 'STIME', 'CALLNUM', 'CALLID', 'HWCALLID', 'ANJSTR']
#
# for i in t:
#     print """str.append(" '" +%s+ "' , ");""" % i
#     pass

# var n1 = document.getElementById("serve.String(N1)").value;
# 			var n2 = document.getElementById("serve.String(N2)").value;
# 			var n1 = document.getElementById("serve.String(N1)").value;
# 			var n1 = document.getElementById("serve.String(N1)").value;
# a = {"SERID" : '1', "USERNO" : '1', "UNAME" : 'naame', "UTEL" : '122', "N1" : '1001', "N2" : '1001004', "N3" : '100100403',
#  "N4" : '10010040301', "REMARK" : '省际工单EMS/速递揽收标准快递', "SDATE" : '2017-03-29', "STIME" : '07:02:12',
#  "CALLNUM" : '3', "CALLID" : '4', "HWCALLID" : '5', "ANJSTR" : '6'}
#
# for key in a:
#     print """str.append("%s = '"+ %s + "'," );""" % (key, key)
#
# SERID = '1'
# USERNO = '1'
# UNAME = 'naame'
# UTEL = '122'
# N1 = '1001'
# N2 = '1001004'
# N3 = '100100403'
# N4 = '10010040301'
# REMARK = '省际工单EMS/速递揽收标准快递'
# SDATE = '2017-03-29'
# STIME = '07=02=12'
# CALLNUM = '3'
# CALLID = '4'
# HWCALLID = '5'
# ANJSTR = '6'
# CALLTYPE, START_TIME,ID,STIF_FLAG = "1","1","1","1"
#
#
# s = "<tr bordercolor='#C9C9C9' class='back4'> " + \
#     "<td align='center' class='td_list_title'>" + \
#         SERID + \
#     "</td>" + \
#     "<td align='center' class='td_list_title'>" +\
#         SDATE +\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         START_TIME+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         CALLTYPE+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         CALLTYPE+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         REMARK+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         ID+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         ID+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>"+\
#         STIF_FLAG+\
#     "</td>"+\
#     "<td align='center' class='td_list_title'>" +\
#         STIF_FLAG +\
#     "</td>" +\
# "</tr>"
#
# print s

# print('\n'.join([''.join([('AndyLove'[(x-y) % 8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# print('\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n)) (lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1)) (0,0.02* x +0.05j * y, 40))2 else ' ' for x in range(-80,20)])for y in range(-20,20)]))

import random

print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))


def guess_my_number(n):
    while True:
        user_input = raw_input(u"Enter a positive integer to guess(游戏开始): ")
        if len(user_input) == 0 or not user_input.isdigit():
            print(u"Not a positive integer(不能违反规则哦)!")
        else:
            user_input = int(user_input)
            if user_input > n:
                print(u"Too big(太大了) ! Try again(再试一次)!")
            elif user_input < n:
                print(u"Too small(太小了) ! Try again(再试一次)!")
            else:
                print(u"You win(你赢了)!")
                return True


# guess_my_number(random.randint(0, 99))
