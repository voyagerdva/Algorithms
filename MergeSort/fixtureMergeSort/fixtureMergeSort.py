def fixtureMakeListEtalonDirect10Elements():
    ListEtalonDirect10Elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (ListEtalonDirect10Elements, ListEtalonDirect10Elements)


def fixtureMakeListShuffle10Elements():
    ListShuffle10Elements = [1, 9, 2, 8, 4, 7, 5, 6, 3, 10]
    ListEtalonDirect10Elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (ListShuffle10Elements, ListEtalonDirect10Elements)


def fixtureMakeListShuffleInRange100():
    ListShuffleInRange100 = [100, 11, 19, 82, 48, 83, 37, 54, 26, 75]
    listEtalonShuffleInRange100 = [11, 19, 26, 37, 48, 54, 75, 82, 83, 100]
    return (ListShuffleInRange100, listEtalonShuffleInRange100)


def fixtureMakeListSeveralSequencesOf7394():
    ListShuffleSeveralsequencesOf7394 = [7, 7, 7, 3, 3, 3, 9, 9, 9, 9, 4, 4, 4]
    listEtalonSeveralsequencesOf7394 = [3, 3, 3, 4, 4, 4, 7, 7, 7, 9, 9, 9, 9]
    return (ListShuffleSeveralsequencesOf7394, listEtalonSeveralsequencesOf7394)


def fixtureMakeListEmpty():
    listEmpty = []
    listEtalonEmpty = []
    return (listEmpty, listEtalonEmpty)


def fixtureMakeListSingle():
    listSingle = [8]
    listEtalonSingle = [8]
    return (listSingle, listEtalonSingle)


def fixtureMakeListNegativeDigitals():
    listShuffleNegativeDigitals = [-1, -9, -2, -8, -4, -7, -5, -6, -3, -10]
    listEtalonNegativeDigitals = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    return (listShuffleNegativeDigitals, listEtalonNegativeDigitals)


def fixtureMakeListNegativeAndPositiveDigitals():
    listShuffleNegativeAndPositiveDigitals = [-1, 9, -2, 8, -4, 7, -5, 6, 3, -10, 0, 10, 3, 2]
    listEtalonNegativeAndPositiveDigitals = [-10, -5, -4, -2, -1, 0, 2, 3, 3, 6, 7, 8, 9, 10]
    return (listShuffleNegativeAndPositiveDigitals, listEtalonNegativeAndPositiveDigitals)


def fixtureMakeListLetters():
    listShuffleLetters = ['a', 'c', 'e', 'b', 'd', 'z', 'y', 'x']
    listEtalonLetters = ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
    return (listShuffleLetters, listEtalonLetters)


def fixtureMakeListFloatDigitals():
    listShuffleFloatFloatDigitals = [1.12, 8.0002, 9.32, 2.0, 8.0001, 4.232, 7.0, 5.123456789, 5.123456788, 6.0, 3.0, 10.0]
    listEtalonFloatDigitals = [1.12, 2.0, 3.0, 4.232, 5.123456788, 5.123456789, 6.0, 7.0, 8.0001, 8.0002, 9.32, 10.0]
    return (listShuffleFloatFloatDigitals, listEtalonFloatDigitals)


def fixtureMakeListBackDirectionfromTENtoONE():
    listShuffleBackDirectionfromTENtoONE = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    listEtalonBackDirectionfromTENtoONE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (listShuffleBackDirectionfromTENtoONE, listEtalonBackDirectionfromTENtoONE)


def fixtureMakeListAlmostShuffle10Elements():
    listAlmostShuffle10Elements = [1, 2, 8, 4, 5, 6, 7, 3, 9, 10]
    listEtalon10Elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (listAlmostShuffle10Elements, listEtalon10Elements)


def fixtureMakeListShuffle30Elements():
    listShuffle30Elements = [28, 9, 7, 5, 65, 3, 2, 4, 6, 7, 15, 8, 8, 24, 100, 5, 6, 67, 45, 25, 7, 28, 1, 45, 98, 6, 65, 45, 23, 12]
    listEtalon30Elements = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 12, 15, 23, 24, 25, 28, 28, 45, 45, 45, 65, 65, 67, 98, 100]
    return (listShuffle30Elements, listEtalon30Elements)
