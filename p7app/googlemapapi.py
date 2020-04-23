#!/usr/bin/python3
# -*- coding: Utf-8 -*
import requests

import json

from p7app.config import keyapi






class TreatingApi:
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.url_1 = "https://maps.googleapis.com/maps/api/geocode/json?address="
        
        
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        self.sentence = str(sentence)    
        self.url= self.url_1 + self.sentence + "&key=" + keyapi
        self.response = requests.get(self.url)
        try:
            self.response_json = self.response.json()
            self.address = (self.response_json["results"][0]["formatted_address"])
            self.lat = (self.response_json["results"][0]["geometry"]["location"]["lat"])  #we select our latitude
            self.lng = (self.response_json["results"][0]["geometry"]["location"]["lng"]) #we select our longitude
            print(self.address)
        except:
            print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de chose mais sur ce coup je ne vois pas ce que tu veux dire.")




if __name__ == "__main__":
    main()

    