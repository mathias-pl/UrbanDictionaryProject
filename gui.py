import tkinter as tk
import pandas as pd
#  import pyinputplus as pyip
#  import random
from functions import choice_switch, search, give_random_word
"""
raw_data = pd.read_csv('urban_dictionary.csv')
data = raw_data.drop('tags', axis=1)
data = data.drop('date', axis=1)
data['word_lower'] = data['word'].str.lower()
"""

choice_switch(1)
search()
give_random_word()

window = tk.Tk()
label = tk.Label(text='The Urban Dictionary App!')
label_modif = tk.Label(text='Those are the options you got : \n'
                            '1 - Search a specific word\n' +
                            '2 - Learn me a new word!',
                       fg="white",
                       bg="#34A2FE",
                       width=25,
                       height=4
                       )
label.pack()
label_modif.pack()

window.mainloop()
