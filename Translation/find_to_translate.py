"""Translations - download the zip, extract the folder into your code folder. You have a French translations folder for
a fake store. You will notice that almost every file has TBT: tag present before some values and those values are
written in English. This means our company needs to translate these texts by sending them to a translations company.
The task: Read all the files in the folder and collect all the TBT values from each file and form a new result file
that would follow this pattern BELOW

"products.json": {
    key: "TBT:value"
},
"settings.json": {
    key: {
        subKey: "TBT:value"
    }
},"""
import json
import os


def find_not_translated(file_names, key_word):
    """Find values with and store them in to file with file name, keu, subkey(if applicable), and value"""
    # Result dictionary to write in file later
    results = {}

    def find_values(input_data, key_value):
        """Find values in file and store them in dictionary that will be added to result dictionary"""
        found_items = {}
        # iterate through key, value pairs in dictionary
        for key, value in input_data.items():
            # Check if value is dictionary
            if isinstance(value, dict):
                # If the value is dictionary then recurse into
                nested_found_items = find_values(value, key_value)
                if nested_found_items:
                    found_items[key] = nested_found_items
            elif key_value in str(value):
                # If the value contains the keyword, add it to the found items dictionary
                found_items[key] = value
        return found_items

    for file_name in file_names:
        # Iterate through file names and open them to process data in them
        with open(file_name, 'r', encoding='utf8') as f:
            data = json.load(f)
        # Find values containing the keyword and store the result dictionary
        results[file_name] = find_values(data, key_word)

    return results


# Write results in json file
def write_file(processed_data: dict):

    with open('results.json', 'w', encoding='utf8') as results_file:
        json.dump(processed_data, results_file, indent=4)


# Find files by type and create list
def create_file_list(path, file_type):
    return [file for file in os.listdir(path) if file.endswith(file_type) and file != 'results.json']


if __name__ == "__main__":
    # Path where to search json files
    path = os.path.realpath('find_to_translate.py').replace('find_to_translate.py', '')
    # Create a list of json files
    file_list = create_file_list(path, '.json')

    # Call the function with a list of file names
    final_data = find_not_translated(file_list, 'TBT')

    # Write a result dictionary in to file
    write_file(final_data)

    print(json.dumps(final_data, indent=4))