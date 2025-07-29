setthis = {'apple', 'mango', 'orange', 'apple'}
print(setthis)#will only print one apple

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(len(set3))

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)#wil print True as is present in the set
print("banana" not in thisset)#will print False

thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.

tropical = {"pine", "coconut", "papaya"}
thisset.update(tropical)
print(thisset)