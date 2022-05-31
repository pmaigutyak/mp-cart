
from django.apps import apps
from django.core.exceptions import FieldDoesNotExist


def get_active_products():

    Product = apps.get_model('products', 'Product')

    queryset = Product.objects.all()

    try:
        Product._meta.get_field('is_visible')
    except FieldDoesNotExist:
        pass
    else:
        queryset = queryset.filter(is_visible=True)

    return queryset
