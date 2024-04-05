import json

json_data = '''
{
    "estudantes": [
        {
            "id": 1,
            "Nome": "Bernardo",
            "Idade": 18
        },
        {
            "id": 2,
            "Nome": "João",
            "Idade": 23
        }
    ]
}
'''

data = json.loads(json_data)
data['test'] = True
new_json = json.dumps(data, indent=2, sort_keys=True)
print(new_json)

