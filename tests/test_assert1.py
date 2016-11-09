# content of test_assert1.py
def f(x):
    return x+1

def test_function():
    assert f(3) == 4, "3+1 should be 4"
