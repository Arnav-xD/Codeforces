str1 = input()
s = set()
for i in str1: 
    s.add(i)

if len(s) % 2 ==0: 
    print("CHAT WITH HER!")
else: 
    print("IGNORE HIM!")
    