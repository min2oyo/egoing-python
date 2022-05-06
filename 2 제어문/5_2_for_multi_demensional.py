print("\n---1")
persons = [
    ["egoing", "Seoul", "Web"],
    ["basta", "Seoul", "IOT"],
    ["blackdew", "Tongyeong", "ML"],
]
print(persons[0][0])

print("\n---2")
for person in persons:
    print(person)

print("\n---3")
for person in persons:
    print(person[0]+","+person[1]+","+person[2])

print("\n---4")
person = ["egoing", "Seoul", "Web"]
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)

print("\n---5")
name, address, interest = ["egoing", "Seoul", "Web"]
print(name, address, interest)

print("\n---6")
for name, address, interest in persons:
    print(name+","+address+","+interest)
