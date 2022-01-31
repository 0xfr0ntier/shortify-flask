import string
import random


def generate_slug(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choices(chars, k=size))
