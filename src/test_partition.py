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


def test_sequence_situation_0():
    """ With no reapeat symbols at all """
    partition = Partition(total_number_of_measures=5)
    sequence = partition.measure_sequence()
    answer = [1, 2, 3, 4, 5]
    assert sequence == answer

def test_sequence_situation_1():
    part_1 = Partition.from_situation(situation_1)
    sequence = part_1.measure_sequence()
    assert sequence == situation_1['measure_sequence']
