import json
import pprint
with open('xx.json', 'r') as file: # r - read mode
    # json.load() takes argument(file here) as a object, while json.loads() will takes argument as string.
    data = json.load(file) 

printer = pprint.PrettyPrinter()
printer.pprint(data)

# data['key'] is not recommended because if key was not found 
# and [key not found error] will arise then program will crash.
values = data.get('key') 

for value in values:
    print(values)
    