import unittest
from functions import *

#---------------------------------------------------------------cubeVol
class TestCubeInputs(unittest.TestCase):
  def test_cube_inputs(self): # test simple values
    self.assertEqual(cubeVol(2),8)
    self.assertEqual(cubeVol(1),1)
    self.assertEqual(cubeVol(0),0)

  def test_cube_inputComplex(self): # test floats
    self.assertEqual(cubeVol(5.5),166.375)
    self.assertEqual(cubeVol(1+1),8)
    self.assertEqual(cubeVol(-2),-8)

  def test_cube_inputType(self): # test non-numeric inputs
    self.assertRaises(TypeError, cubeVol, True)

#---------------------------------------------------------------aveElem
class TestElemInputs(unittest.TestCase):
  def test_elem_inputs(self): # simple arrays
    self.assertEqual(aveElem([1,2,3,4,5,6,7,8,9]),5)
    self.assertEqual(aveElem([9,8,7,6,5,4,3,2,1]),5)

  def test_elem_negative(self): # negative ave array
    self.assertEqual(aveElem([-1,-2,1,2]),0)
    self.assertEqual(aveElem([-1,-2,-3,-4,-5,-6,-7,-8,-9]),-5)

  def test_elem_empty(self): # empty, divide by 0 array
    self.assertEqual(aveElem([]),0)

#---------------------------------------------------------------FullName
class TestNameInputs(unittest.TestCase):
  def test_name_inputs(self): # simple name
    self.assertEqual(fullName("John", "Doe"),"John Doe")
    self.assertEqual(fullName("88", "99"),"88 99")
    self.assertEqual(fullName("John", "of Doe"),"John of Doe")

if(__name__ == '__main__'):
  unittest.main(verbosity=2)