
from django.urls import path, include

from cart import views


app_name = 'cart'


urlpatterns = [

    path('modal/', views.get_modal, name='modal'),

    path('add/', views.add, name='add'),

    path('remove/', views.remove, name='remove'),

    path('set-qty/', views.set_qty, name='set-qty')

]


app_urls = [
    path('cart/', include((urlpatterns, app_name)))
]
