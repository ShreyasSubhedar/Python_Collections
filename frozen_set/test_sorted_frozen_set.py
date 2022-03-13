import unittest
from frozen_set.sorted_frozen_set import SortedFrozenSet


class TestConstruction(unittest.TestCase):
    def test_construct_empty(self):
        s = SortedFrozenSet([])

    def test_construct_from_non_empty_list(self):
        s = SortedFrozenSet([1, 2, 3, 4])

    def test_construct_from_iterator(self):
        li = [1, 2, 3, 4]
        iterator = iter(li)
        s = SortedFrozenSet(iterator)

    def test_construct_with_no_args(self):
        s = SortedFrozenSet()

class TestContainerProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SortedFrozenSet([1, 2, 3, 4, 5, 6])

    def test_positive_contained(self):
        self.assertTrue(2 in self.s)

    def test_negative_contained(self):
        self.assertFalse(12 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(121 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(2 not in self.s)

class TestSizeProtocol(unittest.TestCase):
    def test_zero_len(self):
        s = SortedFrozenSet()
        assert len(s) == 0

    def test_one_len(self):
        s = SortedFrozenSet([23])
        assert len(s) == 1

    def test_ten_len(self):
        s = SortedFrozenSet(range(10))
        assert len(s) == 10

    def test_duplicate_size(self):
        s = SortedFrozenSet([2, 2, 2, 2])
        assert len(s) == 1

class TestIteratorProtocol(unittest.TestCase):

    def test_iterator_set(self):
        s = SortedFrozenSet([10, 1, 2, 3])
        it = iter(s)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 10)
        self.assertRaises(StopIteration)

    def test_iterator_set_revers(self):
        s = SortedFrozenSet([10, 1, 2, 3])
        it = reversed(s)
        self.assertEqual(next(it), 10)
        self.assertEqual(next(it), 3)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 1)
        self.assertRaises(StopIteration)

    def test_iterator_for_loop(self):
        s = SortedFrozenSet([10, 1, 2, 3])
        expected = [1, 2, 3, 10]
        index = 0
        for i in s:
            self.assertEqual(i, expected[index])
            index += 1

class TestSequence(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SortedFrozenSet([10, 2, 3, 1])

    # def test_index_zero(self):
    #     self.assertEqual(self.s[0], 1)
    #
    # def test_index_last(self):
    #     self.assertEqual(self.s[3], 10)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            self.s[13]

    # def test_index_minus_one(self):
    #     self.assertEqual(self.s[-1], SortedFrozenSet[10])
    #
    def test_index_minus_four(self):
        self.assertEqual(self.s[1:3], SortedFrozenSet([2, 3]))

    def test_type_mismatch(self):
        self.assertNotEqual(self.s[2:], [2, 3, 4])

    def test_index_error_with_minus_index(self):
        with self.assertRaises(IndexError):
            self.s[-232]

class TestRepresentation(unittest.TestCase):
    def test_empty_class(self):
        s = SortedFrozenSet()
        self.assertEqual(repr(s), "SortedFrozenSet()")

    def test_repr_two(self):
        s = SortedFrozenSet([1, 2, 3, 4, 5])
        self.assertEqual(repr(s), "SortedFrozenSet([1, 2, 3, 4, 5])")

class TestHashable(unittest.TestCase):
    def test_equal_hash(self):
        self.assertEqual(hash(SortedFrozenSet([1,2,3])), hash(SortedFrozenSet([1,2,3])))

class TestIndexing(unittest.TestCase):
    def test_index(self):
        s = SortedFrozenSet([2,1,3,10])
        self.assertEqual(s.index(3),2)

if __name__ == '__main__':
    unittest.main()
