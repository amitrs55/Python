# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 07:29:21 2020

@author: SINGH'S
"""
from pathlib import Path
import json
from difflib import get_close_matches

#create variable to pass dirctory
data_folder = Path("C:/Users/SINGH'S/Documents/Python Scripts/app1")

#create another variable to pass file name
file_to_open = data_folder / "076 data.json"

#Use json lib function to load by passing the variable name, read only by default
data = json.load(open(file_to_open))

#print(data)
#Create function to return the meaning
def translate(w):
    w=w.lower()
#if word exists in the json loaded in data var, return value
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
#check if you get any close matches by using get close match
    elif len(get_close_matches(w,data.keys()))>0:
#%s is used to replace that with the %command value after the quotes
        response=input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0])
        if response in ("y","Y"):
            return data[get_close_matches(w,data.keys())[0]]
        elif response in ("n","N"):
            return "The word doesnt exist, please check your spelling"
        else :
            return "We did not understand that, please check!"
    else:
        return "The word doesnt exist, please check your spelling"

#Get input from user
word = input("Enter word: ")

#invoke function and store response in output
output = translate(word)

#if output is list, iterate using for loop to display one result at a time
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
