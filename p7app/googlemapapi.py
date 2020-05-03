#!/usr/bin/python3
# -*- coding: Utf-8 -*
"module for google map api"
import requests

from p7app.settings import keyapi


class TreatingApi:
    "class that will send a request to google map api"
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.url_1 = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.sentence = ""
        self.response = ""
        self.url = ""
        self.address = ""
        self.response_json = ""
        self.lat = 0
        self.lng = 0
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        self.sentence = str(sentence)
        self.url = self.url_1 + self.sentence + "&key=" + keyapi
        self.response = requests.get(self.url)
        try:
            self.response_json = self.response.json()
            #we select the address
            self.address = (self.response_json["results"][0]["formatted_address"])
            #we select our latitude
            self.lat = (self.response_json["results"][0]["geometry"]["location"]["lat"])
            #we select our longitude
            self.lng = (self.response_json["results"][0]["geometry"]["location"]["lng"])
            return self.address
            return self.lat
            return self.lng
        except:
            print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de \
                chose mais sur ce coup je ne vois pas ce que tu veux dire.")
if __name__ == "__main__":
    main()
 