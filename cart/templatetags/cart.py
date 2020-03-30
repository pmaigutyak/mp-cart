
from django import template

from cart.lib import get_cart


register = template.Library()


@register.inclusion_tag(
    'cart/cart-js.html',
    takes_context=True,
    name='cart_js')
def render_cart_js(context):
    return context


@register.simple_tag(name='get_cart', takes_context=True)
def get_cart_tag(context):
    return get_cart(context['request'])
