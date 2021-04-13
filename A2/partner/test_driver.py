## @file test_All.py
#  @author Bhavna Pereira
#  @brief This file is used to test methods relating to A2
#  @date 16/02/2021
#  @details This file tests methods within CircleT.py, TriangleT.py,
#           BodyT.py, and Scene.py

import pytest
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene

goodcircle = CircleT(10, 11, 12, 13)


def test_xcoordcircle():
    expectedxcoord = 10
    assert goodcircle.cm_x() == expectedxcoord


def test_ycoordcircle():
    expectedycoord = 11
    assert goodcircle.cm_y() == expectedycoord


def test_mass():
    expectedmass = 13
    assert goodcircle.mass() == expectedmass


def test_minert():
    expected_inert = 936
    assert goodcircle.m_inert() == expected_inert


def test_validrad():
    with pytest.raises(ValueError) as e:
        CircleT(10, 12, -1, 13)
    assert "Invalid Input" == str(e.value)


def test_validmass():
    with pytest.raises(ValueError) as e:
        CircleT(10, 11, 12, -1)
    assert "Invalid Input" == str(e.value)


goodtriangle = TriangleT(10, 20, 30, 40)


def test_xcoordtriangle():
    expectedxcoord = 10
    assert goodtriangle.cm_x() == expectedxcoord


def test_ycoordtriangle():
    expectedycoord = 20
    assert goodtriangle.cm_y() == expectedycoord


def test_masstriangle():
    expectedmass = 40
    assert goodtriangle.mass() == expectedmass


def test_minerttriangle():
    expectedminert = 3000
    assert goodtriangle.m_inert() == expectedminert


def test_validsidelength():
    with pytest.raises(ValueError) as e:
        TriangleT(10, 20, -1, 40)
    assert "Invalid Input" == str(e.value)


def test_validmass_triangle():
    with pytest.raises(ValueError) as e:
        TriangleT(10, 20, -1, 40)
    assert "Invalid Input" == str(e.value)


b = BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, 10])


def test_cm_x_body():
    expectedxcoord = 0
    assert b.cm_x() == expectedxcoord


def test_cm_y_body():
    expectedycoord = 0
    assert b.cm_y() == expectedycoord


def test_mass_body():
    expectedmass = 40
    assert b.mass() == expectedmass


def test_minert_body():
    expectedminert = 80
    assert b.m_inert() == expectedminert


def test_valid_body():
    with pytest.raises(ValueError) as e:
        BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, -1])
    assert "Invalid Input" == str(e.value)


def test_valid_body2():
    with pytest.raises(ValueError) as e:
        BodyT([1, -1, -1, 1], [1, 1, -1], [10, 10, 10, 10])
    assert "Invalid Input" == str(e.value)


triangle = TriangleT(1, 2, 3, 4)


def Fx(t):
    return 34 if t < 19 else 0


def Fy(t):
    return 17


goodscene = Scene(triangle, Fx(4), Fy(4), 10, 12)


def test_set_shape():
    goodscene.set_shape(triangle)
    assert goodscene.get_shape() == (triangle)


def test_set_forces():
    goodscene.set_unbal_forces(Fx(4), Fy(4))
    assert goodscene.get_unbal_forces() == (34, 17)


def test_set_forces2():
    goodscene.set_unbal_forces(Fx(35), Fy(4))
    assert goodscene.get_unbal_forces() == (0, 17)


def test_set_velocities():
    goodscene.set_init_velo(10, 12)
    assert goodscene.get_init_velo() == (10, 12)


def test_get_shape():
    expectedshape = triangle
    assert goodscene.get_shape() == expectedshape


def test_get_forces():
    expectedforces = (0, 17)
    assert goodscene.get_unbal_forces() == expectedforces


def test_get_velo():
    expectedvelocities = (10, 12)
    assert goodscene.get_init_velo() == expectedvelocities
