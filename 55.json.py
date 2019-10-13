# Use JSON (JavaScript Object Notation) In Python

"""
# Python has a built-in package called json, which can be used to work with JSON data.
    we can start use it: (import json)
# If you have a JSON string, you can parse it by using the json.loads(). Method.
    # The result will be a python dictionary.
# If you have a Python object, you can convert it into a JSON string by using the json.dumps()
    method.
# When you convert from Python to JSON, Python objects are converted into the JSON
    (JavaScript) equivalent:
        Python:                   JSON:
            dict            =>      Object
            list, tuple     =>      Array
            str             =>      String
            int,float       =>      Number
            True            =>      true
            False           =>      false
            None            =>      null
"""

import json

myJSON = '{\
            "name":"omar" ,\
            "age": 24, \
            "country": "KSA" }'

toPython = json.loads(myJSON)
print(toPython)
print(toPython["country"])

myDictionary = {"name":"omar" , "age": 24, "country": "KSA" }
toJSON = json.dumps(myDictionary)
print(toJSON)

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

toJSON = json.dumps(all)
print(toJSON)
