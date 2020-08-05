"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.
This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# n = len(sys.argv)


# date = input("Enter a date (Month Year): ");

# print(len(date.split(" ")));

# if len(date.split(" ")) == 2:
#     print(calendar.month(int(date.split(" ")[1]), int(date.split(" ")[0])));
# elif date.split(" ")[0].isnumeric() and len(date.split(" ")) == 1:
#     print(calendar.month(datetime.today().year, int(date.split(" ")[0])));
# else:
#     print("You need to enter a: [month] and/or [month] [year]!");

# Puts today's date on the today variable
today = datetime.now()
# print(datetime.now())

def new_calendar():
    # Month/year are initially assigned to today's, to be replaced with user input
    # If user doesn't input something, it will display today's value for that input
    def create_calender(month=today.month, year=today.year):
        # Use the global keyword to use the calendar input inside of this function
        global calendar
        # .prmonth - Print a month's calendar
        calendar.prmonth(year, month)

    # If there are 3 system arguments (file, month, year):
    # Configure month and year to user's input
    if(len(sys.argv) == 3):
        create_calender(int(sys.argv[1]), int(sys.argv[2]))
    # Else if there are 2 system arguments (file, month):
    # Configure month to user's input and default to current year
    elif(len(sys.argv) == 2):
        create_calender(int(sys.argv[1]))
    # Else if there is only 1 system argument (file):
    # Default to current month and year
    else:
        # create_calender()
        print('wrong usage cal.py [month] [year]')
        sys.exit(1)


new_calendar()