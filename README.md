# MP-cart

Django cart app.

### Installation

Install with pip:

```
pip install django-mp-cart
```

Settings:
```
from cart.settings import CartSettings
 
class CommonSettings(
        ...,
        CartSettings,
        BaseSettings):
    pass
```

Urls:
```
urlpatterns = [
    ...,
    path('cart/', include('cart.urls')),
    ...
]
```

Template (wrapper.html):
```
{% load cart %}
 
{% get_cart as cart %}
 
{% block js %}
 
    ...

    {% cart_js %}
 
{% endblock %}
```

Open cart html:
```
<a href="javascript:void(0);" data-role="open-cart-btn" class="cart-link">
    <i class="fa fa-shopping-cart"></i>
    {% trans 'Cart' %}
    <div data-role="cart-total" class="cart-total">
        {% if not cart.is_empty %}{{ cart.printable_total }}{% endif %}
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
