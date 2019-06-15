# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Datetime: 2019/6/15 21:05

import pytest

class Test_demo():

    def test_case01(self):
        print(1)

    def test_case02(self):
        print(2)


class Test_demo2():

    def test_case03(self):
        print(3)


@pytest.mark.huigui
@pytest.mark.smoke
def test_case04():
    print(3)


def test_case05():
    print(5)


@pytest.mark.smoke
def test_case06():
    print(6)


@pytest.mark.huigui
def test_huigui01():
    print('huigui01')