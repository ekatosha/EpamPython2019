from SiamObj import SiamObj
import pytest


def test_SiamSameObj():
    unit1 = SiamObj('1', '2', a=1)
    unit2 = SiamObj('1', '2', a=1)
    assert unit1 is unit2


def test_SiamDifObj():
    unit3 = SiamObj(1, 2, g=3)
    unit4 = SiamObj(1, 2, g=5)
    assert unit3 is not unit4


def test_SiamSetAtr():
    unit1 = SiamObj('1', '2', a=1)
    unit1.a = 4
    assert unit1.a == 4

def test_SiamSetAtrConnect():
    unit2 = SiamObj('1', '2', a=1)
    unit4 = SiamObj(1, 2, g=5)
    unit2.connect(1, 2, 5).g = 7
    assert unit4.g == 7


def test_SiamPool():
    unit1 = SiamObj('1', '2', a=1)
    unit2 = SiamObj('1', '2', a=1)
    unit3 = SiamObj(1, 2, g=3)
    unit4 = SiamObj(1, 2, g=5)
    assert len(unit2.pool) == 3

def test_SiamPool_del():
    unit1 = SiamObj('1', '2', a=1)
    unit2 = SiamObj('1', '2', a=1)
    unit3 = SiamObj(1, 2, g=3)
    unit4 = SiamObj(1, 2, g=5)
    del unit3
    assert len(unit2.pool) == 2
