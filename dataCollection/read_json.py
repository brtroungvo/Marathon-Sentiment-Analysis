import os
import json

DATA_COLLECTION = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(DATA_COLLECTION, "london2026Comments.json")

with open(filepath,'r',encoding = 'utf-8') as f:
    data = json.load(f)

# Creates a list of strings to contain all the comments
comments = []
for i in range(len(data)):
    comments.append(data[i]["body"])
    
