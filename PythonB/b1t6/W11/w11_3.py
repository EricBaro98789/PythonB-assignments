#code segment 1
x = 10
y = 20

if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15.")

#code segment 2
score = 85

if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        grade = "C"

print(f"Grade: {grade}")

#code segment 3
user_logged_in = True
has_permission = True

if user_logged_in:
    if has_permission:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("Please log in first.")

