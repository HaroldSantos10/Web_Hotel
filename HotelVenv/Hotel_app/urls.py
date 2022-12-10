from django.urls import path

from .views import *




urlpatterns = [ 
    path('index/', index, name = 'inicio'),
    path('error/', error),
    path('register/', register),
    path('about/', about, name = 'about'),
    path('gallery/', gallery),
    path('perfil/', perfil),
    path('products/', products),
    path('', vistalogin), #direcciona directamente al /hotel/ por lo tanto es la primer página que aparece
    path('logout/', cerrarsesion, name="cerrarsesion"),
    path('suscripcion/', adminsuscripciones),
    path('addsuscriptor/', addsuscriptor),
    path('editsuscriptor/<id>', editsuscriptor),
    path('guardarsuscriptor/<id>', guardarsuscriptor),
    path('delsuscriptor/<id>', delsuscripcion),
    path('mostrarclientes/', adminclientes),
    path('addcliente/', addcliente),
    path('addreservacion/', addreservacion),
    path('mostrarreservaciones/', adminreservaciones),
    path('editreservacion/<id>', editreservacion),
    path('guardarreservacion/<id>', guardarreservacion),
    path('delreservacion/<id>', delreservacion),
    path('mostrarusers/', mostrarusers),
    path('deluser/<id>', deluser),


    
]

