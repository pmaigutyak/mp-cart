
from django import forms

from cart.utils import get_active_products


class SelectProductForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['product'] = forms.ModelChoiceField(
            queryset=get_active_products()
        )


class SetQtyForm(SelectProductForm):

    qty = forms.IntegerField(min_value=1, initial=1)
