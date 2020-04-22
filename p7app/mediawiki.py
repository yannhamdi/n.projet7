#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests

import json

from random import randint



class MediaWikiApi:
    "class that calls wikipedia api"
    def __init__(self):
        self.url_2 = "https://fr.wikipedia.org/w/api.php"


    def search_around(self, lat, lng):
        "function that tells us stories about a place near"
        self.params = {
            "format": "json", # format de la réponse
            "action": "query", # action à réaliser
            "list": "geosearch", # méthode de recherche
            "gsradius": 10000, # rayon de recherche autour des coordonnées GPS fournies (max 10'000 m)
            "gscoord": f"{lat}|{lng}" # coordonnées GPS séparées par une barre verticale
                }
        self.response = requests.get(self.url_2, params = self.params)
        try:
            self.geosearch_data = self.response.json()
            self.nbre = len(self.geosearch_data["query"]["geosearch"])
            self.choice = ((randint(0, self.nbre)) - 1)
            self.pageid = self.geosearch_data["query"]["geosearch"][self.choice]['pageid']    
        except:
            print("La requête a donné un statut d'erreur")      
    def search_pageid(self, pageid):
        "method that look nearby our place" 
        self.pageid = pageid
        self.param = params = {
    "format": "json", # format de la réponse
    "action": "query", # action à effectuer
    "prop": "extracts|info", # Choix des propriétés pour les pages requises
    "inprop": "url", # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
    "exchars": 500, # Nombre de caractères à retourner
    "explaintext": 1, # Renvoyer du texte brut (éliminer les balises de markup)
    "pageids": self.pageid
}
        try:
            self.response2 = requests.get(self.url_2, params = self.param)
            self.info_search = self.response2.json()
            self.extract = self.info_search['query']['pages'][str(self.pageid)]['extract']
            self.fullurl = self.info_search['query']['pages'][str(self.pageid)]['fullurl']
            print("T'ai je déjà parler de ce que l'on pouvait trouver dans les alentours de ce que tu me demandes?")
            print(self.extract)
            print(self.fullurl)
        except:
            print("La requête a donné un statut d'erreur")



def main() :
    kk = MediaWikiApi()
    kk.search_around(48.12233,13.54565)
    print(kk.pageid)
main()