from django.db import models

# Create your models here.

CATEGORIE = (
    ("Eléctricité", "Eléctricité"),
    ("Plomberie", "Plomberie"),
    ("Matériels et divers", "Matériels et divers"),
    ("Peinture", "Peinture"),
)


class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField(max_length = 300, null = True)
    image = models.ImageField(upload_to = 'produits')
    categorie = models.CharField(max_length=50, choices=CATEGORIE)

    def __str__(self):
        return self.name
