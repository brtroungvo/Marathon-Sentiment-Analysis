import os
import json

DATA_COLLECTION = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(DATA_COLLECTION, "london2026Comments.json")

with open(filepath,'r',encoding = 'utf-8') as f:
    data = json.load(f)

# Creates a dictionary with the comment as the key and the posting date as the value
comments = {}
for i in range(len(data)):
    if data[i]["body"] not in comments:
        comments[data[i]["body"]] = [data[i]["created_utc"]]
