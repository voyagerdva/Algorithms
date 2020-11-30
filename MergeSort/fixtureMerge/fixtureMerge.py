def fixtureMakeTwoSortedLists7And4SizeAndOneMergedList():
    listA7Elements = [2, 4, 4, 7, 8, 8, 9]
    listB4Elements = [5, 6, 6, 8]
    listEtalon = [2, 4, 4, 5, 6, 6, 7, 8, 8, 8, 9]
    return (listA7Elements, listB4Elements, listEtalon)


def fixtureMakeOneSortedList4SizeOneEmptyListAndOneMergedList():
    listA4Elements = [5, 6, 6, 8]
    listBEmpty = []
    listEtalon = [5, 6, 6, 8]
    return (listA4Elements, listBEmpty, listEtalon)


def fixtureMakeOneEmptyListOneSortedList4SizeAndOneMergedList():
    listAEmpty = []
    listB4Elements = [5, 6, 6, 8]
    listEtalon = [5, 6, 6, 8]
    return (listAEmpty, listB4Elements, listEtalon)


def fixtureMakeTwoEmptyListsAndOneEmptyListForEtalon():
    listAEmpty = []
    listBEmpty = []
    listEtalon = []
    return (listAEmpty, listBEmpty, listEtalon)
