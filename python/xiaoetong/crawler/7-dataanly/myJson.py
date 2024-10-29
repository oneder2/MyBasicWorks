"""
Standard library: json

"""

import json

# dict -> json
info = {
        'name':'牛牧尧',
        'age':'18'
        }

# ensure_ascii can prevent string being encoded by ascii
jsonString = json.dumps(info, ensure_ascii = False) 

print(jsonString, type(jsonString))


# json -> dict
dictJson = json.loads(jsonString)
print(dictJson, type(dictJson))

