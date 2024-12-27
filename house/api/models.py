from django.db import models

# Create your models here.

class Grid(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self)-> str:
        return self.name

