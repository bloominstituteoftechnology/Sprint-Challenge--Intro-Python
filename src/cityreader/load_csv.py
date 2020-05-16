import csv
import os
from collections import namedtuple

Source = namedtuple('Source', ['columns', 'data'])

def _check_exists(filepath):
    return os.path.isfile(filepath)

def _load(filepath, delimiter):
    data = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return Source(data[0], data[1:])

def load_csv(filename, delimiter):
    if _check_exists(filename):
        return _load(filename, delimiter=',')


if __name__ == "__main__":
    print(load_csv('cities.csv', delimiter=','))