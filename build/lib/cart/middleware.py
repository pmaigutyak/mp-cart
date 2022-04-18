
from django.utils.functional import SimpleLazyObject
from cart.service import CartService


class InvoicesMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.invoices = SimpleLazyObject(
            lambda: CartService(request.products, request.user))
        return self.get_response(request)
