from flask_restful import Resource
from shortner_api.parsers.parsers import *
from shortner_api.common.shortener import get_links, shorten_links, update_links
from shortner_api.common.db import db_insert, db_update


class ShortLinks(Resource):
    def get(self):
        # TODO get urls from mongoDB    [X]

        return get_links(), 200

    def post(self):
        # TODO shorten links            [X]
        # TODO Ensure unique Slug       [X]
        # TODO Store in mongodb         [X]

        args = post_args_parser.parse_args()

        if None in list(args.values()):
            return {'msg': 'All urls are required. (i.e. ios, android, web).'}, 400

        shortened_links = shorten_links(args)
        db_insert(shortened_links)

        return shortened_links

    def put(self):
        # TODO Update shotened links    [X]
        # TODO update doc in mongoDB    [X]

        args = dict(put_args_parser.parse_args())

        if not (args['slug'] and (args['web'] or args['ios'] or args['android'])):
            return {'msg': 'Slug and at least one url are required.'}, 400

        updated = update_links(args)
        db_update(updated)

        updated.pop('_id')

        return updated, 200
