from django.urls import path

from .views import *



urlpatterns = [
    path('index/', index),
    path('about/', about),
    path('gallery/', gallery),
    path('contact/', contact),
    path('products/', products)
]