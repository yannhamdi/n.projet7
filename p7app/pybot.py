#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""module that deal with sending the answer to the web"""

import requests

from p7app import parsing

from p7app import googlemapapi

from p7app import mediawiki


class PapyBot():
    """class that will send all the informartion to our webpage"""
    def __init__(self):
        self.data_treated = {}
        self.result = ""
        self.gps_lat = 0
        self.gps_lng = 0
        self.pageid_for_js = 0
        self.info = ""
        self.url = ""
        self.lat = 0
        self.lng = 0
        self.gps_adress = ""
    
    def transformed_gps_into_json_results(self, sentence):
        """ we get our coordinates and adress"""
        sen = parsing.SentenceParse()
        sen.returning_cleaned_sentence(sentence)
        try:
            goo = googlemapapi.TreatingApi()
            goo.sending_to_api(sen.sentence)
            self.gps_lat = goo.lat
            self.gps_lng = goo.lng
            self.gps_adress = goo.address
        except requests.RequestException:
            self.result = "error"
            return self.result
    
    def transformed_pageid_into_json(self, lat, lng):
        """method that will put our page id into json"""
        self.lat = lat
        self.lng = lng
        try:
            media = mediawiki.MediaWikiApi()
            media.search_around(self.lat, self.lng)
            self.pageid_for_js = media.pageid
        except requests.RequestException:
            self.result = "error"
            return self.result
    def transformed_info_js(self, pageid):
        """method that gives informartiona et url"""
        try:
            super_media = mediawiki.MediaWikiApi()
            super_media.search_pageid(pageid)
            self.info = super_media.extract
            self.url = super_media.fullurl
        except requests.RequestException:
            self.result = "error"
            return self.result
    def returning_dictionnary(self, informartion, link_url, gps_adress, latitude, longitude):
        """method that return our dictionnary"""
        self.data_treated = {"addresse": gps_adress, "latitude": latitude,
                             "longitude": longitude, "inquiries":
                             informartion, "weblink":link_url}
        return self.data_treated
def  main():
    """we initlialize our functibn main"""
    if __name__ == '__main__':
        main()
