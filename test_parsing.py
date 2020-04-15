#!/usr/bin/python3
# -*- coding: Utf-8 -*

import parsing as script

import requests








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


def test_sending_to_api_handles_correct_result(monkeypatch):
    FAKE_ADDRESS = "adresse de test, 7 cite de paradis 75010 paris, openclassroom"
    FAKE_LAT = 49.0
    FAKE_LNG = 3.0
    # Defining the mock for requests.get()
    class MockGet:
        def __init__(self,url):
            pass

        def json(self):
	            return {
	                  "results": [{"formatted_address": FAKE_ADDRESS, "geometry": { "location":
	                  { "lat": FAKE_LAT, "lng": FAKE_LNG}

	                  }}]
	}
    # patching the request.get to mock the api call
    monkeypatch.setattr("parsing.requests.get", MockGet)
    # we call the method sending_to_api
    pa = script.SentenceParse()
    pa.sending_to_api("petit test avec mock")
    # Assert on the result's sending_to_api method
    assert pa.address == FAKE_ADDRESS
    assert pa.lat == FAKE_LAT
    assert pa.lng == FAKE_LNG


def test_search_around_correct_result(monkeypatch):
    F_LAT = 49.0
    F_LNG = 3.0
    class MockReturn():
        def __init__(self, url, params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 10000, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{F_LAT}|{F_LNG}" # coordonnées GPS séparées par une barre verticale
                }):
            pass

        def json(self):
	            return {"results": 'query':
	             {'geosearch': [{'title':'openclassroom'}]}}
    monkeypatch.setattr("parsing.requests.get", MockReturn)
    pa = script.SentenceParse()
    pa.search_around(F_LAT, F_LNG)
    assert pa.title == 'openclassroom'




