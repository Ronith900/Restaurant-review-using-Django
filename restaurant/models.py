from django.contrib.auth.models import User
from django.db import models



class restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    avg_rating = models.DecimalField(max_digits=2,decimal_places=1)
    


    def __str__(self):
        return self.name