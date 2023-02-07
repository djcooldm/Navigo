from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=20)


class Vehicle(models.Model):
	vehicle_name = models.CharField(max_length=200)
	vehicle_type = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)