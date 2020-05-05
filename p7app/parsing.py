#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""module that will parses the sentence"""

from p7app.settings import stop_words

class SentenceParse:
    """our class that will creates all the methods needed for parsing the sentence"""
    def __init__(self):
        "we initialize the attribute stop words"
        self.uncleaned_sentence = []
        self.sentence = " "
        self.new_sentence = " "
    def in_lower_case(self, sentence):
        "function that put the strings in lower case"
        self.sentence = str(sentence)
        self.sentence = self.sentence.lower()
        return self.sentence
    def deleting_stop_words(self, sentence):
        """function that deletes the stop words"""
        self.sentence = str(sentence)
        for word in self.sentence.split():
            if word in stop_words:
                pass
            else:
                self.uncleaned_sentence.append(word)
        self.new_sentence = " ".join(self.uncleaned_sentence)
        return self.new_sentence
    def deleting_special(self, sentence):
        """function that deletes the special character"""
        self.sentence = str(sentence)
        intab = ",:?;.-"
        outtab = "      "
        trantab = str.maketrans(intab, outtab)
        self.sentence = self.sentence.translate(trantab)
        return self.sentence
    def deleting_several_spaces(self, sentence):
        """function that deletes spaces in case of double spaces"""
        self.sentence = str(sentence)
        self.sentence = self.sentence.replace("  ", " ")
        return self.sentence
    def returning_cleaned_sentence(self, sentence):
        """fucntion that return the sentence cleaned"""
        self.sentence = str(sentence)
        self.sentence = self.in_lower_case(self.sentence)
        self.sentence = self.deleting_special(self.sentence)
        self.sentence = self.deleting_stop_words(self.sentence)
        self.sentence = self.deleting_several_spaces(self.sentence)
        return self.sentence
if __name__ == "__main__":
    main()
    