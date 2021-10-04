# -*- coding: utf-8 -*-


def test_list_equals():
    list_1 = [1,5,3]
    list_2 = [1,5,3]
    assert list_1 == list_2


def test_list_not_equals_not_same_length():
    list_1 = [1,5,3,5]
    list_2 = [1,5,3]
    assert list_1 != list_2


def test_list_not_equals_not_same_numbers():
    list_1 = [1,5,3]
    list_2 = [1,5,142]
    assert list_1 != list_2
