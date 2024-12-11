from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.producto.nombre}"


