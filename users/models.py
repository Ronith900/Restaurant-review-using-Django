from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from restaurant.models import restaurant


class user(models.Model):
    
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    rest = models.ForeignKey(restaurant,on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
