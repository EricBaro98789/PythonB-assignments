# Check if a list has any negative numbers and if so, flag it
n = [3, 5, -1, 7, -2, 8]
flag = False
for num in n:
    if num < 0:
        flag = True
        break

# Print whether the list has negative numbers
if flag == True:
    print("List contains negative numbers.")
else:
    print("List does not contain negative numbers.")

# Finding and printing all even numbers from the list
even_numbers = []
for number in n:
    if number % 2 == 0:
        even_numbers.append(number)
print("Even numbers:", even_numbers)

# Variable names and magic number
a = 20  # This represents the threshold
b = len(even_numbers)
if b > a:
    print("More than threshold")
else:
    print("Not more than threshold")
