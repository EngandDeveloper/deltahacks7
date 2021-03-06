from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class UserInput(models.Model):
    current_date = models.DateTimeField(default=timezone.now)
    blood_pressure = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True)
