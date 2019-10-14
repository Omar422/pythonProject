# 56. Use JSON (JavaScript Object Notation) In Python p2

"""
# The json.dumps() method has parameters to make it easier to read the result with indent
# also I can define the separators, default value is (", ", ": "), which means using a comma
    and a space to separate each object, and a colon and a space to separate keys from values:
# The json.dumps() method has parameters to order the keys in the result:
# sort_keys is a parameter to specify if the result should be sorted or not (True,False)
#
"""

import json

# Python Object
all = {
    "name":"ali",
    "age" : 20,
    "married": True,
    "divorced": False,
    "chlidren":("x","y"),
    "pets": None,
    "cars":[
        {"model":"BMW", "mpg": 27.5},
        {"model":"Ford Edge", "mpg": 24.1}
    ]
}
# Use the indent parameter to define the numbers of indents
# Define the separators
# Use sort_keys
toJSON = json.dumps(all, indent = 2, separators=(";"," :: "), sort_keys=True)
print(toJSON)
