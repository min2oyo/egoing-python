print("\n---1")
person = {"name": "egoing", "address": "Seoul", "interest": "Web"}
print(person["name"])

print("\n---2")
for key in person:
    print(key, person[key])

print("\n---3")
persons = [
    {'name': 'egoing', 'address': 'Seoul', 'interest': 'Web'},
    {'name': 'basta', 'address': 'Seoul', 'interest': 'IOT'},
    {'name': 'blackdew', 'address': 'Tongyeong', 'interest': 'ML'}
]
for person in persons:
    for key in person:
        print(key + ": " + person[key])
