# def sum_numbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum+= i
#     return sum

# print(sum_numbers(5))

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res+= i
#     return res
# print(sum_str('q', 'e', 'l'))

# import modul 

# print(modul.max1(5,9))

# from modul import *
# print(max1(9,5))

# import modul as m1
# print(m1.max1(8,2))


# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list1 = []
# for i in range (1,10):
#     list1.append(fib(i))
# print(list1)

# Быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         piver =array[0]
#     less = [i for i in array[1:] if i <= piver]
#     greater = [i for i in array[1:] if i > piver]
#     return quick_sort(less) + [piver] + quick_sort(greater)

# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# Сортировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#            nums[k] = left[i]
#            i +=1
#            k += 1
#         while j < len(right):
#            nums[k] = right[j]
#            j +=1
#            k += 1


list1 = [1,5,6,9,8,7,2,1,55,2,4]
print(len(list1))
# merge_sort(list1)
# print(list1)
            
