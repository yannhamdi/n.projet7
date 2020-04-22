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
        def __init__(self,url):
            pass

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
    assert pi.address == FAKE_ADDRESS
    assert pi.lat == FAKE_LAT
    assert pi.lng == FAKE_LNG
