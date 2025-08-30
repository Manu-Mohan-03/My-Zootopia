import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def print_details(fox_data):
    for fox in fox_data:
        print("Name: ", fox['name'])
        print("Diet: ", fox["characteristics"]["diet"])
        print("Location: ", fox["locations"][0])
        if fox.get("characteristics").get("type"):
            print("Type: ", fox["characteristics"]["type"])
        print()


animals_data = load_data('animals_data.json')

print_details(animals_data)