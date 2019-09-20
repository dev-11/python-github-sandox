target = __import__("app.py")

def test_normal():
    pass


def test_normal_2():
    pass

def test_3():
    a = target.fun(1)
    assert a == 2
    
    
