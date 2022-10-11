list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maxnum = max(list_numbers)
idxmaxnum = list_numbers.index(maxnum)
list_numbers[idxmaxnum], list_numbers[-1] = list_numbers[-1], list_numbers[idxmaxnum]

print(list_numbers)

'''
Поскольку лабораторная работа по циклам, предлагаю более длинное решение с циклом:

currentmax = list_numbers[0]
indexofmax = 0
for num in enumerate(list_numbers):
    if num[1] > currentmax:
        currentmax = num[1]
        indexofmax = num[0]

list_numbers[indexofmax], list_numbers[-1] = list_numbers[-1], list_numbers[indexofmax]

print(list_numbers)
'''
