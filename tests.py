target = __import__("my_app")

def test_normal():
    pass


def test_normal_2():
    pass

def test_3():
    a = target.app.fun(1)
    assert a == 2
    
    
