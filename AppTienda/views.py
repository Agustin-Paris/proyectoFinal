from django.shortcuts import render
from AppTienda.models import *
from .forms import *



from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate




# Create your views here.

#####-----------Llamo al render y le pego los HTML-----------####

def inicio(request):
    zapatillas = Zapatilla.objects.all()
    return render(request,"AppTienda/inicio.html", {"zapa":zapatillas})

def clientes(request):
    return render(request,"AppTienda/clientes.html")

def zapatillas(request):
    return render(request,"AppTienda/zapatillas.html")

def remeras(request):
    return render(request,"AppTienda/remeras.html")

def pantalones(request):
    return render(request,"AppTienda/pantalones.html")

#####----------- Crear formularios para guardar en la base de datos -----------####

def clientes(request):
    if request.method == "POST":
        form=ClientesForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            telefono=informacion["telefono"]
            mail=informacion["mail"]
#Guardamos la informacion obtenida en una variable         
            cliente=Cliente(nombre=nombre, apellido=apellido,telefono=telefono,mail=mail)
#Guardamos en la base de datos con save y devolvemos a la pagina inicio cuando todo este correctamente cargado.            
            cliente.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Cliente Cargado"})

#Si no se cargo correctamente, vuelve a mostrar el formulario a cargar vacio 
    else:
        formulario=ClientesForm()
        return render(request, "AppTienda/clientes.html", {"formulario": formulario})

def zapatillas(request):
    if request.method == "POST":
#Ya que los articulos tienen informacion similar, los juntamos en un solo formulario.         
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            imagen = informacion["imagen"]
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            zapatilla=Zapatilla(modelo=modelo, marca=marca,talle=talle,precio=precio, imagen=imagen)           
            zapatilla.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Zapatilla Cargada"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/zapatillas.html", {"formulario": formulario})

def remeras(request):
    if request.method == "POST":     
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            remera=Remera(modelo=modelo, marca=marca,talle=talle,precio=precio)           
            remera.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Remera Cargada"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/remeras.html", {"formulario": formulario})   

def pantalones(request):
    if request.method == "POST":        
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            pantalon=Pantalon(modelo=modelo, marca=marca,talle=talle,precio=precio)           
            pantalon.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Pantalon Cargado"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/pantalones.html", {"formulario": formulario})


def busquedaClientes(request):
    return render(request,"AppTienda/busquedaClientes.html")

def busquedaZapatillas(request):
    return render(request,"AppTienda/busquedaZapatillas.html")

def busquedaRemeras(request):
    return render(request,"AppTienda/busquedaRemeras.html")

def busquedaPantalones(request):
    return render(request,"AppTienda/busquedaPantalones.html")


def buscarCliente(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        clientes=Cliente.objects.filter(apellido=apellido) #Traer de la base todos los clientes que tengan este apellido
        
        return render(request, "AppTienda/resultadosBusquedaClientes.html", {"clientes":clientes})
    else:
        return render(request, "AppTienda/busquedaClientes.html", {"mensaje":"Ingrese nuevamente apellido"})

def buscarZapatilla(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        zapatillas=Zapatilla.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaZapatillas.html", {"zapatillas":zapatillas})
    else:
        return render(request, "AppTienda/busquedaZapatillas.html", {"mensaje":"Ingrese nuevamente marca"})

def buscarRemera(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        remeras=Remera.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaRemeras.html", {"remeras":remeras})
    else:
        return render(request, "AppTienda/busquedaRemeras.html", {"mensaje":"Ingrese nuevamente marca"})

def buscarPantalon(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        pantalones=Pantalon.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaPantalones.html", {"pantalones":pantalones})
    else:
        return render(request, "AppTienda/busquedaPantalones.html", {"mensaje":"Ingrese nuevamente marca"})



#Usiarios login

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST['username']
            clave=request.POST['password']
            
            usuario= authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppTienda/inicio.html")             
            else:
                return render(request, "AppTienda/login.html", {"formulario":form, "mensaje":"incorrecto"})   
        else:
            return render(request, "AppTienda/login.html", {"formulario":form, "mensaje":"incorrecto"})

    else:
        form = AuthenticationForm()
        return render(request, "AppTienda/login.html", {"formulario":form})



def register(request):
    if request.method=="POST":      
        form =UserRegisterForm(request.POST)       
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            return render(request, "AppTienda/inicio.html", {"mensaje": f"usuario {username}"} ) 
        else:
            return render(request, "AppTienda/register.html" , { 'formulario':form, "mensaje":"incorrecto" })  
    else:
        form=UserRegisterForm()
        return render(request, "AppTienda/register.html" , { 'formulario':form })
























'''
def login_request(request):

    if request.method=="POST":
        form = authenticate(request, data = request.POST)

        if form.is_valid():
            usu = request.get['username']
            clave = request.get['password']
            usuario = authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request,usuario)
                return render(request, "AppTienda/inicio.html" )           
            else :
                 return render(request, "AppTienda/login.html", {"mensaje": "Usuario o contrasenia incorrecta"})

        else :
            return render(request, "AppTienda/login.html", { "formulario":form ,"mensaje": "Usuario o contrasenia incorrecta"})

    
    form = AuthenticationForm()
    return render(request, "AppTienda/login.html", {"formulario":form})




#Usiarios register

def register(request):

    if request.method=="POST":      
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            return render(request, "AppTienda/inicio.html", {"mensaje": f"usuario {username}"} ) 
        
    else:
        form=UserRegisterForm()

    return render(request, "AppTienda/register.html" , { 'formulario':form })'''