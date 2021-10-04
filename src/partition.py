# -*- coding: utf-8 -*-
import copy

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
        partition = copy.deepcopy(self)
        safety = 1
        safety_stop = 100_000
        current = 1
        end = self.total_number_of_measures
        sequence = []
        jumps = {}
        while current <= end and safety < safety_stop:
            safety += 1
            sequence.append(current)
            print(f"iter = {safety}, sequence = {sequence}")
            # Find next mesure to add to the sequence
            # Case 1 : if we reach an unused backward
            next_backward = next(iter(partition.repeat_backward), None)
            if next_backward is not None and next_backward == current:
                print(f"found backward repeat {next_backward}, sequence = {sequence}")
                partition.repeat_backward.remove(next_backward)
                previous_forward = max([i for i in partition.repeat_forward if i < current])
                print(f"found forward repeat {previous_forward}, sequence = {sequence}")
                current = previous_forward
                ending_one_candidates = [i for i in partition.ending_one
                                            if i < next_backward and i > previous_forward]
                if ending_one_candidates:
                    jump_start = ending_one_candidates[0]
                    jump_stop = min([i for i in partition.ending_two if i > jump_start])
                    print(f"found jump inside repeat at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                continue

            # Case 2 : if we reach a memorized jump
            if current in jumps:
                current = jumps[current]
                continue
            # Case 5 : else simply read next one
            current += 1

        return sequence

    def is_valid(self):
        return True
