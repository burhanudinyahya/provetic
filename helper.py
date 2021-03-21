import json
from collections import Counter

def most_common(data):
    mc = Counter(data).most_common() 
    return json.dumps(dict(mc))