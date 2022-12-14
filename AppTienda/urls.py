from django.urls import path
from AppTienda.views import *

urlpatterns = [
    
    path('', inicio, name="inicio"),
    path('clientes/', clientes, name="clientes"),
    path('zapatillas/', zapatillas, name="zapatillas"),
    path('remeras/', remeras, name="remeras"),
    path('pantalones/', pantalones, name="pantalones"),

    path('busquedaClientes/', busquedaClientes, name="busquedaClientes"),
    path('busquedaZapatillas/', busquedaZapatillas, name="busquedaZapatillas"),
    path('busquedaPantalones/', busquedaPantalones, name="busquedaPantalones"),
    path('busquedaRemeras/', busquedaRemeras, name="busquedaRemeras"),

    path('buscarCliente/', buscarCliente, name="buscarCliente"),
    path('buscarZapatilla/', buscarZapatilla, name="buscarZapatilla"),
    path('buscarPantalon/', buscarPantalon, name="buscarPantalon"),
    path('buscarRemera/', buscarRemera, name="buscarRemera"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
   
]