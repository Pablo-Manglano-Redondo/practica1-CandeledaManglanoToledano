import pytest
from triangulo import checktriangle


def test_case1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"


def test_case2_isosceles():
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"


def test_case3_equilatero():
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"


def test_case4_no_triangulo_con_cero():
    assert checktriangle(4, 3, 0) == "No es un triangulo"


def test_case5_no_triangulo_imposible():
    assert checktriangle(8, 2, 4) == "No es un triangulo"


def test_isosceles_bug_a_equals_c():
    # Covers the bug condition where a==c
    assert checktriangle(5, 3, 5) == "Triangulo isosceles"


def test_isosceles_b_equals_c():
    # Covers b==c condition
    assert checktriangle(3, 4, 4) == "Triangulo isosceles"


def test_condition_c_ge_a_plus_b():
    # c >= a + b
    assert checktriangle(1, 2, 4) == "No es un triangulo"


def test_condition_b_ge_a_plus_c():
    # b >= a + c
    assert checktriangle(1, 4, 2) == "No es un triangulo"
