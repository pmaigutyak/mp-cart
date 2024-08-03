# MP-cart

Django cart application. Works with/without quantity field. 
Allows to set up max stock.

### Installation

Installation:
* add `django-mp-cart` to `requirements.txt`
* add `cart` to `INSTALLED_APPS`
* add `'cart.middleware.CartMiddleware',` to `MIDDLEWARE` settings
* add `'css/cart.css',` to css files
* add `'js/cart.js',` to js files
* add `path('cart/', include('cart.urls')),` to `urls.py`
* add `{{ request.cart.render_js }}` before `</body>` tag close

Requirements:
* `request.products.filter` method with is_visible(bool), id_in(list) params
* `request.products.format_printable_price` method with price argument


Open cart html:
```
<a href="javascript:void(0);" data-role="open-cart-btn">
    <i class="fa fa-shopping-cart cart-icon"></i>
    <div data-role="cart-total">
        {{ request.env.cart.printable_total }}
    </div>
</a>
```
