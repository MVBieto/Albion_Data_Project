import json


def extract_unique_names():
    encodings = ["utf-8", "latin-1"]  # List of encodings to try
    file_path = 'C:/repos/ALBION_ONLINE_DATA_PROJECT/new2.json'

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                json_data = json.load(file)
                unique_names = []
                for item in json_data:
                    unique_name = item.get("UniqueName")
                    if unique_name:
                        unique_names.append(unique_name)
                return unique_names
        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to decode the file using any of the provided encodings.")


def run_script():
    unique_names_list = extract_unique_names()
    return unique_names_list


result = run_script()
print(result)
