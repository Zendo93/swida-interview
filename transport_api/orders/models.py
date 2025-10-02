from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.order_number

class Waypoint(models.Model):
    TYPE_CHOICES = (
        ('Pickup', 'Pickup'),
        ('Delivery', 'Delivery'),
    )

    order = models.ForeignKey(Order, related_name='waypoints', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.type} - {self.location}"
