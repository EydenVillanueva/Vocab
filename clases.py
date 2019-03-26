'''
Libraries
'''

from peewee import *
from googletrans import Translator
from PyDictionary import PyDictionary

'''
Classes
'''

db = SqliteDatabase('vocab.db')

class Word(Model):
    'Class for save definitions, spanish translations etc.'
    word = CharField()
    translation = CharField()
    definition_e = CharField(null=True)
    definition_s = CharField(null=True)
    translator = Translator()
    
    class Meta:
        database = db #This model uses the 'vocab.db' database
    
    def translate(self, word):
        try:
            trans = self.translator.translate(word,dest='es')
            return trans.text
        except TypeError:
            pass
        return "The argument does not contrain any word\n"
                
    def displaySpanish(self):
        return self.translation + " -> " + self.definition_s
    
    def displayEnglish(self):
        return self.word + " -> " + self.definition_e 
    
    def getFullMeaning(self):
        dictionary = PyDictionary(self.word)
        meaning = dictionary.getMeanings()[self.word]
        return meaning
    
    def __str__(self):
        if(self.definition_e != None  and self.definition_s != None):
            return self.displayEnglish() + " \n" + self.displaySpanish()
        else:
            return self.word 

    def get_words(self):
        for word in Word.select():
            print("Word {}  translation {} ".format(word.word, word.translation))
    

class Synonym(Model):
    'Special class that make a relation between two words with the same definition'
    id_word = DeferredForeignKey('Word', null=True)
    id_synonym = DeferredForeignKey('Word', null=True)
    
    class Meta:
        database = db #This model uses the 'vocab.db' database    
        
        
        
#palabra = Word(word="prueba",translation="prueba",definition_e="prueba",definition_s="prueba")
