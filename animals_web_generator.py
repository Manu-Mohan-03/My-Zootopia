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
        animal_info_str += serialize_animal(fox)
    return animal_info_str


def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    if animal_obj.get("characteristics").get("diet"):
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if animal_obj.get("locations") and len(animal_obj.get("locations")) > 0:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if animal_obj.get("characteristics").get("type"):
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</li>\n'
    return output


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