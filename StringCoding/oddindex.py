
z=input("enter your string:")

def modify(z):
 final=""
 for i in range(len(z)):
  if(i%2==0):
   final=final+z[i]
 return final

print("your modified string is:")
print(modify(z))