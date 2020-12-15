An email server maintains a log file containing records of emails. Each record appears on a separate line.  The format of each line in this log file is as follows:

From stephen.smith@bigred.cornell.edu Saturday Jan 5th 09:30:15 2019

From ihab_fernando@kin.uwaterloo.ca Thursday April 10th 12:45:35 2018

and so on…


Implement a function emailParser(fileName) that accepts the name of a log file and retrieves a list of the email senders’ user names, e.g., [‘stephen.smith’, ‘ihab_fernando’, ‘John.ali’, ……..]. To accomplish this task, you’ll need to implement the below steps inside the emailParser(fileName) function:
- Read a line from the file by using the readline() function
- Parse the line to retrieve the user name from the email
- Append the retrieved user name from the previous step to a list
- Repeat all the three steps above for each line in the file
- Return the list of user names

Use the attached logfile.txt file for your test, if your program runs correctly, you should get the following output list:
['stephen.smith', 'ihab_fernando', 'John.ali', 'marina_fernando', 'radia.paul', 'mansour_rohany', 'stephen.smith', 'carlos_marcos', 'stephen.smith', 'ihab_fernando']

Submit your .py file (Firstname_LastnameIP4.py) to mostafa_ahmed@columbusstate.edu
