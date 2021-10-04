# -*- coding: utf-8 -*-
from .loader import load_situation
from .sheet import Sheet, SheetReader

situation_1 = load_situation(1)
situation_2 = load_situation(2)
situation_3 = load_situation(3)
situation_4 = load_situation(4)
situation_5 = load_situation(5)
situation_6 = load_situation(6)
situation_7 = load_situation(7)
situation_8 = load_situation(8)



def test_sheet_read_simple():
    """ With no reapeat symbols at all """
    sheet = Sheet([[], [], [], [], []])
    reader = SheetReader()
    sequence = reader.read(sheet)
    answer = [1, 2, 3, 4, 5]
    assert sequence == answer


def test_situation_1():
    sheet = Sheet.from_situation(situation_1)
    reader = SheetReader()
    sequence = reader.read(sheet)
    assert sequence == situation_1['measure_sequence']
    
