#!/usr/bin/env python3

def return_evens(num_list):
    return  [i for i in num_list if i % 2 == 0]
    pass

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list if sentence_list]
    pass