# Insert a number.
# Depending whether the number is prime or not
# print yes or no

division_count = 0
valid_number_count = 0
while valid_number_count < 1:
    try:
        number = int(input("Enter the number"))
    except ValueError:
        print("Not a valid number, reenter")
        continue
    valid_number_count += 1
for i in range(2, number):
    if number % i == 0:
        division_count += 1
if number <= 2:
    print(" Yes")
elif division_count == 0:
    print("Yes, it is a prime number")
else:
    print("No, not a prime")