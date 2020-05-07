#!/usr/bin/python3
# -*- coding: Utf-8 -*

from p7app import parsing

from p7app import pybot

from p7app import mediawiki



def test_transformed_gps_into_json_results():
    gps = pybot.PapyBot()
    sentence = "OPENCLASSROOM"
    adresse = "fausse adresse"
    lat = 48
    lng = 50
    par = parsing.SentenceParse()
    assert par.returning_cleaned_sentence(sentence) == "openclassroom"   
    def test_sending_to_api_handles_correct_result(monkeypatch):
        class MockGet:
            def __init__(self,url):
                self.status_code = 200

            def json(self):
	            return {
	                  "results": [{"formatted_address": adresse, "geometry": { "location":
	                  { "lat": lat, "lng": lng}

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
    def test_sending_to_api_handles_error_result(monkeypatch):
        class MockGet:
            def __init__(self,url):
                self.status_code = 300
                self.status_code >300

            def json(self):
                return "error"
        # patching the request.get to mock the api call
        monkeypatch.setattr("requests.get", MockGet)
        # we call the method sending_to_api
        pi = googlemapapi.TreatingApi()
        pi.sending_to_api("petit test avec mock")
        # Assert on the result's sending_to_api method
        assert pi.result == "error"


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
            self.status_code = "Response [200]"

        def json(self):
	        return {
                    'query': {'geosearch':[{
                        'pageid': '9845754'}]}}
    monkeypatch.setattr("requests.get", MockReturn)
    pi = mediawiki.MediaWikiApi()
    pa = pybot.PapyBot()
    pa.transformed_pageid_into_json(59.79685,34.0984)
    assert pa.pageid_for_js == '9845754'

def test_transformed_pageid_into_json_error(monkeypatch):
    F_LAT = 49.0
    F_LNG = 3.0
    class Mock():
        def __init__(self, url, params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 10000, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{F_LAT}|{F_LNG}" # coordonnées GPS séparées par une barre verticale
                }):
            self.status_code = "Response [300]"
            self.status_code != "Response [200]"
        def json(self):
            return "error"
    monkeypatch.setattr("requests.get", Mock)
    me = mediawiki.MediaWikiApi()
    pa = pybot.PapyBot()
    pa.transformed_pageid_into_json(59.79685,34.0984)
    assert pa.result == "error"

   

def test_transformed_info_js(monkeypatch):
    pageid = 56876948
    class MockReturning():
        def __init__(self, url, params = {"format": "json", # format de la réponse
                     "action": "query", # action à effectuer
                       "prop": "extracts|info", # Choix des propriétés pour les pages requises
                       "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
                      "exchars": 500, # Nombre de caractères à retourner
                       "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
                       "pageids": pageid}):
            self.status_code = "Response [200]"
        def json(self):
                return{ 'query': {'pages': {str(pageid): {'extract':'ceci est un mock api',
                                       'fullurl': 'https://fr.wikipedia.org/wiki/Academy_of_Art_University'}}

            }}
    monkeypatch.setattr("requests.get", MockReturning)
    pi = mediawiki.MediaWikiApi()
    pe = pybot.PapyBot()
    pe.transformed_info_js(pageid)
    assert pe.info == 'ceci est un mock api'
    assert pe.url == 'https://fr.wikipedia.org/wiki/Academy_of_Art_University'
def test_transformed_info_js_error(monkeypatch):
    pageid = 56876948
    class MockReturning():
        def __init__(self, url, params = {"format": "json", # format de la réponse
                     "action": "query", # action à effectuer
                       "prop": "extracts|info", # Choix des propriétés pour les pages requises
                       "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
                      "exchars": 500, # Nombre de caractères à retourner
                       "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
                       "pageids": pageid}):
            self.status_code = "Response [300]"
            self.status_code != "Response [200]"
        def json(self):
            return "error"
    monkeypatch.setattr("requests.get", MockReturning)
    pi = mediawiki.MediaWikiApi()
    pe = pybot.PapyBot()
    pe.transformed_info_js(pageid)
    assert pe.return_result == "error"
def test_returning_dictionnary():
    final = pybot.PapyBot()
    adresses = "ceci est une adresse"
    lati= 34.9090
    longi = 56.6059
    info = "ceci est un test"
    url = "https:XXXXXXXXXXXX.fr"
    assert final.returning_dictionnary(info, url, adresses, lati, longi) == {"addresse": adresses, "latitude": lati, "longitude": longi, "inquiries": info, "weblink": url }


