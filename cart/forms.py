
from django import forms

from cart.lib import get_product_model


class SelectProductForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=get_product_model().objects.all())


class SetQtyForm(SelectProductForm):

    qty = forms.IntegerField(min_value=1, initial=1)
