# Week four challenge - QUESTION NO.1
"""
# add (4,8,12) to this set -> set={1,3,5,7,8}
# delete 8 from the set.
# empty the set.
"""
print("Week 4 Challenge - First Question")

set={1,3,5,7,8}
print("\nThe main set's items are:\n"+str(set))

set.add(4)
set.update([8,12])
print("\nAdding 4,8,12 to the set using add() and update([])\n"+str(set))

set.discard(8)
print("\nRemove 8 form the set using discard()\n"+str(set))


set.clear()
print("\nEmpty the set using clear()\n"+str(set))
