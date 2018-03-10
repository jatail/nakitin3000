from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

User = get_user_model()

class Eventmaker(models.Model):
    canAdd = models.BooleanField(
        default = True,
    )
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

# Create your models here.
class Organization(models.Model):
    name = models.CharField(
        max_length=140,
    )
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(
        max_length=140,
    )
    venue = models.CharField(
        max_length=40,
    )
    description = models.TextField(
    )
    date = models.DateField(
        default = timezone.now,
    )
    organizer = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
    )
    createdby = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name

class Nakki(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    task = models.CharField(
        max_length=140,
    )
    starttime = models.TimeField(
        default = timezone.now,
    )
    endtime = models.TimeField(
        default = timezone.now,
    )
    personcount = models.IntegerField(
        default = 1,
        validators=[MinValueValidator(1)]
    )
    def __str__(self):
        return self.task + " @ " + self.event.name

class Nakittautuminen(models.Model):
    nakki = models.ForeignKey(
        Nakki,
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.nakki.task + " @ " + self.nakki.event.name

class Orgadmin(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.organization.name