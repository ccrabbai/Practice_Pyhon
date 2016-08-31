num = int(input("Enter a number: "))
for i in range(1,num+1):
    if num == 1:
        print(num, "has ony one divisor which is ", num)
    elif num == 0:
        print("Number must be greater than zero")
    elif num%i == 0:
        print(i)
