from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as fecha


class Tienda(models.Model):
    id=models.CharField(verbose_name='Id',db_column='ID',max_length=5,primary_key=True)
    nombre=models.CharField(verbose_name='Nombre',db_column='NOMBRE',max_length=100)
    direccion=models.CharField(verbose_name='Dirección',db_column='DIRECCION',max_length=150)
    telefono=models.CharField(verbose_name='Teléfono',db_column='TELEFONO',max_length=15)
    fecha_creado=models.DateTimeField(verbose_name='Fecha de creado',db_column='FECHA_CREADO',default=fecha.now)
    eliminado=models.BooleanField(verbose_name='Eliminado',db_column='ELIMINADO',default=False)


    class Meta():
        db_table='TIENDA'
        verbose_name='Tienda'
        verbose_name_plural='Tiendas'

class UsuarioTienda(models.Model):
    tienda=models.ForeignKey(Tienda,verbose_name='Tienda',db_column='TIENDA_ID',on_delete=models.CASCADE)
    usuario=models.OneToOneField(User,verbose_name='Usuario',db_column='USUARIO',on_delete=models.CASCADE)
    fecha_creado=models.DateTimeField(verbose_name='Fecha de creación',db_column='FECHA_CREADO',default=fecha.now)
    eliminado=models.BooleanField(verbose_name='Eliminado',db_column='ELIMINADO',default=False)

    class Meta():
        db_table='USUARIO_TIENDA'
        verbose_name='Usuario de Tienda'
        verbose_name_plural='Usuarios de Tienda'