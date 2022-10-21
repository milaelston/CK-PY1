def delete(givenlist, index=None):
    if index is None:
        listnew = givenlist[::-1][1:][::-1]
    else:
        list1, list2 = givenlist[:index], givenlist[index+1:]
        listnew = list1 + list2

    return listnew


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
