#!/usr/bin/python3
# -*- coding: Utf-8 -*








#test if our function send a sentence in lower case
def test_in_lower_case():
    pa = script.SentenceParse()
    x = "TEST"
    assert pa.in_lower_case(x) == "test"



def test_deleting_stop_words():
    useless_sentence = "afin ailleurs openclassroom"
    pa = script.SentenceParse()
    assert pa.deleting_stop_words(useless_sentence) == "openclassroom"


def test_deleting_special():
    special_sentence = "openclassroom,paris:france"
    pa = script.SentenceParse()
    assert pa.deleting_special(special_sentence) == "openclassroom paris france"


def test_deleting_several_spaces():
    sentence = "openclassroom  paris"
    pa =  script.SentenceParse()
    assert pa.deleting_several_spaces(sentence) == "openclassroom paris"


def test_returning_cleaned_sentence():
    sentence = "TEST,openclassroom ailleurs:hamdi"
    pa = script.SentenceParse()
    assert pa.returning_cleaned_sentence(sentence) == "test openclassroom hamdi"
