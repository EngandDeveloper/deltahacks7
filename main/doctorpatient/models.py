from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=True)
    location = models.CharField(max_length=300, null=False, blank=True)
    medicalID = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=True)
    location = models.CharField(max_length=300, null=False, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

