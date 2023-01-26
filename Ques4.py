# Q4. write a python script to print first N odd natural Numbers?
n=int(input("Enter how many numbers you print :"))
a=1
while a<=2*n:
    if a%2!=0:
        print(a,end=' ')
    a+=1