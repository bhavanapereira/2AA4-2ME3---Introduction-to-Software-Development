## @file test_driver.py
#  @author Bhavana Pereira
#  @brief The following aim to test the validity of the following files: triangle_adt, complex_T
#  @date 20/01/2021


import pytest
from triangle_adt import TriangleT, TriType
from complex_adt import ComplexT


validInput1 = ComplexT(2, 3)
validInput2 = ComplexT(3, 9)
compEdgeCase1 = ComplexT(0, 0)
compEdgeCase2 = ComplexT(-1, 0)

validIsosceles = TriangleT(1,1,2)
validScalene = TriangleT(1,2,3)
validRight = TriangleT(3,4,5)
validEquilat = TriangleT(3,3,3)
triEdgeCase1 = TriangleT(0, 1, 2)
triEdgeCase2 = TriangleT(0.5, 1, 1.5)
triEdgeCase2 = TriangleT(-3, 4, 5)





