import json
data = {}

def JsonSerialize(data, sFile):
    with open(sFile, 'w') as write_file:
        json.dump(data, write_file)

def JsonDeserialize(sFile):
    with open(sFile, 'r') as read_file:
        return json.load(read_file)

def print_dictionary(dData):
    for keys, values in dData.items():
        print(keys)
        print(values)
        print(type(dData[keys]))
    
MyFile = './quiz.json'
data = JsonDeserialize(MyFile)
print_dictionary(data)

print(type(data['quiz']))
print_dictionary(data['quiz'])
print_dictionary(data)