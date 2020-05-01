#!/usr/bin/python3
# -*- coding: Utf-8 -*
"module that deal with sending the answer to the web"

from p7app import parsing

from p7app import googlemapapi

from p7app import mediawiki




class PapyBot():
    "class that will send all the informartion to our webpage"
    def __init__(self):
        self.data_treated = {}
    def transformed_gps_into_json_results(self, sentence):
        self.sentence = sentence
        sen = parsing.SentenceParse()
        sen.returning_cleaned_sentence(self.sentence)
        goo = googlemapapi.TreatingApi()
        goo.sending_to_api(sen.sentence)
        self.gps_lat = goo.lat
        self.gps_lng = goo.lng
        self.gps_adress = goo.address
    def transformed_pageid_into_json(self, lat, lng):
        "method that will put our page id into json"
        self.lat = lat
        self.lng = lng
        media = mediawiki.MediaWikiApi()
        media.search_around(lat, lng)
        self.pageid_for_js = media.pageid
    def transformed_info_js(self, pageid):
        "method that gives informartiona et url"
        self.pageidjs = pageid
        super_media = mediawiki.MediaWikiApi()
        super_media.search_pageid(self.pageidjs)
        self.info = super_media.extract
        self.url = super_media.fullurl  
    def returning_dictionnary(self, informartion, link_url, gps_adress, latitude, longitude):
        "method that return our dictionnary"
        self.gps_adress = gps_adress
        self.latitude = latitude
        self.longitude = longitude
        self.informartion = informartion
        self.link_url = link_url
        self.data_treated = {"addresse": self.gps_adress, "latitude": self.latitude, 
                        "longitude": self.longitude , "inquiries": self.informartion, "weblink": self.link_url}
        return self.data_treated
        
if __name__ == "__main__":
    main()