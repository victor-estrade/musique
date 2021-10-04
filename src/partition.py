# -*- coding: utf-8 -*-
from dataclasses import dataclass
from dataclasses import field
from typing import List

@dataclass
class Partition():
    total_number_of_measures : int
    repeat_forward : List[int] = field(default_factory=list)
    repeat_backward : List[int] = field(default_factory=list)
    ending_one : List[int] = field(default_factory=list)
    ending_two : List[int] = field(default_factory=list)
    segno : List[int] = field(default_factory=list)
    dalsegno : List[int] = field(default_factory=list)
    dacapo : List[int] = field(default_factory=list)
    tocoda : List[int] = field(default_factory=list)
    coda : List[int] = field(default_factory=list)

    def from_situation(situation):
        lists = situation['lists']
        total_number_of_measures = situation['total_number_of_measures']
        return Partition(total_number_of_measures=total_number_of_measures, **lists)

    def measure_sequence(self):
        return list(range(1, self.total_number_of_measures + 1))

    def is_valid(self):
        return True
