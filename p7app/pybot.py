#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests

import json

from p7app.googlemapapi import 


class Papybot():
    "class that will send all the informartion to our webpage"
    def __init__(self):
        self.sending_gps_coordinate = {}
        
    def transformed_data_into_json_results(self, lat, lng):
        self.a = lat
        self.b = lng
        "we are going to encode our answers from others classes to an answers which can be treated by js"
        self.sending_gps_coordinate = {"latitude": self.a , "longitude": self.b}