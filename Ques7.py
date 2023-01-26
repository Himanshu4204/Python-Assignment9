# Q7. Write a python script to print first N Even Natural Numbers in Reverse Order ?
n=int(input("Enter How many number you print :"))
a=n*2
while a>0:
    if a%2==0:
        print(a,end=' ')
    a-=1