# Given three numbers a, b and num
# Create an array of evenly spaced numbers
# with the length of "num"  and
# over interval of a to b

our_array = []
a_count = 0
b_count = 0
num_count = 0
while a_count < 1:
    try:
        a = int(input("Enter the value a"))
    except ValueError:
        print("Not a valid number")
        continue
    a_count += 1
while b_count < 1:
    try:
        b = int(input("Enter the value b"))
    except ValueError:
        print("Not a valid number")
        continue
    b_count += 1
while num_count < 1:
    try:
        num = int(input("Enter the value num"))
    except ValueError:
        print("Not a valid number")
        continue
    num_count += 1
if a < b:
    element = a
    our_array.append(element)
    while len(our_array) < num:
        element += (b - a) / (num - 1)
        our_array.append(element)
    print(our_array)
elif b < a:
    element = b
    our_array.append(element)
    while len(our_array) < num:
        element += (a - b) / (num - 1)
        our_array.append(element)
    print(our_array)
else:
    print(" this makes no sense, there is no interval")




