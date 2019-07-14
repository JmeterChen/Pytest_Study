# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Datetime: 2019/6/15 21:05

import pytest
import time


class Test_demo():

    def test_case06(self):
        print(1)

    def test_case07(self):
        print(2)


class Test_demo2():

    def test_case08(self):
        print(3)


@pytest.mark.huigui
@pytest.mark.smoke
def test_case09():
    print(3)


def test_case10():
    assert 5 <= 4
    print(5)


@pytest.mark.smoke
def test_case11():
    print(6)


@pytest.mark.huigui
def test_case12():
    print('huigui01')
    
    
def test_case13():
    time.sleep(0.1)