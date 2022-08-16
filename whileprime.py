number = int(input("Enter a number :"))
i=2
while(i<=number/2 and number%i!=0):
    i+=1
if(i>number/2 and number!=1):
    print("prime")
else:
    print("not prime")
