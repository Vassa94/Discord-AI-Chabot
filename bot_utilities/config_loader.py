import yaml
import json
import os

# Config load
with open('config.yml', 'r', encoding='utf-8') as config_file:
    config = yaml.safe_load(config_file)

## Language settings ##
valid_language_codes = []
lang_directory = "lang"

current_language_code = config['LANGUAGE']

for filename in os.listdir(lang_directory):
    if filename.startswith("lang.") and filename.endswith(".json") and os.path.isfile(
            os.path.join(lang_directory, filename)):
        language_code = filename.split(".")[1]
        valid_language_codes.append(language_code)

def load_current_language() -> dict:
    lang_file_path = os.path.join(
        lang_directory, f"lang.{current_language_code}.json")
    with open(lang_file_path, encoding="utf-8") as lang_file:
        current_language = json.load(lang_file)
    return current_language

# Instructions loader
def load_instructions() -> dict:
    instructions = {}
    instructions_path = "instructions"

    # Verificar si la carpeta "instructions" existe
    if not os.path.exists(instructions_path):
        print(f"La carpeta '{instructions_path}' no existe.")
        return instructions

    # Iterar sobre los archivos en la carpeta "instructions"
    for file_name in os.listdir(instructions_path):
        print(file_name)
        if file_name.endswith('.txt'):
            file_path = os.path.join(instructions_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                # Usar el nombre del archivo sin la extensión como el nombre de la variable
                variable_name = os.path.splitext(file_name)[0]
                instructions[variable_name] = file_content
            except Exception as e:
                print(f"Error al leer el archivo '{file_name}': {e}")
    print(instructions)
    return instructions

def load_active_channels() -> dict:
    if os.path.exists("channels.json"):
        with open("channels.json", "r", encoding='utf-8') as f:
            active_channels = json.load(f)
    return active_channels