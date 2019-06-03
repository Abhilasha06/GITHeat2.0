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

Run the code in the file user_details.py. 
Enter the codeforces handle.
The code gives the users’ details as output.

Subtask 2 (upcoming contest details and reminder)


Set up an account on msg91 and generate the APIkey.
Replace ############### in line no 127 in the file contests_details_and_reminder.py by the above generated APIkey.
Run the code in the file contests_details_and_reminder.py.
The name, start time, length and phase of the recent upcoming contests on codeforces is displayed.
To send reminder for the above contests enter the phone number and the reminder messages will be scheduled through msg91 API. The reminder mssages will be received on the given phone number 15 minutes before the start of the contest.
The sceduled time and scheduled request ID for all these upcoming contests is displayed in the output.

#The service provided by msg91 is not free though initially you get 50 free credits (i.e. you can send 50 free messages)

Screenshots

This folder contains the screenshot of output, received reminder messages and delivery report of scheduled messages.


