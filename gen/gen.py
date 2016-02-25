#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys


# print 'Ahoj, przygodo!'

# c = csv.writer(open("file.csv", "wb"))
# c.writerow(["Name","Address","Telephone","Fax","E-mail","Others","\nKarol"])

# cr = csv.reader(open("file.csv","rb"))

# for row in cr: 
#     print row

# for row in cr: 
#     print row[1], row[1]


# doc = csv.writer(sys.stdout, lineterminator='\n')
# doc.writerow('abc')
# doc.writerow(range(3))

ile = int(sys.argv[3])
csv.register_dialect('excel', delimiter='|', quoting=csv.QUOTE_NONE)

f = open(sys.argv[1], 'wt')
ileuserow = 1
try:
    writer = csv.writer(f,delimiter = '|')
    writer.writerow(('ROW_MARKER','CARD_NUMBER','ENROLLMENT_DATE','BIRTH_DATE','T_C_ACCEPTED_DATE','STATUS','REGION','COUNTRY_CODE','CITY','POSTCODE','SEATING_PREF1','SEATING_PREF2','BUSINES_FREQ','PLEASURE_FREQ','SMB_OWN','CC_AGREEMENT','EMAIL_AGREEMENT','POST_AGREEMENT','SMS_AGREEMENT','FAV1_AIRPORT','FAV2_AIRPORT','HOME_AIRPORT','GENDER','FIRST_NAME','MIDDLE_NAME','LAST_NAME','EMAIL'))
    for i in range(ileuserow):
           writer.writerow( ('U','westpalmbeach10','2014-06-08 09:04:13','2016-02-13 00:00:00','2014-06-08 00:00:00','A','BB-01','BRB','westpalmbeach','0','westpalmbeach','westpalmbeach','westpalmbeach','westpalmbeach','Unknown','N','N','N','','JFK','','BGI','F','westpalmbeach','westpalmbeach','westpalmbeach','westpalmbeach@HOTMAIL.COM','25167','2014-05-09 00:00:00','2015-03-01 00:00:00','','','2014-03-16 00:00:00','','F','W','B6','','MR','','60 Simmons Road','cancun','','2417373','M','','','','','','','en-us','ENG','','F','','','','','','','','0'))
    writer.writerow(('T',ileuserow))

finally:                                                                                                                                                         
   f.close()




q = open(sys.argv[2], 'awt')
try:
    writer = csv.writer(q,delimiter = '|')
    writer.writerow( ('ROW_MARKER','CODE','PARTNER','CHANNEL','CARD_NUMBER','TRANSACTION_DATE', 'PROCESSING_DATE','BOOKING_DATE', 'DEPARTURE_DATE','SOURCE_TRANSACTION_NO','BATCH_ID','USER_LOGIN','TRANS_TOTAL_VALUE','TRANSACTION_TYPE','TRANSACTION_STATUS','TARIFF','OND','BOOKING_LOCATION','AIRCRAFT_TYPE','AIRCRAFT_TAIL_NO','AIRLINE_MARKETING_CODE','ONLINE_BOOKING','PAX_TYPE','FEE_CODE','PARTNER_TRN_ID','TRANSACTION_CODE','TRANSACTION_FEE','TRANSACTION_POINTS','PARTNER_POINTS','IATA_LOCATION_CODE','PNR_LOCATOR','BASE_FARE','EXCISE_TAX','DISCOUNT_BASE','DISTANCE','COUPON_NO','AGENT_TYPE','IATA_LOC_NO','FLIGHT_NO','FLIGHT_NO_SUFFIX','OTHER_FFP_PROGRAM_CODE','OTHER_FFP_NO','TICKET_NO','TOUR_CODE','BULK_FARE_INDICATOR','FARE_BASIS','FLOWN_CLASS','TRANSACTION_VALUE','TRASNACTION_REVENUE','ADJUSTED_TRN_ID','CANCELLED_TRN_ID','TRN_EXT01','TRN_EXT02','TRN_EXT03','TRN_EXT04','TRN_EXT05','TRN_EXT06','TRN_EXT07','TRN_EXT08','TRN_EXT09','TRN_EXT10','TRN_EXT11','TRN_EXT12','TRN_EXT13','TRN_EXT14','TRN_EXT15','TRN_EXT16','TRN_EXT17','TRN_EXT18','TRN_EXT19','TRN_EXT20','TRN_EXT21','TRN_EXT22','TRN_EXT23','TRN_EXT24','TRN_EXT25'))
    for i in range(ile):      
         writer.writerow( (  'I','842166164','B6','12','westpalmbeach10','2015-02-03 00:00:00','2015-03-07 01:03:51','2015-02-02 00:00:00','2015-02-03 00:00:00','','17470','System','0','I','1','Y','PBIPBI','seattle10','32F','32F658','B6','F','A','','','','','1922','','Salt Lake Support Center','ONGBGB','298.05','22.35','298.05','1000','1','A','4100003','8072','','','','2125457278','','N','QH00AE5U','Y','','','','','','','B6','8072','SLC','ORL','9010001','WEB - B2C / GUEST - USA','2015-01-08 00:00:00','279','QHIP','','','','','7664','L','P','','','','','','',))
    writer.writerow(('T',ile))
finally:
    q.close()

