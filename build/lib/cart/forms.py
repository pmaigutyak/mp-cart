
from django import forms


class SelectProductForm(forms.Form):

    def __init__(self, products, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['product'] = forms.ModelChoiceField(
            queryset=products.filter({'is_visible': True})
        )


class SetQtyForm(SelectProductForm):

    qty = forms.IntegerField(min_value=1, initial=1)
