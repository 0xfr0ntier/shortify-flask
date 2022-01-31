from flask_restful import reqparse


def non_empty_string(s):
    if not s:
        raise ValueError("Must not be empty string")
    return s


# POST parser
post_args_parser = reqparse.RequestParser()
post_args_parser.add_argument('ios', required=True, nullable=False,
                              type=non_empty_string)
post_args_parser.add_argument('android', required=True,
                              nullable=False, type=non_empty_string)
post_args_parser.add_argument('web', required=True, nullable=False,
                              type=non_empty_string)


# PUT parser
put_args_parser = reqparse.RequestParser()
put_args_parser.add_argument(
    'slug', required=True, nullable=False, type=non_empty_string)
put_args_parser.add_argument('ios', type=non_empty_string)
put_args_parser.add_argument('android', type=non_empty_string)
put_args_parser.add_argument('web', type=non_empty_string)
