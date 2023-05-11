from django.db import models
from django.contrib.auth.models import User, Group


show_ranges = (
    (1, 'wojewódzka'),
    (2, 'krajowa'),
    (3, 'międzynarodowa'),
)


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


class DogShow(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    range = models.IntegerField(choices=show_ranges)


organizer_group, created = Group.objects.get_or_create(name='organizer_group')




