# 60 . Week Challenge Q1

"""
# Make A Tuple With Days Of The Week, Then Converted To String Using JSON
"""

import json as js

Days = ('Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri')
print('tuple:\n'+str(Days))
toJSON = js.dumps(Days)
print('json\n'+str(toJSON))
