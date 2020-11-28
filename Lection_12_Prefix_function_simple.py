# ==================================================
#
#   Lection 12.
#   Поиск значений префикс-функции для строки.
#   Наивный алгоритм.
#   asymptotics: O(N*N)
#
# ==================================================

'''
Поиск равных длин префикса и суфикса для каждого среза исходной строки,
путем прямого перебора и сравнения между собой начальных и конечных последовательностей символов
в каждом срезе с присвоением текущему элементу списка максимального значения длины суффикса, если она
оказалась равна префиксу.
'''

def naivPrefixFunction(S):
    '''
    Второстепенная часть. Подготовка списка длин префиксов с длиной списка, равной длине исходной строки
    и нулевыми значениями элементов. '''
    pi = [0] * len(S)

    '''
    Основная часть. Циклический перебор каждого среза исходной строки и последовательное сравнение
    префиксов и суффиксов каждого среза, длина которых циклически увеличивается на 1 в пределах среза,
    и присвоение элементу списка префиксов с предыдущим индексом значения длины суффикса,
    если он равен префиксу. '''
    for i in range(1,len(S)+1):
        for k in range(1, i):
            if S[0:k] == S[i - k:i]:
                pi[i-1] = k

    return pi

S1 = "ssdsdssd"
print(naivPrefixFunction(S1))