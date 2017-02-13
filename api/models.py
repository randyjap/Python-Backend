from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
