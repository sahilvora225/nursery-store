from django.db import models

# Create your models here.

class Order(models.Model):
    """
    A model to keep track of order.
    """
    buyer = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name='order'
    )
    status = models.CharField(max_length=50, default='delivered')
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    plant = models.ForeignKey(
        'plant.Plant', on_delete=models.CASCADE, related_name='purchase'
    )
    quantity = models.PositiveIntegerField()
    price_each = models.DecimalField(max_digits=5, decimal_places=2)