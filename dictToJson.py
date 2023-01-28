import json

def toJson(details):    
    with open('userDetails/userDetails.json', 'a', encoding='utf-8') as f:
        json.dump(details, f, ensure_ascii=False)
        f.write("\n")
