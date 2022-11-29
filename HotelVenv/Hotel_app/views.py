from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView
) 


# Create your views here.



def index(request):
    return render(request,'index.html')

def error(request):
    return render(request, 'error_404.html')

def about(request):
    return render(request,'about.html') 


def gallery(request):
    return render(request, 'gallery.html')

@login_required(login_url='')
def perfil(request):
    return render(request, 'perfil.html')

#en esta view se contiene el formulario para hacer las reservaciones

def products(request):
    return render(request, 'products.html')


## Views de los CRUD

def mostrarclientes(request):
    return render(request, 'mostrarclientes.html')


def suscriptorescrud(request):
    return render(request, 'suscriptorescrud.html')


##mostraar view del login
## E ingresar con el login
def vistalogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            return redirect('/hotel/index/')
    
        else:

            messages.success(request, 'Datos incorrectos')

    return render(request, 'login.html')


#Cerrar sesión
def cerrarsesion(request):
    logout(request)
    return redirect('/hotel/') 




#####métodos para los CRUD

#mostrar los clientes

def adminclientes(request):
    listacli = tblcliente.objects.all()
    return render(request,'mostrarclientes.html', {"cliente":listacli})

#agregar clientes

def addcliente(request):
    habitacion_id = request.POST['inputhabitacion']
    nombre = request.POST['inputnombre']
    apellido = request.POST['inputapellido']
    edad = request.POST['inputedad']
    identificacion = request.POST['inputid']
    telefono = request.POST['inputtelefono']

    cliente = tblcliente.objects.create(
        habitacion_id = habitacion_id, nombre = nombre, apellido = apellido, edad = edad,
        identificacion = identificacion, telefono = telefono
    )
    return redirect('/hotel/mostrarclientes')


###AGREGAR UNA RESERVACIÓN 
def addreservacion(request):


    nombre = request.POST['inputnombre']
    apellido = request.POST['inputapellido']

    fecha_llegada = request.POST['inputfechaLl']
    fecha_salida = request.POST['inputfechaS']
    email = request.POST['inputemail']

    habitacion = request.POST['inputhabitacion']

    reservacion = tblreservacion.objects.create(
        nombre = nombre, apellido = apellido, fecha_llegada = fecha_llegada, fecha_salida = fecha_salida,
        email = email, habitacion = habitacion

    )
    messages.success(request, 'Reservación realizada con éxito')
    

    return redirect('/hotel/products')


#MOSTRAR RESERVACIONES




#mostrar suscripciones a la pagina
def adminsuscripciones(request):
    listasus = tblsuscripciones.objects.all()
    return render(request, 'suscriptorescrud.html', {'suscriptor':listasus})

#agregar una sucripción
def addsuscriptor(request):
    nombre = request.POST['inputnombre']
    apellido = request.POST['inputapellido']
    email = request.POST['inputemail']

    suscriptor = tblsuscripciones.objects.create(
        nombre = nombre, apellido = apellido, email = email
    ) 
    return redirect('/hotel/suscripcion')







#editar una suscripcion

def editsuscriptor(request,id):
    suscripcion=tblsuscripciones.objects.get(id=id)
    return render(request,'editsuscripcion.html', {"suscripcion":suscripcion})

def guardarsuscriptor(request,id): 
     nombre=request.POST['inputnombre']
     apellido=request.POST['inputapellido']
     email=request.POST['inputemail']

     id=tblsuscripciones.objects.get(id=id)
     id.nombre=nombre
     id.apellido=apellido
     id.email=email
     id.save()
     return redirect('/hotel/suscripcion')     




#eliminar una suscripcion
def delsuscripcion(request, id):
    suscripcion = tblsuscripciones.objects.get(id=id)
    suscripcion.delete()
    return redirect('/hotel/suscripcion')


##Registrar

#### CLASE PARA INSTANCIAR A LOS CAMPOS DEL USERCRATIONFORM

class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']


#Login de usuarios dentro de la web


def register(request):
    form = Registro()

    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado con éxito')

    return render(request, 'register.html', {"form":form})



##### CONTROL DE ERRORES 

class Error404View(TemplateView):
    template_name = "error_404.html"

class Error505View(TemplateView):
    template_name = "error_500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view