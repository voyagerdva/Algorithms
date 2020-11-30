from merge import merge as mrg


def splitIntoTwoSortedList(originalList):
    left = originalList[:len(originalList) // 2]
    firstList = mergeSort(left)

    right = originalList[len(originalList) // 2:]
    secondList = mergeSort(right)
    return (firstList, secondList)


def mergeSort(originalList):
    if len(originalList) < 2:
        return originalList

    (firstList, secondList) = splitIntoTwoSortedList(originalList)

    resultList = mrg.merge(firstList, secondList)

    return resultList