from django.db import models
from django.conf import settings

# Create your models here.
class Household(models.Model): 
    name = models.CharField(max_length=200, null=False)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=False)
