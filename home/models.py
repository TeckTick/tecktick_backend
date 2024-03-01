from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to="home/media/partners")

    def __str__ (self):
        return self.name

class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="home/media/testimonials", blank=True, null=True, default="home/media/testimonials/default.png")

    def __str__ (self):
        return self.title
    
class Team(models.Model):
    fullname= models.CharField(max_length=250)
    role= models.CharField(max_length=250)
    image = models.ImageField(upload_to='home/media/team', null=True, blank=True)

    def __str__ (self):
        return self.fullname