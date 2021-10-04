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
                # Find ending_ones to memorize jumps
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

            # Case 3 : if we reach a dal segno
            next_dalsegno = next(iter(partition.dalsegno), None)
            if next_dalsegno is not None and next_dalsegno == current:
                print(f"found dal segno {next_dalsegno}, sequence = {sequence}")
                partition.dalsegno.remove(next_dalsegno)
                previous_segno = max([i for i in partition.segno if i < current])
                print(f"found segno {previous_segno}, sequence = {sequence}")
                current = previous_segno
                # Find coda to memorize jumps
                tocoda_candidates = [i for i in partition.tocoda
                                            if i < next_dalsegno and i > previous_segno]
                if tocoda_candidates:
                    jump_start = tocoda_candidates[0]
                    jump_stop = min([i for i in partition.coda if i > jump_start])
                    print(f"found jump inside dalsegno at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                continue

            # Case 4 : if we reah a da capo
            next_dacapo = next(iter(partition.dacapo), None)
            if next_dacapo is not None and next_dacapo == current:
                print(f"found da capo {next_dacapo}, sequence = {sequence}")
                partition.dacapo.remove(next_dacapo)
                current = 1
                # Find coda to memorize jumps
                tocoda_candidates = [i for i in partition.tocoda
                                            if i < next_dacapo]
                if tocoda_candidates:
                    jump_start = tocoda_candidates[0]
                    jump_stop = min([i for i in partition.coda if i > jump_start])
                    print(f"found jump inside dalsegno at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                continue

            # Case 5 : else simply read next one
            current += 1

        return sequence

    def is_valid(self):
        return True
