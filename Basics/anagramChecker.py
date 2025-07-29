def is_anagram(str1, str2):
    if(sorted(str1.lower()) == sorted(str2.lower())):
        return 1
    else:
        return 0


print("Input a string")
i = input()
print("Input another string")
j = input()

if(is_anagram(i, j)):
    print("The strings are anagram")
else:
    print("The strings are not anagram")
