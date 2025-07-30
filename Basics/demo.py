from collections import Counter
#print("Hello, world")
"""
THis is a multi
line comment.
using three double quote.
"""
#? for loop
myList = ['apple', 'orange', 'mango']
for x in myList:
    print(x)

#? printing through the index
print("Print through the index")
myList = ["a", 'b', 'c']
for i in range(len(myList)):
    print(myList[i])

#? using while loop
print("print using while loop")
i = 0
while i < len(myList):
    print(myList[i])
    i += 1

#? looping using list comprehension
print("using list comprehension")
[print(x) for x in myList]

#? we are taking the elements containing 'a' and putting it to a new list and printing that list
from collections import Counter
fruits = ["apple","apple", "banana", "cherry", "kiwi", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

for i in newlist:
    print(i)

frut_count = Counter(fruits)
print(frut_count)
print(frut_count['apple'])