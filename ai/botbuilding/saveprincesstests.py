import unittest
from saveprincesstwo import nextMove

class SavePrincessTests(unittest.TestCase):

  def testTwoByTwoMoveDown(self):
    n = 2
    r = 0
    c = 1
    grid = ["-m", "p-"]
    
    self.assertEqual("DOWN", nextMove(n, r, c, grid))

  def testTwoByTwoMoveUp(self):
    n = 2
    r = 1
    c = 0
    grid = ["-p", "m-"]
    
    self.assertEqual("UP", nextMove(n, r, c, grid))

  def testTwoByTwoMoveLeft(self):
    n = 2
    r = 0
    c = 1
    grid = ["pm", "--"]
    
    self.assertEqual("LEFT", nextMove(n, r, c, grid))

  def testTwoByTwoMoveRight(self):
    n = 2
    r = 0
    c = 0
    grid = ["mp", "--"]
    
    self.assertEqual("RIGHT", nextMove(n, r, c, grid))

if __name__ == '__main__':
  unittest.main()
