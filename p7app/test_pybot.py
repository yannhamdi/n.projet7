#!/usr/bin/python3
# -*- coding: Utf-8 -*

from p7app import parsing

from p7app import pybot

from p7app import mediawiki



def test_transformed_gps_into_json_results():
    gps = pybot.PapyBot()
    lat = 48
    lng = 50
    assert gps.transformed_gps_into_json_results(lat,lng) == {"latitude": lat , "longitude": lng}

def test_transformed_pageid_into_json(monkeypatch):
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
	        return {
                    'query': {'geosearch':[{
                        'pageid': '9845754'}]}}
    monkeypatch.setattr("requests.get", MockReturn)
    pi = mediawiki.MediaWikiApi()
    pi.search_around(F_LAT, F_LNG)
    assert pi.pageid == '9845754'
    