i = int(input("Enter current year:"))
n = int(input("Enter year limit/ final year:"))
if i < n :
    print("Here is the list of leap years between"+str(i)+"and"+str(n)+":")
    while i <= n:
        if(i%4==0) and (i%100!=0):
            print(i)
        if(i%100==0) and (i%400==0):
            print(i)
        i+=1
else:
    print("wrong input")