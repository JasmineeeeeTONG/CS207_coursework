import L2

def test_L2_result_1():
    assert L2.L2([4, 3], [1, 1]) == 5.

def test_L2_result_2():
    assert L2.L2([5., 12.]) == 13.

def test_L2_sameLength():
    try:
        L2.L2([4, 3], [1])
    except ValueError as err:
        assert(type(err) == ValueError)

def test_L2_types():
    try:
        L2.L2('hahahaha')
    except TypeError as err:
        assert(type(err) == TypeError)