def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

def test_add():
    assert add(5, 4) == 9
    assert add(-3, 7) == 4
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_power():
    assert power(2, 8) == 256
    assert power(3, 0) == 1
    assert power(5, 2) == 25
