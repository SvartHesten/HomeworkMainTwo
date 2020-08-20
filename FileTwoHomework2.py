# Given a number n >= 0.
# print n-th Fibonacci number.
# a(n) = a(n-1) + a(n-2)

def fibo_fn(n):
    if n <= 1:
        return n
    else:
        return(fibo_fn(n - 1) + fibo_fn(n - 2))


number_count = 0
while number_count < 1:
    try:
        number = int(input("Enter the number"))
    except ValueError:
        print("Not a valid number")
        continue
    number_count += 1
if number < 0:
    print(" It should not be negative")
else:
    print(f" The Fibonacci for {number}  equal to {fibo_fn(number)}")