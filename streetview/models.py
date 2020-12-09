from django.db import models

# Create your models here.
class StreetViewPost(models.Model):
    title = models.CharField(max_length=50,null=False)
    streetXY = models.CharField(max_length=100,null=False)