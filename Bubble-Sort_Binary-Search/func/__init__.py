def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                aux = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = aux
    return lst


def buscaLinear(lst,num):
    n = len(lst)
    cont = 0
    for i in range(0,n-1):
        cont += 1
        if lst[i] == num:
            return print(f"O número {num} foi encontrado na posição {i} e foi utilizado ao todo {cont} comprações")
    return print(f"Foi realizado um total de {cont} comprações e não foi encontrado o número {num} nela")


def buscaBinaria(lst,num):
    inicio = cont = 0
    fim = len(lst)
    while inicio <= fim:
        cont += 1
        metade = (inicio+fim) // 2
        if num == lst[metade]:
            return print(f"O número {num} foi encontrado na posição {metade} e foi utilizado ao todo {cont} comprações")
        if num > lst[metade]:
            inicio = metade+1
        elif num < lst[metade]:
            fim = metade-1
    return print(f"Foi realizado um total de {cont} comparações e não foi encontrado o número {num}")