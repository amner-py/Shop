from django.urls import path,include
from core.tienda.views import TiendaTView

urlpatterns = [
    path('lista/', TiendaTView.as_view(),name='modulo_tienda'),
]