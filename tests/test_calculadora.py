from src.calculadora import soma,sub, mult

def test_soma():
    assert soma(3,7) == 10
    assert soma(2,3) == 5
    assert soma(8,13) == 21

def test_sub():
    assert sub(7,3) == 4
    assert sub(5,2) == 3
    assert sub(18,7) == 11

def test_soma_error():
    assert soma(2,2) != 5
    assert soma(5,8) != 4
    assert soma(4,9) != 7

def test_sub_error():
    assert sub(4,2) != 8

def test_mult():
    assert mult(2,2) == 4
    assert mult(3,9) == 27
    assert mult(2,13) == 26

def test_mult_error():
    assert mult(3,5) != 14
    assert mult(5,8) != 39
    assert mult(7,2) != 13

