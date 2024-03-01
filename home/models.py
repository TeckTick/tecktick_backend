from django.db import models

# Create your models here.

class Team(models.Model):
    fullname= models.CharField(max_length=250)
    role= models.CharField(max_length=250)
    image = models.ImageField(upload_to='home/media/team', null=True, blank=True)

def __str__ (self):
        return self.fullname