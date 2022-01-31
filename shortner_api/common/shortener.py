import requests
from shortner_api.common.utils import generate_slug
from shortner_api.common.db import collec

API_KEY = "UAP42FGNPsqY6X1yG7ayCIJZCjxMMZbpsEwB9A6kdE6pkD2O85wnnDtYihtm"


def get_links() -> list:

    lst = []

    for doc in collec.find():
        doc.pop('_id')
        lst.append(doc)

    return lst


def shorten_link(link: str) -> str:

    req_url = f'https://api.tinyurl.com/create?api_token={API_KEY}'

    req_body = {
        'url': link,
        'domain': 'tiny.one'
    }

    req = requests.post(req_url, req_body)

    res = req.json()

    return res['data']['tiny_url']


def shorten_links(args: dict) -> dict:

    shortened_links = {}
    slug = ''

    while collec.find_one({'slug': (slug := generate_slug())}):
        pass

    shortened_links['slug'] = slug
    shortened_links['web'] = shorten_link(args['ios'])

    shortened_links['ios'] = {
        'primary': shorten_link(args['ios']),
        'fallback': args['ios']
    }

    shortened_links['android'] = {
        'primary': shorten_link(args['ios']),
        'fallback': args['android']
    }

    return shortened_links


def update_links(args: dict) -> dict:

    doc = collec.find_one({'slug': args.pop('slug')})

    for key, value in args.items():
        if value:
            doc[key] = shorten_link(value) if key == 'web' else {
                'primary': shorten_link(value),
                'fallback': value
            }

    return doc
