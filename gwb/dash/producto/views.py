from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

# Create your views here.
from django.http import HttpResponseRedirect
from producto.models import Producto, Comentario, ImagenesProducto,CarritoCompras
from django.urls import reverse
from django.db.models import Q, Max, Min



class Indice(TemplateView):
    template_name = 'producto/index.html'



class ListadoProducto(ListView):
    template_name = 'producto/listado_productos.html' 
    model = Producto
    paginate_by = 10

    def get_queryset(self):
        query = None

        if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
            query = Q(nombre=self.request.GET["nombre"])

        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(precio__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(precio__lte=int(float(self.request.GET['maximo'])))
            except:
                pass


        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(precio__gte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(precio__gte=int(float(self.request.GET['minimo'])))
            except:
                pass


        if query is not None:
            productos = Producto.objects.filter(query)
        else:
            productos = Producto.objects.all()
        return productos
    
    def get_context_data(self, **kwargs):
        context = super(ListadoProducto, self).get_context_data(**kwargs)
        context['maximo'] = Producto.objects.all().aggregate(Max('precio'))['precio__max']
        context['minimo'] = Producto.objects.all().aggregate(Min('precio'))['precio__min']
        return context

class DetalleProducto(DetailView):
    template_name = 'producto/detalle.html'
    model = Producto

#def DetalleProducto(request):
	#return render(request, "producto/DetalleProducto.html")

class ComentarioProducto(CreateView):
    template_name = 'producto/detalle.html'
    model = Comentario
    fields = ('comentario','usuario','producto',)

    def get_success_url(self):
        return "producto/detalle_producto/{}/".format(self.object.producto.pk)

#def ComentarioProducto(request):
#	return render(request, "producto/ComentarioProducto.html")

#def Salir(request):
#	return render(request, "producto/Salir.html")
class Salir(LogoutView):
    next_page = reverse_lazy('indice')


#def Ingresar(request):
#	return render(request, "producto/Ingresar.html")


class CambiarPerfil(UpdateView):
    fields = ('telefono','last_name','first_name','email',)
    #success_url = '/'
    template_name = 'producto/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user



class AniadirCarrito(CreateView):
    model = CarritoCompras
    fields = ('usuario','producto','precio',)
    success_url = reverse_lazy('indice')
   # login_url = 'ingresar'

class EliminarCarrito(DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('indice')
   # login_url = 'ingresar'


class ListarCarrito(ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
   # login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context

class ListarCarritoPendientes(ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
   # login_url = 'ingresar'
#
    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context

class ListarCarritoFinalizadas(ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
   # login_url = 'ingresar'
    
    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context



