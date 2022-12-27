a=[]
n=int(input("Enter your limit:"))

for i in range(1,n+1):
 b=int(input("Enter your elements:"))
 a.append(b)

a.sort()
print(a)
print("output the 2nd largest number:",a[n-2])
