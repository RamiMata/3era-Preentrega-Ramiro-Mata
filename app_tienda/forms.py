# app_tienda/forms.py
from django import forms
from .models import Producto, Cliente, Venta

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaFormulario(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

