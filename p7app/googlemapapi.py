#!/usr/bin/python3
# -*- coding: Utf-8 -*
"module for google map api"


import os

import requests

class TreatingApi:
    "class that will send a request to google map api"
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.dictio_coord = []
        self.address = ""
        self.lat = 0
        self.lng = 0
        self.result = ""
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        sentence = str(sentence)
        url_1 = "https://maps.googleapis.com/maps/api/geocode/json?parameters"
        params = {"address": sentence, "key": os.environ.get("KEY_API")}
        response = requests.get(url_1, params=params)
        if response.status_code == 200:
            response_json = response.json()
            #we select the address
            self.address = (response_json["results"][0]["formatted_address"])
            #we select our latitude
            self.lat = (response_json["results"][0]["geometry"]["location"]["lat"])
            #we select our longitude
            self.lng = (response_json["results"][0]["geometry"]["location"]["lng"])
            self.dictio_coord.append(self.address)
            self.dictio_coord.append(self.lat)
            self.dictio_coord.append(self.lng)
            return self.dictio_coord
        print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de \
            chose mais sur ce coup je ne vois pas ce que tu veux dire.")
        self.result = "error"
        return self.result
def main():
    """we initialize our main function"""
    if __name__ == '__main__':
        main()
