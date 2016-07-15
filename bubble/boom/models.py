from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    age = models.IntegerField(default=0)
    area = models.CharField(max_length=10)
    feature = models.CharField(max_length=100)
    orientation = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    total_price = models.FloatField(default=0.0)
    down_payment = models.FloatField(default=0.0)
    url = models.CharField(max_length=100)
    tax = models.FloatField(default=0.0)
    loan_period = models.CharField(max_length=10)
    community = models.CharField(max_length=100)
    around = models.CharField(max_length=100)
    floor = models.CharField(max_length=10)
    style = models.CharField(max_length=30)
    building_type = models.CharField(max_length=10)
    elevator = models.CharField(max_length=100)
    heating = models.CharField(max_length=10)
    decoration = models.CharField(max_length=10)
