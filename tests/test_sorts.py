# -*- coding: utf-8 -*-
import unittest
import random

from sorts.bubble_sort import BubbleSort
from sorts.insertion_sort import InsertionSort


class SortTestCase(unittest.TestCase):
    """Creates a basic testcase to test different sorts.
    """

    def setUp(self):
        """Sets up some basic testing data.
        """
        self.collection = range(25)
        random.shuffle(self.collection)


class BubbleSortTest(SortTestCase):
    """Tests bubble sort.
    """

    def test_sort(self):
        """Tests the sort method.
        Checks the sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_quick_sort(self):
        """Tests the quick sort method.
        Checks the quick sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.quick_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_quickest_sort(self):
        """Tests the quickest sort method.
        Checks the quickest sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.quickest_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)


class InsertionSortTest(SortTestCase):
    """Tests insertion sort.
    """

    def test_sort(self):
        """Tests the sort method.
        Checks the sort method and whether the collection is sorted.
        """
        self.collection = InsertionSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)
