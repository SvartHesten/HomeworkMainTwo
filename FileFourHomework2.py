# Insert a number.
# calculate product and sum of the digits.
# If product is divisible by sum print the quotient.
# If not print remainder.

product = 1
summa = 0
number_count = 0
while number_count < 1:
    number_str = input("Enter the number")
    try:
        number = int(number_str)
    except ValueError:
        print("Not a valid number")
        continue
    number_count += 1
if len(number_str) == 1:
    product *= number
    summa += number
else:
    for i in range(len(number_str)):
        product *= int(number_str[i])
        summa += int(number_str[i])
try:
    if product % summa == 0:
        print(f"the quotient is  {product / summa}")
    else:
        print(f" the remainder is  {product % summa}")
except ZeroDivisionError:
    print("ну куда на хуй, деление на ноль........")
