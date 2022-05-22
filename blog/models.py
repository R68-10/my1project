from django.db import models

# Create your models here.

# model --> is table 
class Blog (models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()



    def __str__(self) :
        return self.title 
    
