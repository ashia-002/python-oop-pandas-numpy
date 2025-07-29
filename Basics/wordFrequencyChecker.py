from collections import Counter
import re

def frequency_check(str):
    word = re.findall(r'\w+', str.lower())
    return Counter(word).most_common(3)

print("Enter a line: ")
i = input()
print(frequency_check(i))