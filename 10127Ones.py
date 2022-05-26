
p=int(input("val: "))
ones = 1
x=1;
while(x%p !=0):
    x = ((x*10)+1)%p
    ones+=1
print(ones)



