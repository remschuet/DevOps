from app.my_class import MyCalculator

def test_add():
    calc = MyCalculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = MyCalculator()
    assert calc.subtract(5, 2) == 3

def test_subtract_2():
    calc = MyCalculator()
    assert calc.subtract(5, 2) == 5
