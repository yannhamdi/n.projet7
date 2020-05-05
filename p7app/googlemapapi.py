#!/usr/bin/python3
# -*- coding: Utf-8 -*
"module for google map api"
import requests

from p7app.settings import keyapi


class TreatingApi:
    "class that will send a request to google map api"
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.url_1 = "https://maps.googleapis.com/maps/api/geocode/json?parameters"
        self.sentence = ""
        self.response = ""
        self.url = ""
        self.address = ""
        self.response_json = ""
        self.lat = 0
        self.lng = 0
        self.dictio_coord = []
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        self.sentence = str(sentence)
        self.params = {"address": self.sentence, "key": keyapi}
        self.response = requests.get(self.url_1, params=self.params)
        try:
            self.response_json = self.response.json()
            #we select the address
            self.address = (self.response_json["results"][0]["formatted_address"])
            #we select our latitude
            self.lat = (self.response_json["results"][0]["geometry"]["location"]["lat"])
            #we select our longitude
            self.lng = (self.response_json["results"][0]["geometry"]["location"]["lng"])
            self.dictio_coord.append(self.address)
            self.dictio_coord.append(self.lat)
            self.dictio_coord.append(self.lng)
            return self.dictio_coord
        except:
            print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de \
                chose mais sur ce coup je ne vois pas ce que tu veux dire.")

def main():
    po =TreatingApi()
    text = "openclassroom"
    po.sending_to_api(text)
if __name__ == "__main__":
    main()
 