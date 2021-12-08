import csv

from lab_7.data_models.Link import Link
from lab_7.data_models.Movie import Movie
from lab_7.data_models.Rating import Rating
from lab_7.data_models.Tag import Tag


def read(path: str, data_model: str, encoding: str = 'utf8'):
    with open(path, 'r', encoding=encoding) as file:
        type(file)
        csv_reader = csv.reader(file)
        next(csv_reader)

        if data_model == 'movies':
            return getMovies(csv_reader)
        elif data_model == 'links':
            return getLinks(csv_reader)
        elif data_model == 'ratings':
            return getRatings(csv_reader)
        elif data_model == 'tags':
            return getTags(csv_reader)


def getMovies(csv_reader):
    rows = []
    for row in csv_reader:
        movie = Movie(row[0], row[1], row[2]).__dict__
        rows.append(movie)
    return rows


def getLinks(csv_reader):
    rows = []
    for row in csv_reader:
        link = Link(row[0], row[1], row[2]).__dict__
        rows.append(link)
    return rows


def getRatings(csv_reader):
    rows = []
    for row in csv_reader:
        rating = Rating(row[0], row[1], row[2], row[3]).__dict__
        rows.append(rating)
    return rows


def getTags(csv_reader):
    rows = []
    for row in csv_reader:
        tag = Tag(row[0], row[1], row[2], row[3]).__dict__
        rows.append(tag)
    return rows
