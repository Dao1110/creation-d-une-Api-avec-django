from django.db import models

class Livre(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    prix = models.FloatField(default=0)
    description = models.TextField(null=True)