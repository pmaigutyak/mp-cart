
from django.utils.translation import ugettext
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

from cart.forms import SelectProductForm, SetQtyForm


@require_POST
def _cart_action_view(request, action_factory, form_class, message):

    form = form_class(request.products, data=request.POST)

    if not form.is_valid():
        return JsonResponse({'message': form.errors.as_json()}, status=403)

    cart = request.cart

    try:
        result = action_factory(cart, form.cleaned_data)
    except ValidationError as e:
        return JsonResponse({'message': ', '.join(e.messages)}, status=403)

    return JsonResponse({
        'message': message,
        'result': result,
        'total': cart.printable_total
    })


def add(request):
    return _cart_action_view(
        request,
        action_factory=lambda cart, data: cart.add(**data),
        form_class=SelectProductForm,
        message=ugettext('Product added to cart')
    )


def remove(request):
    return _cart_action_view(
        request,
        action_factory=lambda cart, data: cart.remove(**data),
        form_class=SelectProductForm,
        message=ugettext('Product removed from cart')
    )


def get_modal(request):
    return render(request, 'cart/modal.html', {'cart': request.cart})


@csrf_exempt
def set_qty(request):
    return _cart_action_view(
        request,
        action_factory=lambda cart, data: cart.set_qty(**data),
        form_class=SetQtyForm,
        message=ugettext('Quantity updated')
    )
