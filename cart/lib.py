
from django.apps import apps

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from cart.config import CART_PRODUCT_MODEL


def get_product_model():
    return apps.get_model(CART_PRODUCT_MODEL)


def get_cart(request):
    return Cart(request.session)


class CartItem(object):

    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    @property
    def id(self):
        return self.product.id

    @property
    def price(self):
        return self.product.price

    @property
    def printable_price(self):
        return self.product.printable_price

    @property
    def total(self):
        return self.qty * self.price

    @property
    def printable_total(self):
        return get_product_model().format_printable_price(self.total)

    @property
    def name(self):
        return self.product.name

    @property
    def url(self):
        return self.product.get_absolute_url()

    @property
    def logo(self):
        return self.product.logo

    @property
    def max_qty(self):
        return self.product.stock

    @property
    def price_values(self):
        return self.product.price_values

    def set_qty(self, qty):
        self.qty = qty

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'price': self.printable_price,
            'total': self.printable_total
        }


class Cart(object):

    def __init__(self, session):

        self._session = session
        self._session_key = 'CART'

        self._items = self._get_items_from_session()

    def __contains__(self, item):
        return item in self._items

    def _get_items_from_session(self):

        data = self._session.get(self._session_key)

        if not data:
            return {}

        try:
            data = {int(k): int(v) for k, v in data.items()}
        except Exception as e:
            print(e)
            return {}

        queryset = get_product_model().objects.filter(id__in=data.keys())

        if hasattr(queryset, 'visible'):
            queryset = queryset.visible()

        return {p.id: CartItem(p, qty=data[p.id]) for p in queryset}

    def commit(self):
        self._session[self._session_key] = self._get_commit_data()
        self._session.modified = True

    def _get_commit_data(self):
        return {i.id: i.qty for i in self.items}

    def add(self, product):

        if product in self.products:
            raise ValidationError(_('Product already added.'))

        if hasattr(product, 'has_stock') and not product.has_stock:
            raise ValidationError(_('No product in stock.'))

        item = CartItem(product, qty=1)

        self._items[product.id] = item
        self.commit()

        return item.serialize()

    def remove(self, product):

        if product not in self.products:
            return

        del self._items[product.id]
        self.commit()

    def set_qty(self, product, qty):

        if hasattr(product, 'has_stock') and not product.has_stock:
            raise ValidationError(_('No product in stock.'))

        if hasattr(product, 'stock') and qty > product.stock:
            raise ValidationError(
                _('Limit exceeded. Max value: {}').format(product.stock))

        if product not in self.products:
            raise ValidationError(_('Product not added to cart.'))

        item = self._items[product.id]
        item.set_qty(qty)

        self.commit()

        return item.serialize()

    def clear(self):
        self._items = {}
        self.commit()

    @property
    def items(self):
        return self._items.values()

    @property
    def count(self):
        return len(self._items)

    @property
    def is_empty(self):
        return self.count == 0

    @property
    def products(self):
        return [item.product for item in self.items]

    @property
    def total(self):
        return sum([item.total for item in self.items])

    @property
    def printable_total(self):
        return get_product_model().format_printable_price(self.total)
