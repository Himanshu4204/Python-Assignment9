# Q6. Write a python script to print first N natural Even Numbers ?
n=int(input("Enter how many numbers you Print :"))
a=1
while a<=n*2:
    if a%2==0:
        print(a,end=" ")
    a+=1