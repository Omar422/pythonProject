# 26. Week four challenge - QUESTION NO.2
"""
# Create a dictionary with this data {"name":"pigeon", "type":"bird", "skinCover":"feathers"}
# Print the value of type key
# Change the value of type skinCover
"""
print("Week 4 Challenge - Second Question")

mydict = {
    "name"      :  "pigeon",
    "type"      :  "bird",
    "skinCover" :  "feathers"
}
print("\nThe main items in the dictionary are:\n"+str(mydict))

typeVal = mydict["type"]
print("\nThe value of key 'type' using [\"type\"] is:\n"+str(typeVal))

mydict["skinCover"] = "not feathers"
print("\nThe value of key 'skinCover' after change it is:\n"+str(mydict["skinCover"]))

print("\nThe items in the dictionary are:\n"+str(mydict))
