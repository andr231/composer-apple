"""dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views import defaults as default_views

from django.urls import include, path
from producto.views import  (ListadoProducto, Indice, DetalleProducto, ComentarioProducto, Salir, Ingresar,CambiarPerfil,AniadirCarrito,EliminarCarrito,ListarCarrito,ListarCarritoPendientes,ListarCarritoFinalizadas)
#from login.views import (Reusuario,login )
urlpatterns = [ 
    path('admin/', admin.site.urls),
 	path('',Indice.as_view(),name='indice'),
	path('listado_productos/', ListadoProducto.as_view(), name="listado_productos" ),
	path('detalle_producto/<int:pk>/',DetalleProducto.as_view(),name='detalle_productos'),
	path('crear_comentario/', ComentarioProducto.as_view(), name="crear_comentario" ),
	path('salir/', Salir.as_view(), name="salir" ),
	path('ingresar/', Ingresar.as_view(), name="ingresar" ),
	path('cambiar_perfil/', CambiarPerfil.as_view(), name="cambiar_perfil" ),
	path('aniadir_carrito/', AniadirCarrito.as_view(), name="aniadir_carrito" ),
	path('listar_carrito/',ListarCarrito.as_view(),name='listar_carrito'),
	path('listar_pendientes/',ListarCarritoPendientes.as_view(),name='listar_pendientes'),
	path('listar_finalizado/',ListarCarritoFinalizadas.as_view(),name='listar_finalizado'),
	path('eliminar_carrito/<int:pk>/',EliminarCarrito.as_view(),name='eliminar_carrito'),
        

]
