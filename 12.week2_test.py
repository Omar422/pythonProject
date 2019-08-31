#11. Week 2 Test

a = "Please, I want {} sandwishes and {} donutes"
b, c = 5, 7
print("The main text is: "+a+"")
a = a.replace("I","we")
a = a.format(b,c)
a = "After Editing => " + a.replace("a","A")
print(a)
