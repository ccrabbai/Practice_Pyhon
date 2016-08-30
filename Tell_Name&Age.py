#Tell_Name&Age.py
name = input("Enter ur name : ")
age = int(input("Enter ur age : "))
No_Of_Times = int(input("How many times do u wanna see this message: "))
for i in range(No_Of_Times):
    if age < 100:
        New_Age = 100 - age
        print("%s will be 100 yrs old in %d years to come"%(name,New_Age))
        print("\n")


