# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:20:30 2019

@author: Abhilasha
"""

import urllib.request as u
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from pytz import timezone
import http.client

#using web scraping to scrape the contest details from codeforces' site
contest = "https://codeforces.com/contests"
page = u.urlopen(contest)
soup = BeautifulSoup(page,features="html5lib")

#to look at the structure of HTML page
#print(soup.prettify)

#getting all the links, titles and other info 
soup.find_all('a')

#to get only the links
all_links=soup.find_all('a')
#for link in all_links:
 #   print (link.get("href"))
    
rows = soup.find_all('tr')
#print(rows)

for row in rows:
    row_td = row.find_all('td')
#print(row_td)
#type(row_td)

all_tables=soup.find_all('table')
#print(all_tables)

right_table=soup.find('table', class_='')
#print(right_table)

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
import pandas as pd
    
#triming the spaces and newline characters in string
d=[]
for i in D:
    j = i.replace(' ','')
    k=j.replace('\n','')
    d.append(k)
a=[]   
for i in A:
    j = i.replace(' ','')
    k=j.replace('\n','')
    a.append(k)
    
e=[]
for i in E:
    j = i.replace(' ','')
    k=j.replace('\n','')
    e.append(k)
    
#changing the timezone to Asia/Kolkata
    T=[]
for i in C:
    date_str = i
    datetime_obj = datetime.strptime(date_str, "%b/%d/%Y %H:%M")
    datetime_ob = timezone('Europe/Moscow').localize(datetime_obj)
    datetime_obj_ind = datetime_ob.astimezone(timezone('Asia/Kolkata'))
    T.append(datetime_obj_ind.strftime("%Y-%m-%d %H:%M:%S"))

print("\n\n**********UPCOMING CONTEST DETAILS**********\n\n")
df=pd.DataFrame()
df['Name']=a
df['Start']=C
df['Length']=d
df['Phase']=e
print(df)




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
print("Enter the moblie no")
mob=input()
msg="Hey!%20The%20codeforces%20contest%20is%20about%20to%20start%20"
for i in rem:
    url="/api/sendhttp.php?campaign=&response=&afterminutes=&schtime="+i+"&flash=&unicode=&mobiles="+mob+"&authkey=278382AURbibyU5cea80f6&route=4&sender=TESTIN&message="+msg+"&country=91"
    conn.request("GET",url)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

print("Reminder messages have been scheduled for the above contests")
