# import random
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
# def siftDown(arr, i, upper):
#     while True:
#         left = 2 * i + 1
#         right = 2 * i + 2
#         largest = i
#
#         if left < upper and arr[left] > arr[largest]:
#             largest = left
#
#         if right < upper and arr[right] > arr[largest]:
#             largest = right
#
#         if largest == i:
#             break
#
#         swap(arr, i, largest)
#         i = largest
#
# def heapSort(arr):
#     for i in range((len(arr) // 2) - 1, -1, -1):
#         siftDown(arr, i, len(arr))
#
#     for end in range(len(arr) - 1, 0, -1):
#         swap(arr, 0, end)
#         siftDown(arr, 0, end)
#
# random_numbers = [random.randint(1, 1000) for i in range(1000)]
#
# heapSort(random_numbers)
#
# print(random_numbers)
#
#
# import random
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
# def siftDown(arr, i, upper):
#     while True:
#         left = 2 * i + 1
#         right = 2 * i + 2
#         largest = i
#
#         if left < upper and arr[left] > arr[largest]:
#             largest = left
#
#         if right < upper and arr[right] > arr[largest]:
#             largest = right
#
#         if largest == i:
#             break
#
#         swap(arr, i, largest)
#         i = largest
#
# def heapSort(arr):
#     for i in range((len(arr) // 2) - 1, -1, -1):
#         siftDown(arr, i, len(arr))
#
#     for end in range(len(arr) - 1, 0, -1):
#         swap(arr, 0, end)
#         siftDown(arr, 0, end)
#
# random_numbers = [random.randint(1, 100000) for i in range(10000)]
#
# heapSort(random_numbers)
#
# print(random_numbers)
#
#
# import random
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
# def siftDown(arr, i, upper):
#     while True:
#         left = 2 * i + 1
#         right = 2 * i + 2
#         largest = i
#
#         if left < upper and arr[left] > arr[largest]:
#             largest = left
#
#         if right < upper and arr[right] > arr[largest]:
#             largest = right
#
#         if largest == i:
#             break
#
#         swap(arr, i, largest)
#         i = largest
#
# def heapSort(arr):
#     for i in range((len(arr) // 2) - 1, -1, -1):
#         siftDown(arr, i, len(arr))
#
#     for end in range(len(arr) - 1, 0, -1):
#         swap(arr, 0, end)
#         siftDown(arr, 0, end)
#
# random_numbers = [random.randint(1, 1000000) for i in range(10000)]
#
# heapSort(random_numbers)
#
# print(random_numbers)