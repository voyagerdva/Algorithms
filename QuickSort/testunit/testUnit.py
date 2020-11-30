import unittest

from fixtures import fixtures as fx
from myQuickSort import myQuickSort as qs


class myTestQuickSort(unittest.TestCase):

    def test_partShuffleReady(self):
        (listOriginal, listEtalon, base, sepEtalon, low, high) = fx.fixturePartShuffleReady()
        (listResult, sepPart) = qs.partition(listOriginal, base, low, high)
        self.assertEqual(listResult, listEtalon)
        self.assertEqual(sepEtalon, sepPart)

    def test_partShuffle(self):
        (listOriginal, listEtalon, base, sepEtalon, low, high) = fx.fixturePartShuffle()
        (listResult, sepPart) = qs.partition(listOriginal, base, low, high)
        self.assertEqual(listResult, listEtalon)
        self.assertEqual(sepEtalon, sepPart)

    def test_directEtalon(self):
        (original, listEtalon) = fx.fixtureEtalon()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_Shuffle(self):
        (original, listEtalon) = fx.fixtureShuffle()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_Shuffle_100(self):
        (original, listEtalon) = fx.fixtureShuffle_100()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_333777444999(self):
        (original, listEtalon) = fx.fixture333777444999()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_Empty(self):
        (original, listEtalon) = fx.fixtureEmpty()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_Single(self):
        (original, listEtalon) = fx.fixtureSingle()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_Negative(self):
        (original, listEtalon) = fx.fixtureNegative()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_NegativePositive(self):
        (original, listEtalon) = fx.fixtureNegativePositive()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    # def test_Letters(self):
    #     (original, listEtalon) = fx.fixtureLetters()
    #     result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
    #     self.assertEqual(result, listEtalon)

    def test_Float(self):
        (original, listEtalon) = fx.fixtureFloat()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_BackDirection(self):
        (original, listEtalon) = fx.fixtureBackDirection()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_AlmostShuffle(self):
        (original, listEtalon) = fx.fixtureAlmostShuffle()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_bigShuffle(self):
        (original, listEtalon) = fx.fixtureBigShuffle()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)

    def test_bigShuffle_25(self):
        (original, listEtalon) = fx.fixtureBigShuffle_25()
        result = qs.myQuickSort(original, 0, (len(original) - 1))[0]
        self.assertEqual(result, listEtalon)


if __name__ == '__main__':
    unittest.main()
