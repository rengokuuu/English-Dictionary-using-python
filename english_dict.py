import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def english_dict():
    user = input("Enter a word: ").lower()
    if user in data:
        return data[user]
    elif user.title() in data:
        return data[user.title()]
    elif len(get_close_matches(user, data.keys(), ))>0:
        yes_no = input("Did you mean '%s' instead? Enter Y if yes, or N if no: " % get_close_matches(user, data.keys())[0])
        if yes_no == 'Y':
            return data[get_close_matches(user, data.keys())[0]]
        elif yes_no =='N':
            return "Word doesn't exist. Please check the word again."
        else:
            return "We didn't understand your entry."
    else:
        return "Word doesn't exist. Please check the word again."

answer = english_dict()
if type(answer) == list:
    for item in answer:
        print(item)
else:
    print(answer)