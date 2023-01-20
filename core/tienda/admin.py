from django.contrib import admin
from .models import Tienda, UsuarioTienda

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display=['nombre','direccion','telefono']
    list_filter=[]
    list_editable=[]
    list_per_page=15
    search_fields=['nombre']