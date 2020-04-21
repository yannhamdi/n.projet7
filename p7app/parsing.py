#!/usr/bin/python3
# -*- coding: Utf-8 -*

import requests

import json

from pprint import pprint

from p7app.config import keyapi

from random import *


class SentenceParse:

    def __init__(self):
        "we initialize the attribute stop words"
        self.stop_words = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]

        
    def in_lower_case(self, sentence):  
        "function that put the strings in lower case"
        self.sentence =str(sentence)
        self.sentence = self.sentence.lower() 
        return self.sentence
        
    def deleting_stop_words(self,sentence):
        "function that deletes the stop words"
        self.uncleaned_sentence = []
        self.sentence = str(sentence)
        for word in self.sentence.split():
            if word in self.stop_words:
                pass
            elif word == " ":
                pass
            else:
                self.uncleaned_sentence.append(word)
        self.new_sentence = " ".join(self.uncleaned_sentence)
        return(self.new_sentence)

    

    def deleting_special(self, sentence):
        "function that deletes the special character"
        self.sentence = str(sentence)
        intab = ",:?;.-"
        outtab ="      "
        trantab = str.maketrans(intab, outtab)
        self.sentence = self.sentence.translate(trantab)
        return self.sentence
     
        
    def deleting_several_spaces(self, sentence):
        "function that deletes spaces in case of double spaces"
        self.sentence = str(sentence)
        self.sentence = self.sentence.replace("  ", " ")
        return(self.sentence)

    def returning_cleaned_sentence(self, sentence):
        "fucntion that return the sentence cleaned"
        self.sentence = str(sentence)
        self.sentence = self.in_lower_case(self.sentence)
        self.sentence = self.deleting_special(self.sentence)
        self.sentence = self.deleting_stop_words(self.sentence)
        self.sentence = self.deleting_several_spaces(self.sentence)
        return(self.sentence)
    
class TreatingApi:
    def __init__(self):
        "we initialize what is necessary for our requests"
        self.url_1 = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.url_2 = "https://fr.wikipedia.org/w/api.php"
        
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        self.sentence = str(sentence)    
        self.url= self.url_1 + self.sentence + "&key=" + keyapi
        self.response = requests.get(self.url)
        try:
            self.response_json = self.response.json()
            self.address = (self.response_json["results"][0]["formatted_address"])
            self.lat = (self.response_json["results"][0]["geometry"]["location"]["lat"])
            self.lng = (self.response_json["results"][0]["geometry"]["location"]["lng"])
            print(self.address)
        except:
            print("Désolé mon petit loup je sais que je suis vieux et connais énormèment de chose mais sur ce coup je ne vois pas ce que tu veux dire.")

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
    "exchars": 1200, # Nombre de caractères à retourner
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
def main():
    ff = SentenceParse()
    text = "OPENCLASSROOM"
    ff.returning_cleaned_sentence(text)
    fa = TreatingApi()
    fa.sending_to_api(ff.sentence)
    fa.search_around(fa.lat, fa.lng)
    fa.search_pageid(fa.pageid)
main()