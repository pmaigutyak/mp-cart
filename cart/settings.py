
from cart import defaults


class CartSettings(object):

    CART_PRODUCT_MODEL = defaults.CART_PRODUCT_MODEL

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + ['cart']
