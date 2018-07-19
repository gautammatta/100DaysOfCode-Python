#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:46:50 2018

@author: i0318
"""
    
from datetime import datetime, date, timedelta

today = datetime.today()
type(today)

todaydate = date.today()
type(todaydate)



print(todaydate.month)
print(todaydate.day)
print(todaydate.year)

## check the days left to christmas
christmas = date(2018,12,25)
print(christmas - todaydate)
print((christmas - todaydate).days)

if christmas is not todaydate : 
    print("Sorry there are still " + str((christmas - todaydate).days)+ " days until Christmas!")
    
    



################### Next Video #############


## timedelta ##
    
t = timedelta(days = 4 , hours = 10) 
type(t)

print(t.days)

### max of one day in drvonfd
print(t.seconds)

### how to calculate hours? 
print(t.seconds/60/60)
    
