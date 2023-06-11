def progression(a1,d,n):
    list_1 = []
    for i in range(0, n):
      list_1.append(a1)
      a1 += d
    return list_1




def Index(min, max):
    import random
    List_1=[random.randint(0, 10) for i in range(0, 10)]
    print(List_1)
    result = []
    for i in range(len(List_1)):
        if max >= List_1[i] >= min:
            result.append(i)
    return result