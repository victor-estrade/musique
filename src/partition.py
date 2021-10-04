# -*- coding: utf-8 -*-
import copy
import logging

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

    def first_backward(self):
        """ Returns the first repeat_backward position or None if nothing is found. """
        return next(iter(self.repeat_backward), None)

    def first_dalsegno(self):
        """ Returns the first dalsegno position or None if nothing is found. """
        return next(iter(self.dalsegno), None)

    def first_dacapo(self):
        """ Returns the first dacapo position or None if nothing is found. """
        return next(iter(self.dacapo), None)

    def previous_forward_from(self, position):
        """ Returns the first repeat_forward position previous to given position """
        return max([i for i in self.repeat_forward if i < position])

    def previous_segno_from(self, position):
        """ Returns the first segno position previous to given position """
        return max([i for i in self.segno if i < position])

    def find_ending_one_between(self, begin, end):
        """ Returns the list of ending_one position between begin and end """
        return [i for i in self.ending_one if begin < i and i < end]

    def find_tocoda_between(self, begin, end):
        """ Returns the list of tocoda position between begin and end """
        return [i for i in self.tocoda if begin < i and i < end]

    def next_ending_two_from(self, position):
        """ Returns the first repeat_forward position previous to given position """
        return min([i for i in self.ending_two if i > position])

    def next_coda_from(self, position):
        """ Returns the first repeat_forward position previous to given position """
        return min([i for i in self.coda if i > position])


    def measure_sequence(self):
        partition = copy.deepcopy(self)
        safety = 1
        safety_stop = 100_000
        current = 1
        next_backward = partition.first_backward()
        next_dalsegno = partition.first_dalsegno()
        next_dacapo = partition.first_dacapo()
        end = self.total_number_of_measures
        sequence = []
        jumps = {}  # Forward jumps -> ending and coda founds during repeats and dalsegno
        while current <= end and safety < safety_stop:
            safety += 1
            sequence.append(current)
            print(f"iter = {safety}, sequence = {sequence}")

            # Case 1 : if we reach an unused backward
            if next_backward is not None and next_backward == current:
                print(f"found backward repeat {current}, sequence = {sequence}")
                previous_forward = partition.previous_forward_from(current)
                print(f"found forward repeat {previous_forward}, sequence = {sequence}")
                ending_one_candidates = partition.find_ending_one_between(previous_forward, current)
                if ending_one_candidates:
                    jump_start = ending_one_candidates[0]
                    jump_stop = partition.next_ending_two_from(jump_start)
                    print(f"found jump inside repeat at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                current = previous_forward
                partition.repeat_backward.remove(next_backward)
                next_backward = partition.first_backward()
                continue

            # Case 2 : if we reach a memorized jump
            if current in jumps:
                current = jumps[current]
                continue

            # Case 3 : if we reach a dal segno
            if next_dalsegno is not None and next_dalsegno == current:
                print(f"found dal segno {current}, sequence = {sequence}")
                previous_segno = max([i for i in partition.segno if i < current])
                print(f"found segno {previous_segno}, sequence = {sequence}")
                tocoda_candidates = partition.find_tocoda_between(previous_segno, current)
                if tocoda_candidates:
                    jump_start = tocoda_candidates[0]
                    jump_stop = partition.next_coda_from(jump_start)
                    print(f"found jump inside dalsegno at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                current = previous_segno
                partition.dalsegno.remove(next_dalsegno)
                next_dalsegno = partition.first_dalsegno()
                continue

            # Case 4 : if we reah a da capo
            if next_dacapo is not None and next_dacapo == current:
                print(f"found da capo {next_dacapo}, sequence = {sequence}")
                tocoda_candidates = partition.find_tocoda_between(1, current)
                if tocoda_candidates:
                    jump_start = tocoda_candidates[0]
                    jump_stop = partition.next_coda_from(jump_start)
                    print(f"found jump inside dalsegno at {jump_start} going to {jump_stop}")
                    jumps[jump_start] = jump_stop
                current = 1
                partition.dacapo.remove(next_dacapo)
                next_dacapo = partition.first_dacapo()
                continue

            # Case 5 : else simply read next one
            current += 1

        return sequence

    def is_valid(self):
        return True
