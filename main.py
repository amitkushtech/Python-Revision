import json


my_dictionary = {"id": "1o1", "name": "Amit", "address": "KTM"}
json_form = json.dumps(my_dictionary)
print(json_form)


# JSON TO DICTIONARY

my_json = '{"name": "Amit", "places": {"place1": "KTM", "place2": "POK"}, "age": 21}'

dict_data = json.loads(my_json)
print(dict_data["places"])
