from django.db import models

# Create your models here.
class Reader_model(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField( default=0)
    place=models.CharField(max_length=20,default=" ")
    gender=models.CharField(max_length=10)
    