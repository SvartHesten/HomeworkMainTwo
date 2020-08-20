# Given a number n.
# Print Fibonacci up to n.

def fibona(n):
    if n <= 1:
        return n
    else:
        return fibona(n - 1) + fibona(n - 2)


number_count = 0
while number_count < 1:
    try:
        number = int(input("Enter the number"))
    except ValueError:
        print("Not a valid number")
        continue
    number_count += 1
if number < 0:
    print("Should be positive")
elif number == 0:
    print(f" the Fibo is {fibona(0)}")
else:
    for i in range(0, number):
        print(f" and Fibonacci for  {i}  is equal  {fibona(i)}")

