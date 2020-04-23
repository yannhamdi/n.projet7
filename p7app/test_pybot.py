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
    pa = pybot.PapyBot()
    pa.transformed_pageid_into_json(59.79685,34.0984)
    assert pa.pageid_for_js == '9845754'
    

def test_transformed_info_js(monkeypatch):
    "we mock our method search_page_id"
    pageid = 56876948
    class MockReturning():
        def __init__(self, url, params = {"format": "json", # format de la réponse
                     "action": "query", # action à effectuer
                       "prop": "extracts|info", # Choix des propriétés pour les pages requises
                       "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
                      "exchars": 500, # Nombre de caractères à retourner
                       "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
                       "pageids": pageid}):
            pass
        def json(self):
                return{ 'query': {'pages': {str(pageid): {'extract':'ceci est un mock api',
                                       'fullurl': 'https://fr.wikipedia.org/wiki/Academy_of_Art_University'}}

            }}
    monkeypatch.setattr("requests.get", MockReturning)
    pi = mediawiki.MediaWikiApi()
    pi.search_pageid(pageid)
    assert pi.extract == 'ceci est un mock api'
    assert pi.fullurl == 'https://fr.wikipedia.org/wiki/Academy_of_Art_University'