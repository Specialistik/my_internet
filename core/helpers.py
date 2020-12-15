import six
import hmac
from hashlib import sha256

from django.conf import settings


def generate_token(login, password):
    sign = hmac.new(six.b(settings.SECRET_KEY), digestmod=sha256)
    sign.update(six.b(login))
    sign.update(six.b(password))
    return sign.hexdigest()
