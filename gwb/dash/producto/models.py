from django.db import models
# Create your models here.

class User(models.Model):
    usuario = models.CharField(max_length=300)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    telefono = models.CharField(max_length=13)
    email = models.EmailField(max_length=300)

class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()

    def __str__(self):
        return "producto: {} precio: $ {}".format(self.nombre, self.precio)
 

class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    usuario = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, null=True, blank=True, related_name="producto_comentarios",on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.comentario, self.producto)

class ImagenesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    producto = models.ForeignKey(Producto, null=True, blank=True, related_name="producto_imagenes",on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/imagenes/imagenes_producto')

    def __str__(self):
        return "{}".format(self.descripcion)


class CarritoCompras(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, related_name="producto_carrito",on_delete=models.CASCADE)
    precio = models.IntegerField()
    identificador = models.IntegerField(null=True)
    direccion = models.CharField(max_length=300)
    datos_payu = models.TextField()
    comprado = models.BooleanField(default=False)
    pendiente = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} {}".format(self.usuario, self.producto)