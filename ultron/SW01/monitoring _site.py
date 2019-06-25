# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:24:30 2019

@author: Abhilasha
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request as u
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from pytz import timezone
import http.client
import pandas as pd

#this function is executed after every 6 hours
def job_function():
    #web scraping
    contest = "https://codeforces.com/contests"
    page = u.urlopen(contest)
    soup = BeautifulSoup(page,features="html5lib")
    soup.find_all('a')
    all_links=soup.find_all('a')
    rows = soup.find_all('tr')
    for row in rows:
        row_td = row.find_all('td')
    all_tables=soup.find_all('table')
    right_table=soup.find('table', class_='')
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    cnt=0
    for row in right_table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells)==6: 
            A.append(cells[0].find(text=True))
            B.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(cells[5].find(text=True))  
    for row in right_table.findAll("a"):
        cells = row.findAll('span')
        if len(cells)==1: 
            C.append(cells[0].find(text=True))
            
    #changing the timezone to Asia/Kolkata
    T=[]
    for i in C:
        date_str = i
        datetime_obj = datetime.strptime(date_str, "%b/%d/%Y %H:%M")
        datetime_ob = timezone('Europe/Moscow').localize(datetime_obj)
        datetime_obj_ind = datetime_ob.astimezone(timezone('Asia/Kolkata'))
        T.append(datetime_obj_ind.strftime("%Y-%m-%d %H:%M:%S"))
    R=[]  
    
    #storing the time at which the reminder is to be sent(15 minutes before the contest starts)
    for i in T:
        a = datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
        b=str(a-timedelta(minutes=15))
        R.append(b)   
    rem=[]
    for i in R:
        date_str = i
        datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        rem.append(datetime_obj.strftime("%Y/%m/%d %H:%M:%S"))
    
    #using msg91 api to send message
    conn = http.client.HTTPSConnection("api.msg91.com")
    #replace ########## in line no 71 with 10 digit mobile number
    mob="##########"
    print("Reminder messages have been scheduled for these contests with the following request ids")
    msg="Hey!%20The%20codeforces%20contest%20is%20about%20to%20start%20"
    a = datetime.now()
    b = a + timedelta(hours = 3) 
    for i in rem:
        j = datetime.strptime(i, "%Y/%m/%d %H:%M:%S")
        
        #replace '##################' in the next line by the api key generated after setting up an account on msg91
        if j>= a and j<=b:
            url="/api/sendhttp.php?campaign=&response=&afterminutes=&schtime="+i+"&flash=&unicode=&mobiles="+mob+"&authkey=####################&route=4&sender=TESTIN&message="+msg+"&country=91"        
            conn.request("GET",url)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8")," Scheduled Time ",i)


sched = BlockingScheduler()
#The code runs after every 3 hours and if there is a contest within this time period a reminder is scheduled for it 15 minutes before its start.
sched.add_job(job_function, 'interval', hours=3)
sched.start()