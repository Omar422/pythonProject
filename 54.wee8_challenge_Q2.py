# 54 . Week Eight Challenge

"""
# Using datetime module print:
    # year
    # time and date
    # month
    # day
"""
import datetime as dt

d = dt.datetime.now()
print("year: "+str(d.year))
print("now: "+str(d))
print("month: "+str(d.strftime("%B")))
print("day: "+str(dt.datetime.now().strftime("%A")))
