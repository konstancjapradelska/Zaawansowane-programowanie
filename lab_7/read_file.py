import csv
from Movie import Movie


def read(path):
    file = open(path, encoding="utf8")
    type(file)
    csvreader = csv.reader(file)
    next(csvreader)

    rows = []
    for row in csvreader:
        movie = Movie(row[0], row[1], row[2]).__dict__
        rows.append(movie)
    return rows
