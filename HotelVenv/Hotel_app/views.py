from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')

#en esta view se contiene el formulario para hacer las reservaciones

def products(request):
    return render(request, 'products.html')


## Views de los CRUD

def mostrarclientes(request):
    return render(request, 'mostrarclientes.html')


def suscriptorescrud(request):
    return render(request, 'suscriptorescrud.html')



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

