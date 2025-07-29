thislist = ['my', 'cat', 'shiro', 'is', 'not'];
thislist.sort()
print(thislist)

numList = [45, 32, 89, 21, 14]
numList.sort()
print(numList)

numList.sort(reverse=True)#to sort in descending order 
print(numList)

#You can also customize your own function by using 
# the keyword argument #?key = function

def myFunc(n):
    return abs(n - 50)

thisnumList = [100, 50, 45, 67, 48]
thisnumList.sort(key=myFunc)
print(thisnumList)

charlist = ["banana", "Orange", "Kiwi", "cherry"]
charlist.sort()
print(charlist)

charlist.sort(key=str.lower)
print(charlist)

charlist.reverse()
print(charlist)