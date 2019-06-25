Python version- 3.6.7


Requirements

Libraries-
1. Pillow
2. Requests
3. bs4(Beautiful Soup)
4. urllib
5. pytz
6. datetime

Subtask 1 (viewing user details)

1.Run the code in the file user_details.py. 

2.Enter the codeforces handle.

3.The code gives the users’ details as the output.


Subtask 2 (upcoming contest details and reminder)

1.Open the code in the file contest_details_and_reminder.py

2.Set up an account on msg91 and generate the APIkey.

3.Replace ############### in line no 128 in the file contests_details_and_reminder.py by the above generated APIkey.

4.Run the code in the file contests_details_and_reminder.py.

5.The name, start time, length and phase of the recent upcoming contests on codeforces is displayed.

6.To send reminder for the above contests enter the phone number and the reminder messages will be scheduled through msg91 API. The reminder mssages will be received on the given phone number 15 minutes before the start of the contest.

7.The sceduled time and scheduled request ID for all these upcoming contests is displayed in the output.

#The service provided by msg91 is not free though initially you get 50 free credits (i.e. you can send 50 free messages)
Screenshots
This folder contains the screenshot of output, received reminder messages and delivery report of scheduled messages.




MONITORING THE SITE FOR GETTING NEW CONTESTS

1.Open the code in the file monitoring_site.py.

2.Set up an acount on msg91 and generate the API key.

3.Replace ######### in line no 73 by the moblie no on which the reminder meassage is to be sent and ############# in line no 83 by the generated API key.

4.Run the code.

#This code automatically scrapes the content of the contest page of codeforces site after every 3 hours and if there are any contest within those 3 hours a reminder message is scheduled for all those contests.
#The first scraping of codeforces contests page starts 3 hours after you run the code.
#Do not shut down python and make sure you have an active internet connection.
