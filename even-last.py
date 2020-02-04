from operator import itemgetter
#Soma todos os numeros de casas pares(0 incluso) e depois multiplica pelo ultimo numero

def checkio(array):
    indice = 0
    lista = []
    if len(array)==1:
        return array[0]**2
    if len(array)==0:
        return 0
    else:
        while 2 * indice < len(array):
            lista.append(2 * indice)
            indice += 1
        return (sum(itemgetter(*lista)(array)) * array[~0])

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
best-solution
def checkio(array):
      
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]
"""
