from app.my_class import MyCalculator

def test_add():
    calc = MyCalculator()
    assert calc.add(2, 3) == 6

def test_subtract():
    calc = MyCalculator()
    assert calc.subtract(5, 2) == 3
