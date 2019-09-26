import json
from difflib import get_close_matches

database = json.load(open("data.json"))

query = input("Enter word here: ")
query = query.lower()

proper_noun = query[0].upper()+query[1:].lower()
acronym = query.upper()

def dic(w):
    if query in database.keys():
        definition = database[query]
        return definition
    elif proper_noun in database.keys():
        definition = database[proper_noun]
        return definition
    elif acronym in database.keys():
        definition = database[acronym]
        return definition
    elif len(get_close_matches(query, database.keys())) > 0:
        yn = input("Did you mean ~%s~ instead?  Enter Y if yes, or N if no: " % get_close_matches(query, database.keys(), cutoff=0.8)[0])
        yn = yn.lower()
        if yn == "y":
            return database[get_close_matches(query, database.keys())[0]]
        elif yn == "n":
            return "Sorry, we could not find the word you're looking for"
        else:
            return "We didn't understand your entry"
    else:
        return "We could not find that word"

    output = dic(query)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
