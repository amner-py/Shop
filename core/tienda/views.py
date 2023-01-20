from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import UsuarioTienda,Tienda

class TiendaTView(TemplateView):
    template_name = "tienda/modulo_tienda.html"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        tienda_aux=UsuarioTienda.objects.filter(usuario=self.request.user)
        if tienda_aux:
            tienda=tienda_aux.tienda.nombre
        else:
            tienda='Shop'
        
        tiendas=Tienda.objects.all()
        hay_tiendas=len(tiendas)>0
        return render(request,self.template_name,{'tiendas':True,'nombre_tienda':tienda,'lista_tiendas':tiendas,'hay_tiendas':hay_tiendas})
