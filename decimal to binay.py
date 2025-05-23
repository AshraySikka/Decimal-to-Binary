num=int(input("Enter a number: "))
bin=''
while num>0:
    r=num%2
    num=num//2
    bin=str(r)+bin

print('Binary for this number is: ',bin)
