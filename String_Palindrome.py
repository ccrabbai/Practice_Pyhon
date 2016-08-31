#Exercise 6
#String palindrome

letter = input("Enter a string: ")
size = len(letter)
for i in range(0,size):
    if letter[i] == letter[size -(i+1)]:
        i += 1
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

