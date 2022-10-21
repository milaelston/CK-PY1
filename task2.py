def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}
    for char in str_:
        if char.isalpha():
            dict_.update({char: 0})
    for letter in dict_.keys():
        sumoflet = str_.count(letter)
        dict_.update({letter: sumoflet})

    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# ВТОРАЯ ФУНКЦИЯ, КОТОРАЯ ВЫДАЕТ ПРОЦЕНТЫ

def percentage(dictionary):
    numlist = list(dictionary.values())
    keylist = list(dictionary.keys())
    sum_ = sum(numlist)
    newnumlist = []
    for i in numlist:
        ii = i / sum_
        newnumlist.append(ii)
    newdict = {}
    for j in range(len(keylist)):
        key = keylist[j]
        value = str(round(newnumlist[j]*100, 2)) + '%'
        newdict.update({key: value})

    return newdict


dictofmain = get_count_char(main_str)
#print(percentage(dictofmain))
