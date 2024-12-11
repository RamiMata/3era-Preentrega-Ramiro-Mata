

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ProductoFormulario, ClienteFormulario, VentaFormulario
from .models import Producto

def inicio(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = ProductoFormulario()
    return render(request, 'agregar_productos.html', {'formulario': formulario, 'titulo': 'Agregar Producto'})

def agregar_cliente(request):
    if request.method == 'POST':
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = ClienteFormulario()
    return render(request, 'agregar_clientes.html', {'formulario': formulario, 'titulo': 'Agregar Cliente'})

def agregar_venta(request):
    if request.method == 'POST':
        formulario = VentaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = VentaFormulario()
    return render(request, 'agregar_ventas.html', {'formulario': formulario, 'titulo': 'Registrar Venta'})

def buscar_producto(request):
    query = request.GET.get('q')
    resultados = Producto.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})