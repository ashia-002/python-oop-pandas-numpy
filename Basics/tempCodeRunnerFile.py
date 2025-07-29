from collections import Counter
fruits = ["apple","apple", "banana", "cherry", "kiwi", "mango"]
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