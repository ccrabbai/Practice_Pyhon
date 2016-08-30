#List_Less_Than_ten.py
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
New_List = []
for i in a:
    if i < 5:
        New_List.append(i)
print(New_List)

#Ask the user for a number and return a 
#list that contains only elements from the original
#list a that are smaller than that number given by the user.
num = int(input("Enter any number: "))
print([i for i in a if i < num ])
