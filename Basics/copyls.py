thisList = ['apple', 'banana', 'cherry']
myList = thisList.copy()
print(myList)

listn = list(thisList)
print(listn)

#Use Slice Operator
listc = thisList[:]
print(listc)

print(type(thisList))

x = 10
print(type(x))

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
tropical = ['pneapple', 'pomigranate']
print(thisList)
#thisList[2] = "strawberry"
thisList.insert(2, 'strawberry')
thisList.append('Berry')
thisList.append('banana')
thisList.extend(tropical) #?this appends the list to the list it extends
#? can extend list, tuple, dictionaries
print(thisList)
thisList.remove('banana')
thisList.pop(5)
thisList.clear()
print(thisList)

thisList[1:3] = ["mango", 'berry']
print(thisList)

print(4+7+3j)
