
#LIBRERIAS
from clases import *
from random_word import RandomWords
from ui_messages import *
import ast
import warnings
import sys
import os
import platform
import texttable as tt
from peewee import *
#VARIABLES GLOBALES
r = RandomWords()
word_of_the_day = ast.literal_eval(r.word_of_the_day())['word']
meaning = ast.literal_eval(r.word_of_the_day())['definations'][0]['text']
warnings.filterwarnings("ignore")

#METODOS DISPLAY
def displayWelcome():
    print(welcome[0])
    print(welcome[1].format(word_of_the_day,meaning))
    
def displayMenu(flag):
    if(flag):
        print(menu[0])
        print(menu[1].format("t - Translator","n - New Word","s - Show Words","d - Dictionary","q - Exit"))
    else:
        print(menu[1].format("t - Translator","n - New Word","s - Show Words","d - Dictionary", "q - Exit"))

def displayTranslate(flag):
    if(flag):
        print(menu_translate[0])
    else:
        print(menu_translate[1])

def displayDictionary():
    print(menu_dictionary[0])

def displayWord():
    print(menu_word[0])
def displayShow():
    print(menu_show[0])
#METODOS SUBMENUS
def translate():
    displayTranslate(True)
    while True:
        user_input = str(input("t> "))
        if( user_input == 'q'):
            if(platform.platform()[0] == 'L') :
                os.system('clear')
            else:
                os.system('cls')
            break
        else:
            word = Word()
            print("\n\t"+word.translate(user_input)+"\n")

def dictionary():
    displayDictionary()
    while True:
        user_input = str(input("d> "))
        if(user_input == 'q'):
            if(platform.platform()[0] == 'L') :
                os.system('clear')
            else:
                os.system('cls')
            break
        else:
            word = Word()
            word.word = user_input
            aux_list = word.word.split(" ")
            if(len(aux_list) > 1):
                print("\n\tWrite only 1 word\n")
            else:
                dictionary = word.getFullMeaning()
                if(dictionary != None):
                    for key , elem in dictionary.items():
                        if elem:
                            if(len(elem) >= 2 ):
                                print("\n\t" + key + " - > ")
                                for e in elem:
                                    print("\t\t *-  {:.85}  \n\t".format(e))
                            else:
                                print("\n\t" + key + ' - > ')
                                print("\t\t *-  {:.85}  \n\t".format(elem[0]))
                else:
                    print('\n\tNo Meaning in this dictionary\n')

def new_word():
    displayWord()
    while True:
        new_word = str(input("n> Enter the new word (q to comeback): "))
        if(new_word != 'q'):
            word = Word()
            instruction = str(input("Set default translation(Y/N) ? "))
            if(instruction == 'y' or instruction == 'Y' ):
                word.word = new_word
                word.translation = word.translate(new_word)
                if(word.save()):
                    print('\nWord Sucessfully saved ! \n')
                else:
                    print('\nSomething Happen, Word not saved !! \n')
            elif(instruction == 'n' or instruction == 'N '):
                print('\n')
                word.word = new_word
                word.translation = str(input("n> Enter the translation: \n"))
                word.definition_e = str(input("n> Enter the word definition: \n"))
                word.definition_s = str(input("n> Enter the word definition in spanish: \n"))
                
                if(word.save()):
                    print('\nWord Sucessfully saved ! \n')
                else:
                    print('\nSomething Happen, Word not saved !! \n')
            else:
                print('\nInvalid Input\n')
        else:
            if(platform.platform()[0] == 'L') :
                os.system('clear')
            else:
                os.system('cls')
            break
    
def exit():
    if(platform.platform()[0] == 'L') :
        os.system('clear')
    else:
        os.system('cls')
    displayTranslate(False)
    sys.exit()
    
def show_words():
    displayShow()
    while True:
        table = tt.Texttable()
        headings = ['Word','Translation','Definition English','Definition Spanish']
        table.header(headings)
        list_words = [ word.word for word in Word.select() ]
        list_translations = [word.translation for word in Word.select()]
        list_defe = [str(word.definition_e) for word in Word.select()]
        list_defs = [str(word.definition_s) for word in Word.select()]
        
        for row in zip(list_words,list_translations,list_defe,list_defs):
            table.add_row(row)
        
        s = table.draw()
        print(s)
        user_input = str(input('s>'))
        if( user_input == 'q' or user_input == 'Q'):
            if(platform.platform()[0] == 'L') :
                os.system('clear')
            else:
                os.system('cls')
            break
        else:
            pass
        

#MENU PRINCIPAL
def switch_menu(instruction):
    switch =  {
        't' :  translate,
        'n' : new_word,
        's' : show_words,
        'd' : dictionary,
        'q': exit
    }
    function = switch.get(instruction, lambda: "Invalid Input")
    function()
    displayMenu(True)


def main():
    # MAIN
    displayWelcome()
    displayMenu(True)
    while True:
        instruction = str(input("> "))
        switch_menu(instruction)


main()

    
    