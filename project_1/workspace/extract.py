"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    list_neo = []
    with open(neo_csv_path) as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            designation = row['pdes']
            name = row['name']
            diameter = row['diameter']
            hazardous = row['pha']
            neo = NearEarthObject(designation, name, diameter, hazardous)
            list_neo.append(neo)
    return list_neo


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    list_cad = []
    with open(cad_json_path) as infile:
        json_reader = json.load(infile)
        json_data = json_reader['data']
        for row in json_data:
            designation = row[0]
            time = row[3]
            distance = row[4]
            velocity = row[7]
            cad = CloseApproach(designation, time, distance, velocity)
            list_cad.append(cad)
    return list_cad
