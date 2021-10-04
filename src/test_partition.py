# -*- coding: utf-8 -*-

from .loader import load_situation
from .partition import Partition


situation_1 = load_situation(1)
situation_2 = load_situation(2)
situation_3 = load_situation(3)
situation_4 = load_situation(4)
situation_5 = load_situation(5)
situation_6 = load_situation(6)
situation_7 = load_situation(7)
situation_8 = load_situation(8)


# TEST measure_sequence()
# =======================

def test_sequence_situation_0():
    """ With no reapeat symbols at all """
    partition = Partition(total_number_of_measures=5)
    sequence = partition.measure_sequence()
    answer = [1, 2, 3, 4, 5]
    assert sequence == answer


def test_sequence_situation_1():
    partition = Partition.from_situation(situation_1)
    sequence = partition.measure_sequence()
    assert sequence == situation_1['measure_sequence']




# TEST is_valid()
# ===============

def test_is_valid_situation_1():
    partition = Partition.from_situation(situation_1)
    valid_value = partition.is_valid()
    assert valid_value == situation_1['valid']


def test_is_valid_situation_2():
    partition = Partition.from_situation(situation_2)
    valid_value = partition.is_valid()
    assert valid_value == situation_2['valid']


def test_is_valid_situation_3():
    partition = Partition.from_situation(situation_3)
    valid_value = partition.is_valid()
    assert valid_value == situation_3['valid']


def test_is_valid_situation_4():
    partition = Partition.from_situation(situation_4)
    valid_value = partition.is_valid()
    assert valid_value == situation_4['valid']


def test_is_valid_situation_5():
    partition = Partition.from_situation(situation_5)
    valid_value = partition.is_valid()
    assert valid_value == situation_5['valid']


def test_is_valid_situation_6():
    partition = Partition.from_situation(situation_6)
    valid_value = partition.is_valid()
    assert valid_value == situation_6['valid']


def test_is_valid_situation_7():
    partition = Partition.from_situation(situation_7)
    valid_value = partition.is_valid()
    assert valid_value == situation_7['valid']


def test_is_valid_situation_8():
    partition = Partition.from_situation(situation_8)
    valid_value = partition.is_valid()
    assert valid_value == situation_8['valid']
