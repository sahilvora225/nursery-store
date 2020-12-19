from django.db import models

# Create your models here.

class Plant(models.Model):
    """
    A model for Plants.
    """
    name = models.CharField(max_length = 254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='plant/')
    seller = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name='plants'
    )