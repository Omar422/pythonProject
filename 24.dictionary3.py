# 24. Dictionaries In Python 3
"""
# dictName.copy() and dict(dictName): are use to copy a dictionary
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# It is also possible to use the dict() constructor to make a new dictionary.
    #Ex: mydict= dict(key="value").... key without "" , and (=) not (:)
"""

myd = {
    "name":"omar",
    "age": 23
}
print("'myd' dictionary items are:\n"+str(myd))
copydict = myd.copy()
print("copy the myd dictionary using .copy() and save it in a new var called 'copydict'")
print("'copydict' dictionary items are:\n"+str(copydict))
dict = dict(myd)
print("copy the myd dictionary using dict() and save it in a new var called 'dict'")
print("'copydict' dictionary items are:\n"+str(dict))

f = {
    "first":{
    "no":"one",
    },
    "second":{
    "no":"two",
    }
}
print("\nnested dictionary\n"+str(f))

#print("Create a new dictionary using dict")
#newdict = dict(a="A",b="B")
#print(newdict)
