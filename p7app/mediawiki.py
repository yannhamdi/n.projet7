#!/usr/bin/python3
# -*- coding: Utf-8 -*
""" module that deal with requesting with the wikipedia api"""

from random import randint

import requests

class MediaWikiApi:
    """class that calls wikipedia api"""
    def __init__(self):
        self.url_2 = "https://fr.wikipedia.org/w/api.php"
        self.pageid = 0
        self.dictionnary_search = []
        self.extract = ""
        self.fullurl = ""
        self.result = ""
        self.result2 = ""
        self.response2 = ""
    def search_around(self, lat, lng):
        """function that tells us stories about a place near"""
        params = {
            "format": "json", # format of the response
            "action": "query", # action requiered
            "list": "geosearch", # research method
            # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gsradius": 10000,
            # coordonnées GPS séparées par une barre verticale
            "gscoord": f"{lat}|{lng}"
                }
        response = requests.get(self.url_2, params=params)
        if (response.status_code == 200):
            geosearch_data = response.json()
            nbre = len(geosearch_data["query"]["geosearch"])
            choice = ((randint(0, nbre)) - 1)
            self.pageid = geosearch_data["query"]["geosearch"][choice]['pageid']
            return self.pageid
        else:
            print("La requête a donné un statut d'erreur")
            self.result = "error"
            return self.result
    def search_pageid(self, pageid):
        """method that look nearby our place"""
        self.pageid = pageid
        param = {
            "format": "json", # format de la réponse
            "action": "query", # action à effectuer
            "prop": "extracts|info", # Choix des propriétés pour les pages requises
            # gives us urls
            "inprop": "url",
            "exchars": 500, # Nombre de caractères à retourner
            "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
            "pageids": self.pageid
        }
        self.response2 = requests.get(self.url_2, params=param)
        if (self.response2.status_code == 200):
            info_search = self.response2.json()
            self.extract = info_search['query']['pages'][str(self.pageid)]['extract']
            self.fullurl = info_search['query']['pages'][str(self.pageid)]['fullurl']
            print("T'ai je déjà parler de ce que l'on pouvait trouver \
                    dans les alentours de ce que tu me demandes?")
            self.dictionnary_search.append(self.extract)
            self.dictionnary_search.append(self.fullurl)
            return self.dictionnary_search
        else:
            print("La requête a donné un statut d'erreur")
            self.result2 = "error"
            return self.result2

def main():
    po = MediaWikiApi()
    pageid = 450439
    po.search_pageid(pageid)
main()
