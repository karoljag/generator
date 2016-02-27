#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
import datetime
import os
import shutil

# filename = "/Pulpit/generator/filenameConst"
# save_path = '/home/karolubu/Pulpit/generator'

# name_of_file = raw_input("What is the name of the file: ")

# completeName = os.path.join(save_path, name_of_file+".txt")         

# file1 = open(completeName, "w")

# toFile = raw_input("Write what you want into the field")

# file1.write(toFile)

# file1.close()

userId = "PathCsvUserName"
now = datetime.datetime.now()
myDate = now.strftime("%Y%m%d%H%M%S")

usrPath = r'/home/karolubu/Pulpit/generator/dane/'+myDate+'/usr' 
if not os.path.exists(usrPath):
    os.makedirs(usrPath,0755)

# f = open(r"/home/karolubu/Pulpit/generator/papa/JETBLUE_MEMBERS_"+myDate+".csv", "a")
f = open(usrPath+"/JETBLUE_MEMBERS_"+myDate+".csv", "a")
# member = open("JETBLUE_MEMBERS_"+myDate+".csv", 'wt')
ileuserow = 1
try:
    writer = csv.writer(f,delimiter = '|')
    writer.writerow(('ROW_MARKER','CARD_NUMBER','ENROLLMENT_DATE','BIRTH_DATE','T_C_ACCEPTED_DATE','STATUS','REGION','COUNTRY_CODE','CITY','POSTCODE','SEATING_PREF1','SEATING_PREF2','BUSINES_FREQ','PLEASURE_FREQ','SMB_OWN','CC_AGREEMENT','EMAIL_AGREEMENT','POST_AGREEMENT','SMS_AGREEMENT','FAV1_AIRPORT','FAV2_AIRPORT','HOME_AIRPORT','GENDER','FIRST_NAME','MIDDLE_NAME','LAST_NAME','EMAIL'))
    for i in range(ileuserow):
           writer.writerow( ('U',userId,'2014-06-08 09:04:13','2016-02-13 00:00:00','2014-06-08 00:00:00','A','BB-01','BRB','westpalmbeach','0','westpalmbeach','westpalmbeach','westpalmbeach','westpalmbeach','Unknown','N','N','N','','JFK','','BGI','F','westpalmbeach','westpalmbeach','westpalmbeach','westpalmbeach@HOTMAIL.COM','25167','2014-05-09 00:00:00','2015-03-01 00:00:00','','','2014-03-16 00:00:00','','F','W','B6','','MR','','60 Simmons Road','cancun','','2417373','M','','','','','','','en-us','ENG','','F','','','','','','','','0'))
    writer.writerow(('T',ileuserow))

finally:                                                                                                                                                        
	f.close()


shutil.make_archive('output_filename.zip', 'zip', "/home/karolubu/Pulpit/generator/filenameConst")
# shutil.make_archive("desired_zipfile_name_no", "zip", "name_of_the_folder_you_want_to_zip")