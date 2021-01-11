import pandas as pd
import pyinputplus as pyip
import random

raw_data = pd.read_csv('urban_dictionary.csv')
data = raw_data.drop('tags', axis=1)
data = data.drop('date', axis=1)
data['word_lower'] = data['word'].str.lower()

"""
Index quantity : 4272

Columns and type of data : 
 0   definition     object
 1   word           object
 2   author         object
 3   tags           object
 4   up             int64 
 5   down           int64 
 6   date           object
 
We're going to drop the columns tags and date. Later in the process,possibility to add new functionalities
We're going to only do a simple research of word and a random function to return a word and her information
"""


def treat_data():
    raw_data = pd.read_csv('urban_dictionary.csv')
    data = raw_data.drop('tags', axis=1)
    data = data.drop('date', axis=1)


def choice_switch(argument):
    switcher = {
        1: search,
        2: give_random_word
    }
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    func()


def search():
    chosen_word = pyip.inputStr('Enter the word you are searching for : ').lower()
    definition = None
    found = False

    try:
        definition = data.loc[data['word_lower'] == chosen_word, 'definition'].values[0]
        found = True
    except IndexError:
        print('No word found...')
    finally:
        if found:
            print('The word you searched was ' + chosen_word + '\n' +
                  'Definition : ' + definition)


def give_random_word():
    index = random.randint(0, 4271)
    definition = data.iloc[[index]]['definition'].values[0]
    word = data.iloc[[index]]['word'].values[0]
    print('The word was ' + word + '\n' +
          'Definition : ' + definition)


print('Welcome to the Urban Dictionary app!\n' +
      '   1 - Search a specific word\n' +
      '   2 - Learn me a new word!')

#  Code to get the user choice
while True:
    choice = input('What do you want to do? Enter the number : ')
    try:
        choice = int(choice)
    except ValueError:
        print('Please use numeric digits!\n')
        continue
    if not(choice == 1 or choice == 2):
        print('Please enter a valid choice!\n')
        continue
    choice_switch(choice)
    break
