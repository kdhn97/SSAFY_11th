from django.db import models

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True, auto_now_add=False)

class Trend(models.Model):
    name = models.CharField(max_length=100)
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateField(auto_now=True, auto_now_add=False)