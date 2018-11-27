#Cleancode is equally important !!!

#Step1 - The data

#Step 2 - Check for non-exsiting wprds
# Usage of the basic if else statement will help you check for non existing words. If the word is not present
# in the data, simply let the user know. In our case, it will print "The word doesn't exist, please double check it"

#step3 - The case-sensitivity
# For example 'Rain' and 'rain' will give the same output. In order to do that, we are going to
# we are going to convert the word which the user has entered to all lower case

# step 4 - Closest Match
# Method 1 - Sequence Matcher
# Method 2 - Get close Matches

#step 5 - Did you mean this instead?
#step 6 - retrieving the defintion

# step7 - The icing on the cake

#The data here is in JSON format
#Load the data, and just check if data is loaded correctly

#Import Library
import json

# This is a python library for 'Text Processing Services', as the official site suggests.
from difflib import SequenceMatcher
from difflib import get_close_matches

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two lines of this snippet
data = json.load(open("data.json"))

# Run a Sequence Matcher
# First Parameter id 'Junk' which includes white spaces, blank lines and so oneself.
# Second and third parameters are the words you want to find similarities in-between.
# Ratio is used to find how close two words are in numerical terms
value = SequenceMatcher(None, "rainn", "rain").ratio()

#print out the value
print(value)

# Before you dive in, the basic template of this function is as follows
# get_close_matches(word, possibilities, n=3, cutoff=0.66)
# First parameter is of course the word for which you want to find close Matches
# second is a list of sequences against which to match the word
# [optional] Third is maximum number of close Matches
# [optional] where to stop considering a word as a match(0.99 being the closest to word while 0.0 being otherwise)

# output = get_close_matches("rain", ["help", "mate", "rainy"], n=1, cutoff = 0.75)
# print out output, any guesses
# print(output)


#Function for retrieving definition
def retrieve_definition(word):
    # Removing the case-sensitivity from the program
    # For example 'Rain' and 'rain' will give the same output
    # Converting all letters to lower because our data is in that format
    word = word.lower()

    #check for non existing words
    # 1st elif: To make sure the program returm the definition of words taht start with a capital letter (e.g. Delhi, Texas)
    # 2ns elif: To make sure the program return the definition of (e.g. USA, NATO)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len( get_close_matches(word, data.keys()) ) > 0:
        # return ("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        # The [0] in return statement indicates the frist close match of all  matches.
        action = input("Did you mean %s instead? [y or n]:" % get_close_matches(word, data.keys())[0])
        # if the answers is yes, retrieve definition of suggested word
        if(action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")
    else:
        return("The word doesn't exist, please double check it.")

#Input from user
word_user = input("Enter a word: ")

#Retrieve the defintion using function and print the reesult
# print(retrieve_definition(word_user))
output = retrieve_definition(word_user)
# If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-", item)
# For words having single defintion
else:
    print("-", output)
