from django.db import models
from django.contrib.auth.models import User


class Kennel(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    from_city = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=128)
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
