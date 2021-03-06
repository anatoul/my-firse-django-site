from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_dade = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=20)
    email = models.EmailField()
    foto = models.ImageField()

    def registered(self):
        self.registered_date = timezone.now()    

# Create your models here.
