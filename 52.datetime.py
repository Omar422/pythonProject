# 52. Date and Time

"""
# A date in Python is not a data type of its own, but we can import a module
    named datetime to work with dates as date objects.
# To create a date, we can use the datetime() class (constructor) of the datetime module.
    The datetime() class requires three parameters to create a date: year, month, day
# The datetime() class also takes parameters for time and timezone (hour, minute, second,
    microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone)
# The datetime object has a method for formatting date objects into readable strings.
    The method is called strftime(), and takes one parameter, format, to specify the format the returned string.
"""

import datetime as dt
d = dt.datetime.now()
print("now(): "+str(d))
print("datetime constructor: "+str(dt.datetime(2019,10,11)))
print("strftime(\"%A\"): "+str(d.strftime("%A")))
print("strftime(\"%B\"): "+str(d.strftime("%B")))
print(".year method: "+str(d.year))
