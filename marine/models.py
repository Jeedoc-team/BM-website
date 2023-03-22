from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField(max_length = 300, null = True)
    image = models.ImageField(upload_to = 'produits')

    def __str__(self):
        return self.name
