from dumps import dumps as dmp
from fixtures import fixtures as fx


def myQuickSort(Arr, low, high):
    base = high
    if low < high:
        base = (Arr[low] + Arr[(low + high) // 2] + Arr[high]) // 3
        (Arr, sep) = partition(Arr, base, low, high)
        if sep > low:
            myQuickSort(Arr, low, sep - 1)
            myQuickSort(Arr, sep, high)
    return (Arr, base)


def partition(Arr, base, low, high):
    i = low
    j = high
    sep = high
    while i <= j:
        if Arr[i] > Arr[j]:
            Arr[i], Arr[j] = Arr[j], Arr[i]
        if Arr[i] <= base:
            i = i + 1
        if Arr[j] > base:
            sep = j
            j = j - 1
    return (Arr, sep)

#####################################################################

# Arr = [28, 9, 7, 5, 65, 3, 2, 4, 6, 7, 15, 8, 8, 24, 5, 6, 67, 45, 23, 7, 28, 1, 45, 98, 6, 65, 45, 23, 12]
# Arr = [1, 9, 2, 8, 4, 7, 5, 6, 3, 10]

# Arr = [-1, 9, -2, 8, -4, 7, -5, 6, 3, -10, 0, 10, 3, 2]

# Arr = [100, 11, 19, 82, 48, 83, 37, 54, 26, 75]
# Arr = [7, 7, 7, 3, 3, 3, 9, 9, 9, 9, 4, 4, 4]
# Arr = ['a', 'd', 'c', 'b']
# Arr = [7, 7, 3, 3, 9, 4]
# Arr = [6, 2, 7, 0, 3]
# sep = partition(Arr, base, low, high)
# low = 0
# high = len(Arr) - 1
# base = (Arr[low] + Arr[high // 2] + Arr[high]) // 3
# print(' base = ', base)
# print(Arr, '\n')
#
#
# print(' массив ПОСЛЕ partition Arr = ', Arr, '\n')
#
#
# # myQuickSort(Arr, low, high)
# print(myQuickSort(Arr, low, high))

################################################################

# def myQuickSort(listOriginal):
#     if listOriginal == dmp.dumpEtalon():
#         return fx.fixtureEtalon()[1]
#
#     if listOriginal == dmp.dumpShuffle():
#         return fx.fixtureAlmostShuffle()[0]
#
#     if listOriginal == dmp.dumpEmpty():
#         return fx.fixtureEmpty()[1]
#
#     if listOriginal == dmp.dumpSingle():
#         return fx.fixtureSingle()[1]
#
#     if listOriginal == dmp.dumpNegative():
#         return fx.fixtureNegative()[1]
#
#     if listOriginal == dmp.dumpNegativePositive():
#         return fx.fixtureNegativePositive()[1]
#
#     if listOriginal == dmp.dumpLetters():
#         return fx.fixtureLetters()[1]
#
#     if listOriginal == dmp.dumpFloat():
#         return fx.fixtureFloat()[1]
#
#     if listOriginal == dmp.dumpBackDirection():
#         return fx.fixtureBackDirection()[1]
#
#     if listOriginal == dmp.dumpAlmostShuffle():
#         return fx.fixtureAlmostShuffle()[1]
#

########################################################################


##########################################################################
