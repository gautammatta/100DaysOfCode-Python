#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:11:55 2018

@author: gmatta
"""
    
from datetime import datetime,  timedelta
import time


def start_timer():
    current_time = datetime.today()
    delta = timedelta(minutes= 25)
    return current_time + delta



def check_time(end_time):
    current_time = datetime.today()
    timeToFinish = end_time - current_time
    minutes_left = timeToFinish.seconds//60
    seconds_left = timeToFinish.seconds%60
    if minutes_left > 0: 
        print(str(minutes_left).zfill(2) + ":" + str(seconds_left).zfill(2))
        return timeToFinish.seconds
    else : 
        print("Goodbye! \n\n\n\n")
        return 0


def display_countdown(delta): 
    while delta:
        print(str(delta//60).zfill(2) + ":" + str(delta%60).zfill(2))
        time.sleep(1)
        delta -=1
    
    
end_time = start_timer()
timeLeft = check_time(end_time)
display_countdown(timeLeft)
