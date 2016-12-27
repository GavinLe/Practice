#-*- coding: utf8 -*-
import xlrd
from os import *
import json
fname = "abc.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
	# 根据名字获取 相对应的sheet
    sh = bk.sheet_by_name("data")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)
#print cell_value

row_list = []
wti = {"aa":None}

#获取各行数据
for i in range(1,nrows):
    row_data = sh.row_values(i)
    print "'"+'-'.join(row_data)+"',"
# wti['aa'] = row_list	
# fo = open("./res.json", "rw")
# fo.write(json.dumps(row_list, indent=4));
# fo.close()

# print row_list