#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests

import json
from p7app import googlemapapi






def test_sending_to_api_handles_correct_result(monkeypatch):
    FAKE_ADDRESS = "adresse de test, 7 cite de paradis 75010 paris, openclassroom"
    FAKE_LAT = 49.0
    FAKE_LNG = 3.0
    # Defining the mock for requests.get()
    class MockGet:
        def __init__(self,url, params = {"address": FAKE_ADDRESS, "key": 9584833}):
            self.status_code = 200
            

        def json(self):
	            return {
	                  "results": [{"formatted_address": FAKE_ADDRESS, "geometry": { "location":
	                  { "lat": FAKE_LAT, "lng": FAKE_LNG}

	                  }}]
	}
    # patching the request.get to mock the api call
    monkeypatch.setattr("requests.get", MockGet)
    # we call the method sending_to_api
    pi = googlemapapi.TreatingApi()
    pi.sending_to_api("petit test avec mock")
    # Assert on the result's sending_to_api method
    assert pi.dictio_coord == [FAKE_ADDRESS, FAKE_LAT, FAKE_LNG]

def test_sending_to_api_for_error(monkeypatch):
    """ we test the exceptions"""
    status_code = 300
    RESULTS = "error"
    class Mockget:
        def __init__(self, url,params):
            self.status_code = status_code
            self.status_code > 200
        def json(self):
            return RESULTS
    monkeypatch.setattr("requests.get", Mockget)
    mo = googlemapapi.TreatingApi()
    mo.sending_to_api("petit test erreur")
    assert mo.result == RESULTS