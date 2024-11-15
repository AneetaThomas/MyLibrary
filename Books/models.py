from django.db import models

# # # Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author =models.CharField(max_length=20)
    price=models.IntegerField()
    pages=models.IntegerField()
    languages=models.CharField(max_length=20)
    cover=models.ImageField(upload_to='cover')
    pdf=models.FileField(upload_to='pdf')


    def __str__(self):
        return self.title
    def __str__(self):
        return self.author # only string commads are returned
