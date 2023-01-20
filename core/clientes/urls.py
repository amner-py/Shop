from django.urls import path,include
from core.clientes.views import ClientesView

urlpatterns = [
    path('lista/', ClientesView.as_view(),name='lista_clientes'),
]