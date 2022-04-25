#-*- coding :utf-8-*-
"""
Created on Sun Apr 25 9:22 2022


@author: Administrator
"""

from datetime import datetime
from re import I
import time
a=time.time()
b=time.localtime(a)
c=time.ctime(a)
print(c)



from datetime import *
a# = datetime.now()
a= datetime.today() 
print(a)

import time
def time_convert(sec):
    mins =sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed ={0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
input("press Enter to start")
start_time = time.time() 
try:
    hours =0
    while True:
        for minutes in range(0,60):
            for seconds in range(0,60):
                time.sleep(1)
                print(hours,";",minutes,";",seconds+1)
except KeyboardInterrupt:
    end_time =time.time()
    time_lapsed =end_time-start_time
    time_convert(time_lapsed)

