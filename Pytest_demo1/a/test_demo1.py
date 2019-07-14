# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Datetime: 2019/6/15 21:05

import  pytest

a = 100


def test_case01():
    global a
    a += 1
    print(a)
    assert a >= 101


def test_case02():
    print(3)


def test_case03():
    assert (1, 2, 3) == (3, 2, 1)
    

def test_case04():
    print('2+3 <= 4')
    assert 2 + 3 <= 4
    
    
def test_case05():
    print('case06')
    assert 'kobe' not in ['kobe', 'james', 'Wade']

if __name__ == '__main__':
    pytest.main()
