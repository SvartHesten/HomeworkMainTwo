# Given array , padding amount and repeat count.
# Pad the array - how many elements to be taken from array edges.
# Repeat - how many times pad to be repeated.
# Also make sure that padding is no longer than array length.

pad_count = 0
repeat_count = 0
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
while pad_count <1:
    try:
        pad = int(input("Enter padding amount"))
    except ValueError:
        print("Not valid padding")
        continue
    pad_count += 1
while repeat_count < 1:
    try:
        repeat = int(input("Enter repeat"))
    except ValueError:
        print("Not valid repeat")
        continue
    repeat_count += 1
if pad > number:
    print("Beware the pad is greater than array")
else:
    front_list =init_list[:pad]
    print(front_list)
    back_list = init_list[number - pad:]
    print(back_list)
    for i in range(repeat):
        init_list.insert(0, front_list)
        init_list.append(back_list)
    print(init_list)


