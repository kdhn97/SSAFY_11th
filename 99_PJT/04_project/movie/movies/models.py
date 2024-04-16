from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField()

    # admin page에서 title 표시 기능
    def __str__(self):
        return self.title