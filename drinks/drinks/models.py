from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=250)
    decription = models.CharField(max_length=200)
