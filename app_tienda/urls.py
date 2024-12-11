from django.urls import path
from app_tienda import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página principal
    path('agregar/producto/', views.agregar_producto, name='agregar_producto'), 
    path('buscar/producto/', views.buscar_producto, name='buscar_producto'),  
    path('agregar/cliente/', views.agregar_cliente, name='agregar_cliente'),  
    path('agregar/venta/', views.agregar_venta, name='agregar_venta'),  
]


