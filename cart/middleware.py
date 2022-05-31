
from django.utils.functional import SimpleLazyObject
from cart.service import CartService


class CartMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.cart = SimpleLazyObject(lambda: CartService(request.session))
        return self.get_response(request)
