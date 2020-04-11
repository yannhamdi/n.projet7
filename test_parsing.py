#!/usr/bin/python3
# -*- coding: Utf-8 -*

import parsing as script







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
    # Definition du mock pour requests.get()
    class MockGet:
        def __init__(self,url):
            pass

        def json(self):
	            return {
	                  "results": [{"formatted_address": FAKE_ADDRESS, "geometry": { "location":
	                  { "lat": FAKE_LAT, "lng": FAKE_LNG}

	                  }}]
	            }
	# Definition du test pour search_around()
    def mock_search_around(self, lat, lng):
        pass
    # patching the request.get pour simuler l'appel de l'api
monkeypatch.setattr("parsing.requests.get", MockGet)
    # patching de SentenceParse.search_around pour eviter de tester deux methondes en mêmme temps. We replace it with a method which doesnt do anything
monkeypatch.setattr("parsing.SentenceParse.search_around", mock_search_around)
    # we call the method sending_to_api
    pa = script.SentenceParse()
    pa.sending_to_api("petit test avec mock")
    # Assert on the result's sending_to_api method
    assert pa.address == FAKE_ADDRESS

