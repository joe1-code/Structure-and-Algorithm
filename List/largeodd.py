a=[]
n=int(input("Enter the number of elements:"))

for i in range(0,n):
 c=int(input("Enter the elements:"))
 a.append(c)

#create the variables for even and odd
even=[]
odd=[]

for i in a:
 if(i%2==0):
  even.append(i)
 else:
  odd.append(i)

even.sort()
odd.sort()
print(even)
print(odd)
#initialize the variables 
count1=0
count2=0

for k in even:
 count1=count1+1
for j in odd:
 count2=count2+1

#output the largest even and odd elements.
print("The largest odd element:",odd[count2-1])
print("The largest even element:",even[count1-1])