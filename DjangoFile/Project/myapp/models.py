from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    year=models.IntegerField()
    image=models.ImageField(upload_to='img')

    def __str__(self):
        return '{}'.format(self.title)
    
class AdminDetails(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    con_password=models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)