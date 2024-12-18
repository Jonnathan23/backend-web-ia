from django.db import models

# Create your models here.
class Histoy(models.Model):
    acurracy = models.FloatField()    
    predicted_calsses = models.TextField()
    loss = models.FloatField()
    
class Images(models.Model):
    image = models.ImageField(null=True)