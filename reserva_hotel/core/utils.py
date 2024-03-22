from django.utils.crypto import get_random_string as django_get_random_string
from decimal import Decimal


def generate_random_code():
    random_string = django_get_random_string(16).upper()
    return random_string