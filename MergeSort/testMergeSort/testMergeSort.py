import unittest

from merge.fixtureMergeSort import fixtureMergeSort as fixture
from merge.mergeSort import mergeSort


class myTestQuickSort(unittest.TestCase):

    def testListShuffle10Elements(self):
        (original, listEtalon) = fixture.fixtureMakeListShuffle10Elements()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testShuffle_100(self):
        (original, listEtalon) = fixture.fixtureMakeListShuffleInRange100()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def test333777444999(self):
        (original, listEtalon) = fixture.fixtureMakeListSeveralSequencesOf7394()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testEmpty(self):
        (original, listEtalon) = fixture.fixtureMakeListEmpty()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testSingle(self):
        (original, listEtalon) = fixture.fixtureMakeListSingle()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testNegative(self):
        (original, listEtalon) = fixture.fixtureMakeListNegativeDigitals()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testNegativePositive(self):
        (original, listEtalon) = fixture.fixtureMakeListNegativeAndPositiveDigitals()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testLetters(self):
        (original, listEtalon) = fixture.fixtureMakeListLetters()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testFloat(self):
        (original, listEtalon) = fixture.fixtureMakeListFloatDigitals()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testBackDirection(self):
        (original, listEtalon) = fixture.fixtureMakeListBackDirectionfromTENtoONE()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testAlmostShuffle(self):
        (original, listEtalon) = fixture.fixtureMakeListAlmostShuffle10Elements()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testbigShuffle(self):
        (original, listEtalon) = fixture.fixtureMakeListShuffle30Elements()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)

    def testdirectEtalon(self):
        (original, listEtalon) = fixture.fixtureMakeListEtalonDirect10Elements()
        result = mergeSort(original)
        self.assertEqual(result, listEtalon)


if __name__ == '__main__':
    unittest.main()
