"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open('close_approach.csv', 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()
        for approach in results:
            row = dict([('datetime_utc', ''), ('distance_au', ''), ('velocity_km_s', ''), ('designation', ''), ('name', ''),  ('diameter_km', ''),  ('potentially_hazardous', '')])
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    dict_list = []
    for approach in results:
        ca_dict = {'datetime_utc': approach.time_str, 'distance_au': approach.distance, 'velocity_km_s': approach.velocity, 'neo': {'designation': approach.neo.designation, 'name': approach.neo.name, 'diameter_km': approach.neo.diameter, 'potentially_hazardous': approach.neo.hazardous}}
        dict_list.append(ca_dict)
    with open('close_approach.json', 'w') as outfile:
        json.dump(dict_list, outfile, indent =2)
