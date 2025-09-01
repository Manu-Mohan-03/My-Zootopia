import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_info(fox_data):
    animal_info_str = ""
    # adding information to a string
    for fox in fox_data:
        # For Serialization
        animal_info_str += '<li class="cards__item">\n'

        animal_info_str += 'Name: ' + fox["name"] + '<br/>\n'
        if fox.get("characteristics").get("diet"):
            animal_info_str += 'Diet: ' + fox["characteristics"]["diet"] + '<br/>\n'
        if fox.get("locations") and len(fox.get("locations")) > 0:
            animal_info_str += 'Location: ' + fox["locations"][0]  + '<br/>\n'
        if fox.get("characteristics").get("type"):
            animal_info_str += 'Type: ' + fox["characteristics"]["type"]  + '<br/>\n'
        animal_info_str += '</li>\n'
    return animal_info_str

def edit_html_template(file_path,animals_info):
    """Open the html file for reading"""
    with open(file_path,"r", encoding="utf-8") as handle:
        html_template = handle.read()
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    return html_template

def write_animals_html(file_path,animals_html):
    with open(file_path, "w", encoding = "utf-8") as handle:
        handle.write(animals_html)


def main():
    animals_data = load_data('animals_data.json')
    animals_info = get_animal_info(animals_data)
    animals_html = edit_html_template("animals_template.html",animals_info)
    write_animals_html("animals.html", animals_html)

if __name__ == "__main__":
    main()