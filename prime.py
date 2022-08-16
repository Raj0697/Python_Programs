number = int(input("Enter a number :"))
if number ==1:
    prime = False
elif number ==2:
    prime = True
else:
    prime = True
    for check_number in range(2,int(number/2)+1):
        if number%check_number==0:
            prime=False
            break
print(prime)
