from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Template(models.Model):
    full_name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField()
    #file = models.FileField()
    def __str__(self):
        return self.full_name