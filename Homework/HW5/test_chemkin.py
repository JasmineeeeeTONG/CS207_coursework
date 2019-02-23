import numpy as np
from chemkin import *

# Unittests: get_progress_rate()
def test_get_progress_rate_result():
    assert get_progress_rate(3, [1.0, 2.0, 1.0], [1.0, 1.0, 3.0]) == 6

def test_get_progress_rate_non_positive_k():
    try:
        get_progress_rate(-1, [1.0, 2.0, 1.0], [1.0, 1.0, 3.0])
    except ValueError as err:
        assert(type(err) == ValueError)

def test_get_progress_rate_type():
    try:
        get_progress_rate('hahaha', [1.0, 2.0, 1.0], [1.0, 1.0, 3.0])
    except TypeError as err:
        assert(type(err) == TypeError)

def test_get_progress_rate_diff_length():
    try:
        get_progress_rate(3, [1.0, 2.0, 1.0], [1.0, 1.0])
    except Exception as err:
        assert(type(err) == Exception)


# Unittests: get_progress_rate_list()
def test_get_progress_rate_list_result():
    assert get_progress_rate_list([10, 10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]]) == [40.0, 10.0]

def test_get_progress_rate_list_non_positive_k():
    try:
        get_progress_rate_list([1, -1], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    except ValueError as err:
        assert(type(err) == ValueError)

def test_get_progress_rate_list_type():
    try:
        get_progress_rate_list(['hahaha', 'hahaha'], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    except TypeError as err:
        assert(type(err) == TypeError)

def test_get_progress_rate_list_diff_length():
    try:
        get_progress_rate_list([10, 10], [1.0, 2.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_progress_rate_list_diff_shape_1d():
    try:
        get_progress_rate_list([10, 10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [1, 2, 3])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_progress_rate_list_diff_shape_2d():
    try:
        get_progress_rate_list([10, 10], [1.0, 2.0, 1.0], [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2]])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_progress_rate_list_wrong_k_length():
    try:
        get_progress_rate_list([10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [2.0, 0.0, 2.0]], [[0.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    except Exception as err:
        assert(type(err) == Exception)


# Unittests: get_reaction_rate()
def test_get_reaction_rate_result():
    ret = get_reaction_rate([1, 1], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    ret = ret.reshape(ret.shape[0])
    ret_0 = ret[0]
    ret_1 = ret[1]
    ret_2 = ret[2]
    assert (ret_0 == -3 and ret_1 == -6 and ret_2 == 2)

def test_get_reaction_rate_non_positive_k():
    try:
        get_reaction_rate([1, -1], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    except ValueError as err:
        assert(type(err) == ValueError)

def test_get_reaction_rate_type():
    try:
        get_reaction_rate(['hahaha', 'hahaha'], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    except TypeError as err:
        assert(type(err) == TypeError)

def test_get_reaction_rate_diff_length():
    try:
        get_reaction_rate([10, 10], [1.0, 2.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_reaction_rate_diff_shape_1d():
    try:
        get_reaction_rate([10, 10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [1, 2, 3])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_reaction_rate_diff_shape_2d():
    try:
        get_reaction_rate([10, 10], [1.0, 2.0, 1.0], [[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2]])
    except Exception as err:
        assert(type(err) == Exception)

def test_get_reaction_rate_wrong_k_length():
    try:
        get_reaction_rate([10], [1.0, 2.0, 1.0], [[1.0, 2.0, 0.0], [0.0, 0.0, 2.0]], [[0.0, 0.0, 1.0], [1.0, 2.0, 0.0]])
    except Exception as err:
        assert(type(err) == Exception)