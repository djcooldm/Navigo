from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField("date published")

    def __str__(self):
        return self.user_name


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=200)
    vehicle_type = models.CharField(max_length=200)

    def __str__(self):
        return self.vehicle_name
