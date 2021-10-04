# -*- coding: utf-8 -*-

from .loader import load_situation



def test_load_situation_1():
    sit_1 = load_situation(1)
    answer = {
    	"lists": {
    		"repeat_forward": [
    			1,
    			3
    		],
    		"repeat_backward": [
    			2,
    			6
    		],
    		"ending_one": [
    			4
    		],
    		"ending_two": [
    			7
    		],
    		"segno": [],
    		"dalsegno": [],
    		"dacapo": [],
    		"tocoda": [],
    		"coda": []
    	},
    	"total_number_of_measures": 8,
    	"valid": True,
    	"measure_sequence": [
    		1,
    		2,
    		1,
    		2,
    		3,
    		4,
    		3,
    		5,
    		6,
    		7,
    		8
    	]
    }
    assert sit_1 == answer
