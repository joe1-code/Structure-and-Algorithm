a=[]
n=int(input("Enter number of elements:"))

for i in range(1,n+1):
  b=int(input("Enter your Elements:"))
  a.append(b)

a.sort()
print(a)
print("The largest number is:",a[n-1])