from django.urls import path

from .views import *



urlpatterns = [
    path('index/', index),
    path('about/', about),
    path('gallery/', gallery),
    path('contact/', contact),
    path('products/', products),
    path('suscripcion/', adminsuscripciones),
    path('addsuscriptor/', addsuscriptor),
    path('editsuscriptor/<id>', editsuscriptor),
    path('guardarsuscriptor/<id>', guardarsuscriptor),
    path('delsuscriptor/<id>', delsuscripcion),
    path('mostrarclientes/', adminclientes),
    path('addcliente/', addcliente),
    


]