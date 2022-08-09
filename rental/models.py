from django.db import models

# Create your models here.
class cycle(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    describe = models.TextField(default="Hari")

class sport(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    describe = models.TextField(default="Hari")

class electronic(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    describe = models.TextField(default="Hari")