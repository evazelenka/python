# def f (x):
#     return(x*x)

# print(f(5))
# print(type(f))
# a = f
# print(a(5))

# def calc1(a,b):
#     return(a+b)

# def calc2(a, b):
#     return(a*b)

# def math(op, x, y):
#     print(op(x, y))

# # math(calc2, 5, 8)


# # calc1 = lambda a,b: a*b
# math(lambda a,b: a*b, 5, 8)


# Task1
# Из списка выбрать только четные числа и составить список пар(числож квадрат числа).

# nums2 = []
# nums = [1, 2, 3, 5, 8, 15, 23, 38]
# for i in nums:
#     if i % 2 == 0:
#         nums2.append((i, i**2))
# print(nums2)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# nums = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, nums)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x : (x, x**2), res))
# print(res)


# list_1 = [x for x in range(1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = '15 156 96 3 5 8 52 5'
# print(data)
# # data = data.split()
# # print(data)

# data = list(map(int, data.split()))
# print(data)


# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# colors = ['red', '666', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# print(56)

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Модуль OS

