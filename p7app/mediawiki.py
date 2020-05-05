#!/usr/bin/python3
# -*- coding: Utf-8 -*
""" module that deal with requesting with the wikipedia api"""

from random import randint

import requests

class MediaWikiApi:
    """class that calls wikipedia api"""
    def __init__(self):
        self.url_2 = "https://fr.wikipedia.org/w/api.php"
        self.params = {}
        self.param = {}
        self.response = ""
        self.geosearch_data = ""
        self.pageid = 0
        self.dictionnary_search = []
        self.response2 = ""
        self.info_search = ""
        self.extract = ""
        self.fullurl = ""
        self.nbre = 0
        self.choice = 0
    def search_around(self, lat, lng):
        """function that tells us stories about a place near"""
        self.params = {
            "format": "json", # format of the response
            "action": "query", # action requiered
            "list": "geosearch", # research method
            # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gsradius": 10000,
            # coordonnées GPS séparées par une barre verticale
            "gscoord": f"{lat}|{lng}"
                }
        self.response = requests.get(self.url_2, params=self.params)
        try:
            self.geosearch_data = self.response.json()
            self.nbre = len(self.geosearch_data["query"]["geosearch"])
            self.choice = ((randint(0, self.nbre)) - 1)
            self.pageid = self.geosearch_data["query"]["geosearch"][self.choice]['pageid']
            return self.pageid
        except:
            print("La requête a donné un statut d'erreur")
    def search_pageid(self, pageid):
        """method that look nearby our place"""
        self.pageid = pageid
        self.param = params = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            # gives us urls
            "inprop": "url",
            "exchars": 500, # Nombre de caractères à retourner
            "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": self.pageid
        }
        try:
            self.response2 = requests.get(self.url_2, params=self.param)
            self.info_search = self.response2.json()
            self.extract = self.info_search['query']['pages'][str(self.pageid)]['extract']
            self.fullurl = self.info_search['query']['pages'][str(self.pageid)]['fullurl']
            print("T'ai je déjà parler de ce que l'on pouvait trouver \
                    dans les alentours de ce que tu me demandes?")
            self.dictionnary_search.append(self.extract)
            self.dictionnary_search.append(self.fullurl)
            return self.dictionnary_search
        except:
            print("La requête a donné un statut d'erreur")
if __name__ == "__main__":
    main()
