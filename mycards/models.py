from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Flashcards(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    subject = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now=True)
    




    def __str__(self):
        return self.title