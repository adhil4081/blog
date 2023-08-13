from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=5000)
    subtitle = models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    
    