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


1.Set up an account on msg91 and generate the APIkey.

2.Replace ############### in line no 128 in the file contests_details_and_reminder.py by the above generated APIkey.

3.Run the code in the file contests_details_and_reminder.py.

4.The name, start time, length and phase of the recent upcoming contests on codeforces is displayed.

5.To send reminder for the above contests enter the phone number and the reminder messages will be scheduled through msg91 API. The reminder mssages will be received on the given phone number 15 minutes before the start of the contest.

6.The sceduled time and scheduled request ID for all these upcoming contests is displayed in the output.

#The service provided by msg91 is not free though initially you get 50 free credits (i.e. you can send 50 free messages)


Screenshots

This folder contains the screenshot of output, received reminder messages and delivery report of scheduled messages.


