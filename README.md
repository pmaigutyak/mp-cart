# MP-cart

Django cart application. Works with/without quantity field. 
Allows to set up max stock.

### Installation

Installation:
* add `django-mp-cart` to `requirements.txt`
* add `cart` to `INSTALLED_APPS`
* add `'cart.middleware.CartMiddleware',` to `MIDDLEWARE` settings
* add `path('cart/', include('cart.urls')),` to `urls.py`
* add `{{ request.cart.render_js }}` before `</body>` tag close

Requirements:
* `request.products.filter` method with is_available(bool), id_in(list) params
* `exchange.utils.format_printable_price` method


Open cart html:
```
<a href="javascript:void(0);" data-role="open-cart-btn">
    <i class="fa fa-shopping-cart cart-icon"></i>
    <div data-role="cart-total">
        {{ request.env.cart.printable_total }}
    </div>
</a>
```

Cart modal template customization example (templates/cart/modal.html):
```
{% extends 'cart/modal.html' %}
 
{% load i18n %}
 
 
{% block item %}
    <tr data-role="cart-item">
        <td>
            <a href="{{ item.url }}">
                {{ item.name }}
            </a>
        </td>
        <td>
            {% include 'cart/qty.html' %}
        </td>
        <td>
            {% include 'cart/sum.html' %}
        </td>
        <td class="remove-cell">
            {% include 'cart/remove-button.html' %}
        </td>
    </tr>
{% endblock %}
 
 
{% block total %}
    <td colspan="4" class="cart-total">
        {% include 'cart/total.html' %}
    </td>
{% endblock %}
```
