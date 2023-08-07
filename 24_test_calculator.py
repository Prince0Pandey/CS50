'''
from calculator_23 import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print('2 squared was not 4')

    try:
        assert square(3) == 9
    except AssertionError:
        print('3 squared was not 9')

    try:
        assert square(-2) == 4
    except AssertionError:
        print('-2 squared was not 4')

    try:
        assert square(-3) == 9
    except AssertionError:
        print('-3 squared was not 9')

    try:
        assert square(0) == 0
    except AssertionError:
        print('0 squared was not 0')

    # if square(2) != 4:
    #     print('2 squared was not 4')
    # if square(3) != 9:
    #     print('3 squared was not 9')

if __name__ == '__main__':
    main()
'''

# from calculator_23 import square

#instead of writing one big function to test we can divide it in parts so that tracking
#will be easier

# def test_square():
#     assert square(3) == 9
#     assert square(2) == 4
#     assert square(1) == 1
#     assert square(0) == 0
#     assert square(-1) == 1      #here this test case will fail and program will not be executed further so we don't know
#                                 #which other cases will get failed after this line
#     assert square(-2) == 4
#     assert square(-3) == 9

#here if any one fails, other function will be attempted
from calculator_23 import square
import pytest
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(1) == 1

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
