
from django.conf import settings

from cart import defaults


CART_PRODUCT_MODEL = getattr(
    settings, 'CART_PRODUCT_MODEL', defaults.CART_PRODUCT_MODEL)
