import json
from difflib import get_close_matches

# Loading json data to a varible data
data = json.load(open("dictionary.json"))

# Function to retrieve the definintion of the word input by the user
def retrieve_meaning(word):
    #Converting all inputs to lower case
    word = word.lower()

    # Checking if the entered word exists or not and taking action according to the situation/consition
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead ? [y or n]: " % get_close_matches(word, data.keys())[0])
        if action == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif action == 'n':
            return ("The word doesnt exist in this dictionary. Sorry.");
        else:
            return ("We dont understand you, Sorry!")


user_input = input("Enter a word:")

output = retrieve_meaning(user_input)
if(type(output) == list):
    for item in output:
        print("-", item)

else:
    print("-", output)
