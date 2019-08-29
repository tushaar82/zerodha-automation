# Zerodha Selenium Automation

"""
Created on Thu June 6  08:45:35 2019
@author: Tushar Chaudhari
@email : tushaar.chaudhari@gmail.com
@key : 32e76465f8acefff449e6476b6c9258bc3c35eb5

"""
# Importing Packages 

from datetime import datetime, time
from datetime import timedelta
import time as sleep
import os
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from stocktrends import indicators
from talib import EMA
from selenium import webdriver
import time
#import pysql

# connect to MySQL database.



# 1) load web driver
browser = webdriver.Chrome('chromedriver.exe')
print('Web Driver Loaded')
# 2) delete cookies and chache of browser
browser.delete_all_cookies()
print('cookies Deleted')
# 3) load kite.zerodha.com in browser
browser.get('http://kite.zerodha.com')
print('Zerodha Loaded')
# 4) check if login page opened
print('Login Page Opened')
# 5) enter user name and password
print('User Name & Password Entered')
# 6 )enter pin
print('Pin Entered')
# 7 ) check if user loged in correctly
print('Logged in Sucessfully')
# 8) Send Telegram Message
print('Telegram Message Send')

    
   


def savehistdata():
    # 0) Crude Oil Graph Open
    print('Crude Oil Page Opened')
    # 1) check if required page is opened
    # 2) get OHLC data 
    print('OHLC Data Extracted')
    # 3) Save it in database
    print('OHLC Data saved sucessfully')
    # 4) send telegram message
    print('Telegram Message Send')

def buy():
    # 1) check if required page is opened
    print('Buy')
    print('Buy Link Clicked')
    # 2) click on buy button
    print('values entered')
    # 3) enter values
    print('Crude Oil Lot Buyed')
    # 4) confirm

def sell():
    # 1) check if required page is opened
    print('Sell')
    # 2) click on buy button
    print('Sell Link CLicked')
    # 3) enter values
    print('value entered')
    # 4) confirm
    print('Crude Oil Selled')

def closealltrades():
    # 1) selenium code to close all trades
    print('Closed all open trades')


def strategy():
    # 1) read dataframe
    print('Read Hist Data')
    # 2) Convert to renko ohlc data
    # 3) Calculate Moving Avegrages
    # 4) Buy and sell accordingly
    print('Sell Signal Generated')
    sell()
    closealltrades()


def CheckTrades():
    from datetime import datetime, time
    from datetime import timedelta
    import time as sleep
    now = datetime.now()
    now_time = now.time()
    end_dt = datetime.now().strftime("%d/%m/%Y")
    start_dt = (datetime.now() - timedelta(3)).strftime('%d/%m/%Y')

    if time(9,0) <= now_time <= time(14,15):
        

        for script in range(1):
            print("~~~~~~~~~~~~~~~~~~~~~~~ \n Now the time is: %s" % datetime.now().time())
            print("CHecking Parameters")
            savehistdata()
            strategy()
          
        
            
    elif time(14,58) <= now_time <= time(15,00):
        print("Exiting all the open position now and exiting execution")
        #log.write("Exiting all the open position now and exiting execution")
        closealltrades() #Cancel all open orders
        #log.close()
        #execution.close()
        exit()

    else:
        print("There is no market activity now. Checking in 2 mins.. Now the time is: %s" % datetime.now().time())
        #log.write("There is no market activity now. Checking in 2 mins.. Now the time is: %s" % datetime.now().time())
        sleep.sleep(120)

#%%
while True:
    

    CheckTrades()
    print("\n***Now waiting for 5 seconds")
    #log.write("\n***Now waiting for 320 seconds")
    sleep.sleep(5)




