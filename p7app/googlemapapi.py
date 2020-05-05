#!/usr/bin/python3
# -*- coding: Utf-8 -*
"module for google map api"
import requests

from p7app.settings import keyapi


class TreatingApi:
    "class that will send a request to google map api"
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.dictio_coord = []
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        sentence = str(sentence)
        url_1 = "https://maps.googleapis.com/maps/api/geocode/json?parameters"
        params = {"address": sentence, "key": keyapi}
        response = requests.get(url_1, params=params)
        try:
            response_json = response.json()
            #we select the address
            address = (response_json["results"][0]["formatted_address"])
            #we select our latitude
            lat = (response_json["results"][0]["geometry"]["location"]["lat"])
            #we select our longitude
            lng = (response_json["results"][0]["geometry"]["location"]["lng"])
            self.dictio_coord.append(address)
            self.dictio_coord.append(lat)
            self.dictio_coord.append(lng)
            return self.dictio_coord
        except:
            print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de \
                chose mais sur ce coup je ne vois pas ce que tu veux dire.")
if __name__ == "__main__":
    main()
 