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
                self.gps_adress = adresse
                self.gps_lat = lat
                self.gps_lng = lng
            def sending_to_api(self, sentence):
                pass

        monkeypatch.setattr("p7app.googlemapapi.TteatingApi", MockGet)
        po = pybot.PapyBot()
        po.transformed_gps_into_json("sentence")
        assert po.gps_lat == lat
        assert po.gps_lng == lng
        assert po.gps_adress == adresse

def test_transformed_pageid_into_json(monkeypatch):
    pageid = 4545
    FAKE_LAT = 50
    FAKE_LNG = 45
    class MockReturn():
        def __init__(self):
            self.pageid = pageid
            self.lat = FAKE_LAT
            self.lng = FAKE_LNG
        def search_around(self, lat, lng):
            pass
    monkeypatch.setattr("p7app.mediawiki.MediaWikiApi", MockReturn)
    pl = pybot.PapyBot()
    pl.transformed_pageid_into_json(FAKE_LAT, FAKE_LNG)
    assert pl.pageid_for_js == pageid
def test_transformed_info_js(monkeypatch):
    """mock for our method transformed info js"""  
    extract = "ceci est un mock api"
    fullurl = "mock full url"
    class MockWiki():
        def __init__(self):
            self.extract = extract
            self.fullurl = fullurl
        def search_pageid(self, pageid):
            pass
    monkeypatch.setattr("p7app.mediawiki.MediaWikiApi", MockWiki)
    pe = pybot.PapyBot()
    pe.transformed_info_js(1)
    assert pe.info == extract
    assert pe.url == fullurl
def test_returning_dictionnary():
    final = pybot.PapyBot()
    adresses = "ceci est une adresse"
    lati= 34.9090
    longi = 56.6059
    info = "ceci est un test"
    url = "https:XXXXXXXXXXXX.fr"
    assert final.returning_dictionnary(info, url, adresses, lati, longi) == {"addresse": adresses, "latitude": lati, "longitude": longi, "inquiries": info, "weblink": url }


