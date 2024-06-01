"""
Electronics provider api - You are given a file electronics_products.json it has some keys missing and some values
might be in a wrong formats, read the  file, clean the data and serve it in a  csv format so that excel people would
be able to look at it as json is too Techyy for them.
"""
import json
import csv


def read_file(file_name):
    """Read and return json data from file"""
    with open(file_name, 'r', encoding='utf8') as f:
        data = json.load(f)['data']

    return data


def clean_line(line: dict, headers: list, replace_string='N/A'):
    """From dictionary replace none/missing values with N/A (default)"""
    for header in headers:
        if header not in line:
            line[header] = replace_string
        elif line[header] is None:
            line[header] = replace_string
    return line


if __name__ == '__main__':
    # Get headers from json file
    headers = read_file('electronics_products.json')[0].keys()

    # Prepare file for writing
    with open('result.csv', 'w', encoding='utf8') as result_file:
        writer = csv.DictWriter(result_file, fieldnames=headers)
        writer.writeheader()
        for line in read_file('electronics_products.json'):
            writer.writerow(clean_line(line, headers))


