from django.db import models



# Create your models here.
class tblpais(models.Model):

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre)



class tblciudad(models.Model):

    nombre = models.CharField(max_length=200)
    def __str__(self):
        return str(self.nombre)




class tblhotel(models.Model):#########HOTEL

    pais_id = models.ForeignKey(tblpais, on_delete = models.CASCADE)
    ciudad_id = models.ForeignKey(tblciudad, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return str(self.nombre)
    



class tbltemporada(models.Model):

    nombre_temp = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    def __str__(self):
        return str(self.nombre_temp)


class tbltipo_habitacion(models.Model):

    nombre_tipo_habitacion = models.CharField(max_length=200)
    cant_camas = models.IntegerField()

    def __str__(self):
        return str(self.nombre_tipo_habitacion)




class tblhabitacion(models.Model):#######HABITACION

    hotel_id = models.ForeignKey(tblhotel, on_delete = models.CASCADE)
    tipo_habitacion_id = models.ForeignKey(tbltipo_habitacion, on_delete = models.CASCADE)
    piso = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    disponibilidad = models.BooleanField()

    def __str__(self):
        #tipo = tbltipo_habitacion()
        return str(f'{self.id} {self.tipo_habitacion_id}')




class tblprecio_habitacion(models.Model):

    tipo_habitacion_id = models.ForeignKey(tbltipo_habitacion, on_delete = models.CASCADE)
    temporda_id = models.ForeignKey(tbltemporada, on_delete = models.CASCADE)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return str(f'{self.tipo_habitacion_id} ${self.precio}')


#Preservación Pagina WEB


class tblreservacion(models.Model):#######RESERVACION

    #hotel_id =  models.ForeignKey(tblhotel, on_delete = models.CASCADE)
    #habitacion_id =  models.ForeignKey(tblhabitacion, on_delete = models.CASCADE)
    #precio_hab_id = models.ForeignKey(tblprecio_habitacion, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    email = models.EmailField(max_length=254, null= False)
    fecha_registro = models.DateField(auto_now_add=True)
    habitacion = models.CharField(max_length=200, null= True)


    
    def __str__(self, ):
        return str(f'{self.nombre} {self.apellido}, fecha registro: {self.fecha_registro}')


class tblcliente(models.Model):#######CLIENTE

    habitacion_id = models.ForeignKey(tblhabitacion, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField(default='0')
    identificacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return str(f'{self.nombre}  {self.apellido}')






class tblservicio(models.Model):

    nombre_servicio = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)

    fecha = models.DateField()

    def __str__(self):
        return str(self.nombre_servicio)


class tbltipo_pago(models.Model):

    nombre_tipo_pago = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre_tipo_pago)


class tblpago(models.Model):##############PAGO

    reservacion_id = models.ForeignKey(tblreservacion, on_delete = models.CASCADE)
    servicio_id = models.ForeignKey(tblservicio, on_delete = models.CASCADE)
    tipo_pago_id = models.ForeignKey(tbltipo_pago, on_delete = models.CASCADE)
    fecha = models.DateField()
    total_pago = models.DecimalField(max_digits = 10, decimal_places = 2)
  

    
    def __str__(self, ):
        return str(f'{self.reservacion_id} , Total a pagar:{self.total_pago}')



class tblsuscripciones(models.Model):##

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, null= True)

    def __str__(self, ):
        return str(f'{self.nombre} {self.email}')

