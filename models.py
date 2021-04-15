from django.db import models

# Create your models here.
class Registeration(models.Model):
    firstname          = models.CharField(max_length=100)
    lastname           = models.CharField(max_length=100)
    fullname           = models.CharField(max_length=100)
    fathername         = models.CharField(max_length=100)
    mobileno           = models.IntegerField()
    email               = models.EmailField()
    password1           = models.CharField(max_length=20)
    password2           = models.CharField(max_length=20)
    tempadd             = models.TextField()
    pin_temp            = models.IntegerField()
    permadd             = models.TextField()
    pin_per             = models.IntegerField()
    aadhar              = models.ImageField(upload_to='pics')
    pan                 = models.ImageField(upload_to='pics')
    bankno             =  models.ImageField(upload_to='pics')
    Holder_name        =  models.TextField()
    bankNo             =  models.IntegerField()
    ifsccode           =  models.CharField(max_length=100)
    lastname           = models.CharField(max_length=100)

