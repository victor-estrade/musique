# -*- coding: utf-8 -*-
import os
import logging
import json

from pathfinder import DATA_DIR

def load_situation(i:int):
    fname = os.path.join(DATA_DIR, f"situation{i}.json")
    with open(fname, "r") as file :
        data = json.load(file)
    return data
