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

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('ROW_MARKER', 'CARD_NUMBER', 'ENROLLMENT_DATE','BIRTH_DATE','T_C_ACCEPTED_DATE','REGION','COUNTRY_CODE','CITY','POSTCODE','SEATING_PREF1','SEATING_PREF2','BUSINES_FREQ','PLEASURE_FREQ','SMB_OWN','CC_AGREEMENT','EMAIL_AGREEMENT','POST_AGREEMENT','SMS_AGREEMENT','FAV1_AIRPORT','FAV2_AIRPORT','HOME_AIRPORT','GENDER','FIRST_NAME','MIDDLE_NAME','LAST_NAME','EMAIL' ))
    for i in range(10):
      #   writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
        writer.writerow( ('U', 'Karol%01d' % (i+1), '2014-06-08 09:04:13','2014-06-08 09:04:13','2014-06-08 09:04:13','A','BB-01','Cracov',0,'seatingpref','seatingpref1','businFreq','pleasureFreq','Unknown','ccagr','N','N','N','JFK','CUN','ORD','M','Bobby','Kris','Brown','boob@migmail.pl'))
finally:
    f.close()

#print open(sys.argv[1], 'rt').read()


q = open(sys.argv[2], 'awt')
try:
    writer = csv.writer(q)
    writer.writerow( ('ROW_MARKER','CODE','PARTNER','CHANNEL','CARD_NUMBER','TRANSACTION_DATE',	'PROCESSING_DATE','BOOKING_DATE', 'DEPARTURE_DATE','SOURCE_TRANSACTION_NO','BATCH_ID','USER_LOGIN','TRANS_TOTAL_VALUE','TRANSACTION_TYPE','TRANSACTION_STATUS','TARIFF','OND','BOOKING_LOCATION','AIRCRAFT_TYPE','AIRCRAFT_TAIL_NO','AIRLINE_MARKETING_CODE','ONLINE_BOOKING','PAX_TYPE','FEE_CODE','PARTNER_TRN_ID','TRANSACTION_CODE','TRANSACTION_FEE','TRANSACTION_POINTS','PARTNER_POINTS','IATA_LOCATION_CODE','PNR_LOCATOR','BASE_FARE','EXCISE_TAX','DISCOUNT_BASE','DISTANCE','COUPON_NO','AGENT_TYPE','IATA_LOC_NO','FLIGHT_NO','FLIGHT_NO_SUFFIX','OTHER_FFP_PROGRAM_CODE','OTHER_FFP_NO','TICKET_NO','TOUR_CODE','BULK_FARE_INDICATOR','FARE_BASIS','FLOWN_CLASS','TRANSACTION_VALUE','TRASNACTION_REVENUE','ADJUSTED_TRN_ID','CANCELLED_TRN_ID','TRN_EXT01','TRN_EXT02','TRN_EXT03','TRN_EXT04','TRN_EXT05','TRN_EXT06','TRN_EXT07','TRN_EXT08','TRN_EXT09','TRN_EXT10','TRN_EXT11','TRN_EXT12','TRN_EXT13','TRN_EXT14','TRN_EXT15','TRN_EXT16','TRN_EXT17','TRN_EXT18','TRN_EXT19','TRN_EXT20','TRN_EXT21','TRN_EXT22','TRN_EXT23','TRN_EXT24','TRN_EXT25'))
    for i in range(ile):
      #   writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
      #  writer.writerow( ('U', 'DUPA%01d' % (i+1), '2014-06-08 09:04:13','2014-06-08 09:04:13','2014-06-08 09:04:13','A','BB-01','Cracov',0,'seatingpref','seatingpref1','businFreq','pleasureFreq','Unknown','ccagr','N','N','N','JFK','CUN','ORD','M','Bobby','Kris','Brown','boob@migmail.pl'))
          writer.writerow( ('ROW_MARKER','CODE','PARTNER','CHANNEL','CARD_NUMBER','TRANSACTION_DATE',	'PROCESSING_DATE','BOOKING_DATE', 'DEPARTURE_DATE','SOURCE_TRANSACTION_NO','BATCH_ID','USER_LOGIN','TRANS_TOTAL_VALUE','TRANSACTION_TYPE','TRANSACTION_STATUS','TARIFF','OND','BOOKING_LOCATION','AIRCRAFT_TYPE','AIRCRAFT_TAIL_NO','AIRLINE_MARKETING_CODE','ONLINE_BOOKING','PAX_TYPE','FEE_CODE','PARTNER_TRN_ID','TRANSACTION_CODE','TRANSACTION_FEE','TRANSACTION_POINTS','PARTNER_POINTS','IATA_LOCATION_CODE','PNR_LOCATOR','BASE_FARE','EXCISE_TAX','DISCOUNT_BASE','DISTANCE','COUPON_NO','AGENT_TYPE','IATA_LOC_NO','FLIGHT_NO','FLIGHT_NO_SUFFIX','OTHER_FFP_PROGRAM_CODE','OTHER_FFP_NO','TICKET_NO','TOUR_CODE','BULK_FARE_INDICATOR','FARE_BASIS','FLOWN_CLASS','TRANSACTION_VALUE','TRASNACTION_REVENUE','ADJUSTED_TRN_ID','CANCELLED_TRN_ID','TRN_EXT01','TRN_EXT02','TRN_EXT03','TRN_EXT04','TRN_EXT05','TRN_EXT06','TRN_EXT07','TRN_EXT08','TRN_EXT09','TRN_EXT10','TRN_EXT11','TRN_EXT12','TRN_EXT13','TRN_EXT14','TRN_EXT15','TRN_EXT16','TRN_EXT17','TRN_EXT18','TRN_EXT19','TRN_EXT20','TRN_EXT21','TRN_EXT22','TRN_EXT23','TRN_EXT24','TRN_EXT25'))

finally:
    q.close()

#print open(sys.argv[2], 'rt').read()