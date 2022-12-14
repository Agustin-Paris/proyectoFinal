from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    mail=models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido   

class Zapatilla(models.Model):
    imagen = models.ImageField(upload_to="productos", null=True)
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca + " " + str(self.talle)   

class Remera(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca + " " + str(self.talle)  

class Pantalon(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca + " " + str(self.talle)   

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="avatares")