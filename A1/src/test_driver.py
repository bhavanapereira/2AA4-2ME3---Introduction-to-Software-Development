## @file test_driver.py
#  @author Bhavana Pereira
#  @brief The following aim to test the validity of the following files: triangle_adt, complex_T
#  @date 20/01/2021


import pytest
from triangle_adt import TriangleT, TriType
from complex_adt import ComplexT


validInput1 = ComplexT(2, 3)
compEdgeCase1 = ComplexT(0, 0)
compEdgeCase2 = ComplexT(-1, -5)
comp = ComplexT(2, 3)
comp2 = ComplexT(3, 3)

validIsosceles = TriangleT(1,1,2)
validScalene = TriangleT(1,2,3)
validRight = TriangleT(3,4,5)
validEquilat = TriangleT(3,3,3)
triEdgeCase1 = TriangleT(0, 1, 2)
triEdgeCase2 = TriangleT(0.5, 1, 1.5)
triEdgeCase2 = TriangleT(-3, 4, 5)
tri = TriangleT(3, 3, 3)
tri2 = TriangleT(1, 2, 3)

def test_Real():
	expectedReal = 2
	assert validInput1.real() == expectedReal

def edge_test_Real():
	expectedReal1 = 0
	assert compEdgeCase1.real() == expectedReal1

def edge2_test_Real():
	expectedReal2 = -1
	assert compEdgeCase2.real() == expectedReal2

def test_Imag():
	expectedImag = 3
	assert validInput1.imag() == expectedImag

def edge_test_Imag():
	expectedImag1 = 0
	assert compEdgeCase1.imag() == expectedImag1

def edge2_test_Imag():
	expectedImag2 = -5
	assert compEdgeCase2.imag() == expectedImag2

def r_test():
	expectedR = 3.6055
	assert pytest.approx(validInput1.r(), rel=1e-3) == expectedR

def edge_r_test():
	expectedR1 = 0
	assert pytest.approx(compEdgeCase1.r(), rel=1e-3) == expectedR1

def edge2_r_test():
	expectedR2 = 5.0990
	assert pytest.approx(compEdgeCase2.r(), rel=1e-3) == expectedR2

def test_getPhi():
	expectedPhi = 0.9828
	assert pytest.approx(validInput1.get_phi(), rel=1e-3) == expectedPhi

def edge_test_getPhi():
	expectedPhi1 = 0
	assert pytest.approx(compEdgeCase1.get_phi(), rel=1e-3) == expectedPhi1

def edge2_test_getPhi():
	expectedPhi2 = -1.7682
	assert pytest.approx(compEdgeCase2.get_phi(), rel=1e-3) == expectedPhi2


def test_equal():
	assert validInput1.equal(comp) == True

def test2_equal():
	assert validInput1.equal(comp2) == False

def test_conj():
	expectedConj = ComplexT(2, -3)
	assert validInput1.conj() == expectedConj

def edge_test_conj():
	expectedConj1 = ComplexT(-1, 5)
	assert compEdgeCase2.conj() == expectedConj1

def test_add():
	expectedAdd = ComplexT(4, 6)
	assert validInput1.add(comp) == expectedAdd

def edge_test_add():
	expectedAdd1 = ComplexT(1, -2)
	assert compEdgeCase2.add(comp) == expectedAdd1

def test_sub():
	expectedSub = ComplexT(0, 0)
	assert validInput1.sub(comp) == expectedSub

def edge_test_sub():
	expectedSub1 = ComplexT(3, 8)
	assert comp.sub(compEdgeCase2) == expectedSub1

def test_mult():
	expectedMult = ComplexT(4, 9)
	assert validInput1.mult(comp) == expectedMult

def test_recip():
	expectedRecip = ComplexT(0.1583, -0.2308)
	assert pytest.approx(validInput1.recip(), rel=1e-3) == expectedRecip

def test_div():
	expectedDiv = ComplexT(1, 1)
	assert validInput1.div(comp) == expectedDiv

def edge_test_div:
	with pytest.raises(ZeroDivisionError) as e:
		validInput1.div(compEdgeCase1)
	assert "Cannot Divide By Zero" == str(e.value)

####################################

def test_get_sides():
	expectedSides = (1, 1, 2)
	assert validIsosceles.getsides() == expectedSides

def edges_test_get_sides():
	with pytest.raises(ValueError) as e:
		triEdgeCase1.getsides():
	assert "This is not a valid triangle" == str(e.value)

def test_equal():
	excpectedEqual = True
	assert validEquilat.equal(tri) == excpectedEqual

def test2_equal():
	expectedEqual2 = False
	assert validEquilat.equal(tri2) == expectedEqual2

def test_perim():
	expectedPerim = 12
	assert validRight.perim() == expectedPerim

def test2_perim():
	with pytest.raises(ValueError) as e:
		triEdgeCase1.perim():
	assert "This is not a valid triangle" == str(e.value)



















