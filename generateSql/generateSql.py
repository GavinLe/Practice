#-*- coding: utf8 -*-
import xlrd
from os import *
import json
fname = "/Users/gavin/Desktop/insert_data.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
	# 根据名字获取 相对应的sheet
    sh = bk.sheet_by_name("a")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
# ,REDEMPTION_STATUS, IS_OFFLINE,LOAN_PRICE,LOAN_AMOUNT,RES_STATUS,GOODSID,INTERFACE_TYPE,PACK_COMMENTS9, GOODSPRICE,REDEMPTION_DATETIME,LOAN_LOCK_STATUS

insert_sql = "Insert into RNTRADE.LOAN_PACKDETAIL (LOANPACK_ID,PACK_CODE,FACTORY_RES_CODE,PACK_ID,PRODUCT_TYPE_CODE,PRODUCT_TYPE_NAME,PRODUCT_NAME,PRODUCT_CODE,SHOP_SIGN,SPEC,PIECES,SPECIAL,WEIGHT,WAREHOUSE_CODE,WAREHOUSE_NAME,LOCATION,BRANDID,MANUFACTURER,PRICE,PACK_AMOUNT,IN_DATE,REDEMPTION_STATUS, IS_OFFLINE,LOAN_PRICE,LOAN_AMOUNT,RES_STATUS,GOODSID,INTERFACE_TYPE,PACK_COMMENTS9, GOODSPRICE,REDEMPTION_DATETIME,LOAN_LOCK_STATUS) values"

row_list = []

#获取各行数据
for i in range(1,nrows):
	row_data = sh.row_values(i)
	insert_value = "(%s,'%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7],row_data[8],row_data[9],row_data[10],'',row_data[12],row_data[13],row_data[14],row_data[15],row_data[16],row_data[17],row_data[18],row_data[19],'',0,0,0,0,1,'goodsid',1,'','','','')
	print insert_sql + insert_value + ';'
	
	
# wti['aa'] = row_list	
# fo = open("./res.json", "rw")
# fo.write(json.dumps(row_list, indent=4));
# fo.close()

#print "update rnrsbrand.query_availablepackage set loancontractno= '%s', provider_loan='OYF' where pack_code = '%s'" %(row_data)
# print row_list