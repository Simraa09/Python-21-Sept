num = int(input("Enter the number: "))
len = 0
while num!=0:
    num//=10
    len+=1
print(len)