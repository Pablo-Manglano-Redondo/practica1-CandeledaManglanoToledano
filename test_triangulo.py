import pytest
from triangulo import checktriangle


def test_case1_escaleno():
    assert checktriangle(6, 5, 10) == "Triangulo escaleno"


def test_case3_isosceles():
    # Caso 3 en PDF: 3, 3, 4
    assert checktriangle(3, 3, 4) == "Triangulo isosceles"


def test_case2_equilatero():
    # Caso 2 en PDF: 6, 6, 6
    assert checktriangle(6, 6, 6) == "Triangulo equilatero"


def test_case4_no_triangulo_cero():
    # Caso 4 en PDF: 4, 3, 0
    assert checktriangle(4, 3, 0) == "No es un triangulo"


def test_case5_no_triangulo_imposible():
    # Caso 5 en PDF: 8, 2, 4
    assert checktriangle(8, 2, 4) == "No es un triangulo"
