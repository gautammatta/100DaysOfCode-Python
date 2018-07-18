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


eta = timedelta(hours = 6)
today = datetime.today()
print((str(today + eta)


timedelta()
####### EXERCISE ######## 

'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    dateStr = line.split(" ")[1]
    date = datetime.strptime(dateStr, '%Y-%m-%dT%H:%M:%S')
    return date
    pass


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    start = True   
    for line in loglines :
        if "Shutdown initiated" in line: 
            if start : 
                startLine = line
                start = False
            endLine = line
    startDate= datetime.strptime( startLine.split(" ")[1],            '%Y-%m-%dT%H:%M:%S')
    endDate = datetime.strptime( endLine.split(" ")[1] , '%Y-%m-%dT%H:%M:%S')
    return endDate-startDate
    pass



##### Test Cases 
from datetime import datetime, timedelta

#from logtimes import loglines, convert_to_datetime, time_between_shutdowns


def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    diff = time_between_shutdowns(loglines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'