# -*- coding: utf-8 -*-

def test_dict_equals():
    dict_1 = {'a' : 1, 'b': {'aa': 5}}
    dict_2 = {'a' : 1, 'b': {'aa': 5}}
    assert dict_1 == dict_2


def test_dict_not_equals():
    dict_1 = {'a' : 1, 'b': {'aa': 5}}
    dict_2 = {'a' : 2, 'b': {'aa': 5}}
    assert dict_1 != dict_2


def test_dict_not_equals_deep():
    dict_1 = {'a' : 1, 'b': {'aa': 5}}
    dict_2 = {'a' : 1, 'b': {'aa': 2}}
    assert dict_1 != dict_2


def test_dict_and_list_equals():
    dict_1 = {'a' : 1, 'b': {'aa': 5}, 'lili' : [1,2,3] }
    dict_2 = {'a' : 1, 'b': {'aa': 5}, 'lili' : [1,2,3] }
    assert dict_1 == dict_2


def test_dict_and_list_equals_deep():
    dict_1 = {'a' : 1, 'b': {'aa': 5, 'lili' : [1,2,3]} }
    dict_2 = {'a' : 1, 'b': {'aa': 5, 'lili' : [1,2,3]} }
    assert dict_1 == dict_2


def test_dict_and_list_not_equals():
    dict_1 = {'a' : 1, 'b': {'aa': 5}, 'lili' : [1,45,3] }
    dict_2 = {'a' : 1, 'b': {'aa': 5}, 'lili' : [1,2,3] }
    assert dict_1 != dict_2


def test_dict_and_list_not_equals_deep():
    dict_1 = {'a' : 1, 'b': {'aa': 5, 'lili' : [1,45,3]} }
    dict_2 = {'a' : 1, 'b': {'aa': 5, 'lili' : [1,2,3]} }
    assert dict_1 != dict_2
