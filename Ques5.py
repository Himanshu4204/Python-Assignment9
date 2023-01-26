# Q5. Write a python script to print first N odd natural number in reverse order ?
n=int(input("Enter How many numbers you print :"))
a=n*2
while a>0:
    if a%2!=0:
        print(a)
    a-=1