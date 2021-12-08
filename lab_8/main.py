from flask import Flask
from flask_restful import Api

from endpoints.endpoints import MoviesEndpoint, LinksEndpoint, RatingsEndpoint, TagsEndpoint

app = Flask(__name__)
api = Api(app)


api.add_resource(MoviesEndpoint, '/movies')
api.add_resource(LinksEndpoint, '/links')
api.add_resource(RatingsEndpoint, '/ratings')
api.add_resource(TagsEndpoint, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
