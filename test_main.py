import main

def test_add():
    assert main.add(5, 4) == 9
    assert main.add(-3, 7) == 4
    assert main.add(0, 0) == 0

def test_multiply():
    assert main.multiply(3, 4) == 12
    assert main.multiply(-2, 3) == -6
    assert main.multiply(0, 5) == 0

def test_power():
    assert main.power(2, 8) == 256
    assert main.power(3, 0) == 1
    assert main.power(5, 2) == 25
