from django.db import models
from datetime import datetime



class Dinner(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
