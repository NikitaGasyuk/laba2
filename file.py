import random

list1 = [random.randint(-10, 10) for i in range(20)]

with open(filename, 'w') as f:
    for index in list1:
        if index**2 > 30:
            continue
        f.write(str(index) + "\n")
