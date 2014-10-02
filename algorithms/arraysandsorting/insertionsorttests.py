import unittest
import sys
from StringIO import StringIO
from insertionsortone import insertionSort

class InsertionSortTests(unittest.TestCase):

  def setUp(self):
    self.saved_stdout = sys.stdout

  def tearDown(self):
    sys.stdout = self.saved_stdout

  def test_OneElement(self):
    ar = [1]
    solution = "1"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

  def test_TwoElementsFirst(self):
    ar = [2, 1]
    solution = "2 2\n1 2"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())
  
  def test_ThreeElementsFirst(self):
    ar = [2, 3, 1]
    solution = "2 3 3\n2 2 3\n1 2 3"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

  def test_FourElementsFirst(self):
    ar = [2, 3, 4, 1]
    solution = "2 3 4 4\n2 3 3 4\n2 2 3 4\n1 2 3 4"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())


  def test_FourElementsSecond(self):
    ar = [1, 3, 4, 2]
    solution = "1 3 4 4\n1 3 3 4\n1 2 3 4"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

  def test_FourElementsThird(self):
    ar = [1, 2, 4, 3]
    solution = "1 2 4 4\n1 2 3 4"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

  def test_FourElementsFourth(self):
    ar = [1, 2, 3, 4]
    solution = "1 2 3 4"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

  def test_FiveElementsWithMatch(self):
    ar = [1, 2, 3, 4, 2]
    solution = "1 2 3 4 4\n1 2 3 3 4\n1 2 2 3 4\n1 2 2 3 4"
    out = StringIO()
    sys.stdout = out
    insertionSort(ar)
    self.assertEqual(solution, out.getvalue().strip())

if __name__ == '__main__':
  unittest.main()
