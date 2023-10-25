# import random
#
# array = []
# for i in range(1000):
#     array.append(random.randint(1, 1000000))
#
# for i in range(len(array) - 1, 0, -1):
#     for j in range(i):
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]
#
# print(array)
#
#
import random

array = []
for i in range(100000):
    array.append(random.randint(1, 10000))

for i in range(len(array) - 1, 0, -1):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

#
# import random
#
# array = []
# for i in range(1000000):
#     array.append(random.randint(1, 100000))
#
# for i in range(len(array) - 1, 0, -1):
#     for j in range(i):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)