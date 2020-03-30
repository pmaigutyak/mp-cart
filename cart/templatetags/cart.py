
from django import template

from cart.lib import get_cart


register = template.Library()


@register.simple_tag(name='get_cart', takes_context=True)
def get_cart_tag(context):
    return get_cart(context['request'])
