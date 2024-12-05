from django.db import models
from django.contrib import auth

class Player(models.Model):
  username=models.CharField(max_length=100)
  flips_quantity=models.IntegerField()
  used_time=models.IntegerField()
  date=models.DateTimeField()
  has_completed=models.BooleanField()
  user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)