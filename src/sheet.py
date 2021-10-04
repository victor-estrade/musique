# -*- coding: utf-8 -*-
from enum import Enum
from dataclasses import dataclass
from dataclasses import field
from typing import List


class Symbols(Enum):
    # Sort in priority order !
    repeat_forward = 1
    forward = 1  # Alias
    repeat_backward = 2
    backward = 2 # Alias
    ending_one = 3
    ending_two = 4
    segno = 5
    dalsegno = 6
    dacapo = 7
    tocoda = 8
    coda = 9


@dataclass
class Sheet():
    mesures : List[List[Symbols]]

    @property
    def length(self):
        return len(self.mesures)

    def create_empty(length : int):
        """ Creates a sheet of given length with no symbols """
        mesures = [[] for _ in range(length)]
        new_empty_sheet = Sheet(mesures)
        return new_empty_sheet

    def from_situation(situation):
        lists = situation['lists']
        total_number_of_measures = situation['total_number_of_measures']
        new_sheet = Sheet.create_empty(total_number_of_measures)
        new_sheet.insert_repeat_forward_from_positions(lists['repeat_forward'])
        new_sheet.insert_repeat_backward_from_positions(lists['repeat_backward'])
        new_sheet.insert_ending_one_from_positions(lists['ending_one'])
        new_sheet.insert_ending_two_from_positions(lists['ending_two'])
        new_sheet.insert_segno_from_positions(lists['segno'])
        new_sheet.insert_dalsegno_from_positions(lists['dalsegno'])
        new_sheet.insert_dacapo_from_positions(lists['dacapo'])
        new_sheet.insert_tocoda_from_positions(lists['tocoda'])
        new_sheet.insert_coda_from_positions(lists['coda'])
        return new_sheet

    def insert_repeat_forward_from_positions(self, repeat_forward_positions):
        for position in repeat_forward_positions:
            self.mesures[position].append(Symbols.repeat_forward)

    def insert_repeat_backward_from_positions(self, repeat_backward_positions):
        for position in repeat_backward_positions:
            self.mesures[position].append(Symbols.repeat_backward)

    def insert_ending_one_from_positions(self, ending_one_positions):
        for position in ending_one_positions:
            self.mesures[position].append(Symbols.ending_one)

    def insert_ending_two_from_positions(self, ending_two_positions):
        for position in ending_two_positions:
            self.mesures[position].append(Symbols.ending_two)

    def insert_segno_from_positions(self, segno_positions):
        for position in segno_positions:
            self.mesures[position].append(Symbols.segno)

    def insert_dalsegno_from_positions(self, dalsegno_positions):
        for position in dalsegno_positions:
            self.mesures[position].append(Symbols.dalsegno)

    def insert_dacapo_from_positions(self, dacapo_positions):
        for position in dacapo_positions:
            self.mesures[position].append(Symbols.dacapo)

    def insert_tocoda_from_positions(self, tocoda_positions):
        for position in tocoda_positions:
            self.mesures[position].append(Symbols.tocoda)

    def insert_coda_from_positions(self, coda_positions):
        for position in coda_positions:
            self.mesures[position].append(Symbols.coda)

    def get(self, position : int) -> List[Symbols]:
        """ Get the mesure content at given position """
        # Simple accessor ... Should it be able to read and write ?
        return self.mesures[position]


@dataclass
class SheetReader():
    current_position : int = 1
    repeat_forward_stack : List[int] = field(default_factory=list)
    segno_stack : List[int] = field(default_factory=list)

    def read(self, sheet : Sheet) -> List[int]:
        safety = 1
        safety_stop = 100_000
        end = sheet.length
        sequence = []
        while self.current_position <= end and safety < safety_stop:
            safety += 1
            sequence.append(self.current_position)
            current_mesure = sheet.get(self.current_position)
            self.handle(current_mesure)

        return list(range(1, sheet.length+1))


    def handle(self, current_mesure):
        symbols = sorted(current_mesure)
        for symbol in current_mesure:
            break_flag = self.consume(symbol)
            if break_flag:
                break

    def consume(self, symbol):
        pass

    def consume_repeat_forward(self):
        pass
