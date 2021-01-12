import pandas as pd
import pyinputplus as pyip
import random

raw_data = pd.read_csv('urban_dictionary.csv')
data = raw_data.drop('tags', axis=1)
data = data.drop('date', axis=1)
data['word_lower'] = data['word'].str.lower()


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
