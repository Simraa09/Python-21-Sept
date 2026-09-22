num = int(input("Enter the number: "))
rem = 0
while num!=0:
    rem = num%10
    print(rem, end="")
    num = num//10