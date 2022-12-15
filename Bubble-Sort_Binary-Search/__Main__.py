import random, func

numeros = random.sample(range(10_000),1000)
if 9875 not in numeros:
    numeros.append(9875)

numeros = func.bubbleSort(numeros)
print("="*83)
print("Na Busca Linear: ")
func.buscaLinear(numeros,9875)
print("="*83)
print("Na Busca Binária: ")
func.buscaBinaria(numeros,9875)
print("="*83)
print("Com isso podemos perceber que a Busca Binária em uma lista com mil valores, consegue ser 100 vezes mais rapido, imagina se essa lista possui-se invés de mil, milhões ou bilhões de números o quanto não se economizaria utilziando da busca binária!!!")