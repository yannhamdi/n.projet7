#!/usr/bin/python3
# -*- coding: Utf-8 -*
import requests

import json

from random import randint

from p7app import parsing

from p7app import googlemapapi

from p7app import mediawiki




class PapyBot():
    "class that will send all the informartion to our webpage"
    def __init__(self):
        self.sending_gps_coordinate = {}
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
        "we are going to encode our answers from others classes to an answers which can be treated by js"
        self.sending_gps_coordinate = {"addresse": self.gps_adress, "latitude": self.gps_lat , "longitude": self.gps_lng}
        return self.sending_gps_coordinate


    def transformed_pageid_into_json(self, lat, lng):
        "method that will put our page id into json"
        self.lat = lat
        self.lng = lng
        ap = mediawiki.MediaWikiApi()
        ap.search_around(lat, lng)
        self.pageid_for_js = ap.pageid
    
    def transformed_info_js(self, pageid):
        self.pageidjs = pageid
        ab = mediawiki.MediaWikiApi()
        ab.search_pageid(self.pageidjs)
        self.info = ab.extract
        self.url = ab.fullurl  

    def returning_dictionnary(self, informartion, link_url):
        self.informartion = informartion
        self.link_url = link_url
        self.data_treated = {"inquiries": self.informartion, "web link": self.link_url }
        return self.data_treated
        
        
 
if __name__ == "__main__":
    main()