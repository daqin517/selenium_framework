# from utils.config import *
#
# c = Config().get('log')
#
# print('c的类型为： ',type(c))
# print(c.get('file_name'))
import os
from xlrd import open_workbook

e = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(e)
e = os.path.join(e, 'data', 'baidu.xls')
# e = e.encode('utf-8')
print(os.path.dirname(os.path.abspath(__file__)))
# reader = open_workbook(e)
# print(reader)
