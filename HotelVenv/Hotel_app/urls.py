from django.urls import path

from .views import *



urlpatterns = [ 
    path('index/', index),
    path('error/', error),
    path('register/', register),
    path('about/', about),
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
    

 
]