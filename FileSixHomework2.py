# given array of numbers
# Find index of second maximum element.

element_count = 0
number_count = 0
init_list = []
while number_count <1:
    try:
        number = int(input("Enter number of elements in array"))
    except ValueError:
        print(" Number of elements integer!!!")
        continue
    number_count += 1
while element_count < number:
    try:
        element = int(input(" Enter current number"))
    except ValueError:
        print("Not a valid number")
        continue
    element_count += 1
    init_list.append(element)
print(init_list)
new_list = sorted(init_list)
print(new_list)
for i in range(number):
    if new_list[number - 2] == init_list[i]:
        print(f" and the index of second largest element is  {i}")

