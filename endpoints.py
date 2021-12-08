from flask_restful import Resource

from read_file import read

moviesPath = 'data/movies.csv'
linksPath = 'data/links.csv'
ratingsPath = 'data/ratings.csv'
tagsPath = 'data/tags.csv'


class MoviesEndpoint(Resource):
    @staticmethod
    def get():
        return read(moviesPath, 'movies')


class LinksEndpoint(Resource):
    @staticmethod
    def get():
        return read(linksPath, 'links')


class RatingsEndpoint(Resource):
    @staticmethod
    def get():
        return read(ratingsPath, 'ratings')


class TagsEndpoint(Resource):
    @staticmethod
    def get():
        return read(tagsPath, 'tags')
