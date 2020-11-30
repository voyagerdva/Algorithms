import unittest
import sys

sys.path.append("d:\\= GitRepo\\merge")
sys.path.append("d:\\= GitRepo\\merge\\fixtures")

from fixtureMerge import fixtureMerge as fx
from merge import merge as mrg


class myTestMerge(unittest.TestCase):

    def test_mergeList7ElementsWithList4(self):
        (listA, listB, listEtalon) = fx.fixtureMakeTwoSortedLists7And4SizeAndOneMergedList()
        (listResult) = mrg.merge(listA, listB)
        self.assertEqual(listResult, listEtalon)

    def test_mergeList4ElementsWithListEmpty(self):
        (listA, listB, listEtalon) = fx.fixtureMakeOneSortedList4SizeOneEmptyListAndOneMergedList()
        (listResult) = mrg.merge(listA, listB)
        self.assertEqual(listResult, listEtalon)

    def test_mergeListEmptyWithList4Elements(self):
        (listA, listB, listEtalon) = fx.fixtureMakeOneEmptyListOneSortedList4SizeAndOneMergedList()
        (listResult) = mrg.merge(listA, listB)
        self.assertEqual(listResult, listEtalon)

    def test_mergeListEmptyWithListEmpty(self):
        (listA, listB, listEtalon) = fx.fixtureMakeTwoEmptyListsAndOneEmptyListForEtalon()
        (listResult) = mrg.merge(listA, listB)
        self.assertEqual(listResult, listEtalon)


if __name__ == '__main__':
    unittest.main()
