#from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q, Max, Min
from producto.models import Producto, Comentario, ImagenesProducto,CarritoCompras,User

User = get_user_model()
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

class ComentarioProducto(CreateView):
    template_name = 'producto/detalle.html'
    model = Comentario
    fields = ('comentario','usuario','producto',)

    def get_success_url(self):
        return "/detalle_producto/{}/".format(self.object.producto.pk)

class Salir(LogoutView):
    	next_page = reverse_lazy('indice')
#vita para inicio de sesion 
class Ingresar(LoginView):
    	template_name = 'producto/login.html'
        def get(self, request, **args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('indice'))
            else:
                context = self.get_context_data(**kwargs)
                return self.render_to_response(context)
        def get_success_url(self):
                return reverse('indice')

###falta codigo en inicio de sesion
#falta agregar el carrito en el html detalle

class CambiarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('telefono','apellido','usuario','nombre','email',)
    success_url = '/'
    template_name = 'producto/perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class AniadirCarrito(LoginRequiredMixin, CreateView):
    model = CarritoCompras
    fields = ('usuario','producto','precio',)
    success_url = reverse_lazy('indice')
    login_url = 'ingresar'
#desbes de estar logiado pra poder utilizar el carrito
class EliminarCarrito(LoginRequiredMixin,DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('indice')
    login_url = 'ingresar'

class ListarCarrito(LoginRequiredMixin,ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context

class ListarCarritoPendientes(LoginRequiredMixin,ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context

class ListarCarritoFinalizadas(LoginRequiredMixin,ListView):
    template_name = 'producto/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context