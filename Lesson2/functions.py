# list1 = []
# list2 = list()
# list3 = [1, 2, 3, 8]

# print(list3[-1])

# list1 = []
# print(list1)
# for i in range(5):
#     list1.append(i)
#     print(list1)

# list1 = [12, 7, -1, 21, 0]
# print(list1)
# print(list1.pop(0))
# print(list1)
# print(list1.pop(0))
# print(list1)
# print(list1.pop(0))

# list1 = [12, 7, -1, 21, 0]
# print(list1)
# print(list1.insert(2,11))
# print(list1)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list1[:])
# print(list1[:2])
# print(list1[len(list1)-2:])
# print(list1[2:9])
# print(list1[6:-18])
# print(list1[0:len(list1):6])
# print(list1[::6])

# t = ()
# print(type(t))

# t = (1, )
# print(type(t))

# v =[1,3,6]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v

# print(a,b,c)

# t = [1,2,3,6]
# t[0] = 2

# d = {}
# d = dict()

# d['w'] = 'werty'
# d['q'] = 'querty'
# print(d[])


# dictionary = {}
# dictionary = {'up': '|', 'left': '<-', 'down': '_', 'right': '->'}
# # print(dictionary)
# # print(dictionary['left'])
# dictionary['spb'] = 52
# # print(dictionary)
# print(dictionary['spb'])
# del dictionary['left']
# print(dictionary)

# # for item in dictionary:
# #     print('{}: {}'.format(item, dictionary[item]))
# print(dictionary.items())
# for (k, v) in dictionary.items():
#     print(k, v)



# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)


# Задача: создать список, состоящий из четных чисел в диапазоне от 1 до 100

# list1 = []
# for i in range(1, 101):
#     list1.append(i)
# print(list1)

# OR

list2 = [i for i in range(1,101) if i % 2 == 0]
print(list2)