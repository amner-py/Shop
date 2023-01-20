from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from ..tienda.models import UsuarioTienda


class Inicio(TemplateView):
    template_name = "inicio/inicio.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        tienda_aux=UsuarioTienda.objects.filter(usuario=self.request.user)
        if tienda_aux:
            tienda=tienda_aux.tienda.nombre
        else:
            tienda='Shop'
        return render(request,self.template_name,{'inicio':True,'nombre_tienda':tienda})