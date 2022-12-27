from string import ascii_lowercase as asc_lower

def check(s):
 return set(asc_lower) - set(s.lower()) == set([])
names=input("Enter a string: ")
if(check(names)==True):
 print("The string is pangram")
else:
 print("The string is not pangram")