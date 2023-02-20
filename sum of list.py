list=[]
sum=0
limit=int(input("Enter the limit:"))
print("Enter the ",limit,"numbers:")
for i in range(limit):
    x=int(input("Enter the numbers:"))
    list.append(x)
print(list)
for i in list:
    sum=sum+i
print("Sum of list is:",sum)