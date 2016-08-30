#Even_Or_Odd_Number.py


Num = int(input("Enter a number: "))
if Num%2 == 0:
    print("%d is an even number"%Num)
else:
    print("%d is an odd number"%Num)
if Num%2 == 0 and Num%4 == 0:
    print("and also a mutiple of 4")
else:
    print("and it is a not a multiple of 4 ")

num = int(input("\nCheck if a is divisible by b\nEnter a: "))
check = int(input("Enter b: "))
try:
    if num%check==0:
        print("%d is divisible by %d"%(num,check))
    else:
        print("%d is not divisible by %d"%(num,check))
except ZeroDivisionError:
    print ("b won't be zero")
