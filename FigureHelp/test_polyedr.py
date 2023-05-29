from shadow.polyedr import Polyedr
from math import sqrt


def test_sum_perimeter_01():
    Poly = Polyedr(f'data/test_1.geom')
    assert Poly.sum_perimeter() == 0


def test_sum_perimeter_02():
    Poly = Polyedr(f'data/test_2.geom')
    assert Poly.sum_perimeter() == 0


# однин квадрат перекрывает другой
def test_sum_perimeter_03():
    Poly = Polyedr(f'data/test_3.geom')
    assert Poly.sum_perimeter() == 400
