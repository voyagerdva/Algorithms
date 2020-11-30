from dumps import dumps as dmp


# .....................................................................#

def fixturePartShuffleReady():
    listPartShuffleReady = [3, 0, 2, 7, 6]
    listPartShuffleEtalon = [3, 0, 2, 7, 6]
    base = 5
    sep = 3
    low = 0
    high = len(listPartShuffleReady) - 1
    return (listPartShuffleReady, listPartShuffleEtalon, base, sep, low, high)


def fixturePartShuffle():
    listPartShuffle = [6, 2, 7, 0, 3]
    listPartShuffleEtalon = [3, 0, 2, 7, 6]
    base = 5
    sep = 3
    low = 0
    high = len(listPartShuffle) - 1
    return (listPartShuffle, listPartShuffleEtalon, base, sep, low, high)


# .....................................................................#

def fixtureEtalon():
    listEtalon = dmp.dumpEtalon()
    return (listEtalon, listEtalon)


def fixtureShuffle():
    listShuffle = dmp.dumpShuffle()
    listEtalon = dmp.dumpEtalon()
    return (listShuffle, listEtalon)


def fixtureShuffle_100():
    listShuffle = [100, 11, 19, 82, 48, 83, 37, 54, 26, 75]
    listEtalon = [11, 19, 26, 37, 48, 54, 75, 82, 83, 100]
    return (listShuffle, listEtalon)

def fixture333777444999():
    listShuffle = [7, 7, 7, 3, 3, 3, 9, 9, 9, 9, 4, 4, 4]
    listEtalon = [3, 3, 3, 4, 4, 4, 7, 7, 7, 9, 9, 9, 9]
    return (listShuffle, listEtalon)

def fixtureEmpty():
    listEmpty = dmp.dumpEmpty()
    listEtalon = []
    return (listEmpty, listEtalon)


def fixtureSingle():
    listSingle = dmp.dumpSingle()
    listEtalon = [8]
    return (listSingle, listEtalon)


def fixtureNegative():
    listNegative = dmp.dumpNegative()
    listEtalon = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    return (listNegative, listEtalon)


def fixtureNegativePositive():
    listNegativePositive = dmp.dumpNegativePositive()
    listEtalon = [-10, -5, -4, -2, -1, 0, 2, 3, 3, 6, 7, 8, 9, 10]
    return (listNegativePositive, listEtalon)


def fixtureLetters():
    listLetters = dmp.dumpLetters()
    listEtalon = ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
    return (listLetters, listEtalon)


def fixtureFloat():
    listFloat = dmp.dumpFloat()
    listEtalon = [1.12, 2.0, 3.0, 4.232, 5.123456788, 5.123456789, 6.0, 7.0, 8.0001, 8.0002, 9.32, 10.0]
    return (listFloat, listEtalon)


def fixtureBackDirection():
    listBackDirection = dmp.dumpBackDirection()
    listEtalon = dmp.dumpEtalon()
    return (listBackDirection, listEtalon)


def fixtureAlmostShuffle():
    listAlmostShuffle = dmp.dumpAlmostShuffle()
    listEtalon = dmp.dumpEtalon()
    return (listAlmostShuffle, listEtalon)


def fixtureBigShuffle():
    listBigShuffle = [28, 9, 7, 5, 65, 3, 2, 4, 6, 7, 15, 8, 8, 24, 5, 6, 67, 45, 25, 7, 28, 1, 45, 98, 6, 65, 45, 23,
                      12]
    listEtalon = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 12, 15, 23, 24, 25, 28, 28, 45, 45, 45, 65, 65, 67, 98]
    return (listBigShuffle, listEtalon)


def fixtureBigShuffle_25():
    listBigShuffle_25 = [28, 9, 7, 5, 65, 3, 2, 4, 6, 7, 15, 8, 8, 24, 5, 6, 67, 45, 23, 7, 28, 1, 45, 98, 6, 65, 45,
                         23, 12]
    listEtalon = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 12, 15, 23, 23, 24, 28, 28, 45, 45, 45, 65, 65, 67, 98]
    return (listBigShuffle_25, listEtalon)
