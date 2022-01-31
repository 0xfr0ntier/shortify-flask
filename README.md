# [Shortify Flask](https://github.com/0xfr0ntier/shortify-flask/blob/main/LICENSE) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/0xfr0ntier/shortify-flask/blob/main/LICENSE)

This repo contains the backend of Shortify, a link shortener project. Built using [Flask](https://github.com/pallets/flask), [Flask-RESTful](https://github.com/flask-restful/flask-restful), and [PyMongo](https://github.com/mongodb/mongo-python-driver).

## API Tour

The API is accessed through `{Server IP}/shortlinks`: 
1. `GET` - Retrieve all shortened links from MongoDB
2. `POST` - Submit links for shortening.
3. `PUT` - Update links through `slug` property.

## Running the Site

Clone this [Repo](https://github.com/0xfr0ntier/shortify-flask).
```sh
git clone <shortify-flask>
```
Create virtual environment, and install required packages.
```sh
virtualenv venv

pip install -r req.txt
```
Get an API key from [Tinyurl](https://tinyurl.com/app) shortening service and place it in `shortner_api/common/shortener.py`.

Make a database using [mongoDB](https://www.mongodb.com/), and place your credentials in `shortner_api/common/db.py`

Next we should install our `shortner_api` as a package.
In project root, I.e. on the same level as `setup.py` run the following command
If you find any problem with this step, refer to [this thread](https://stackoverflow.com/questions/6323860/sibling-package-imports).
```sh
pip install -e .
# notice the dot after '-e'
```
Finally, run the project in dev mode.

Or serve it through your favorite server software such as [nginx](https://www.nginx.com/)

```sh
python app.py
```

### License
This project is [MIT licensed](https://github.com/0xfr0ntier/shortify-flask/blob/main/LICENSE).
