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
    image = models.ImageField(upload_to="home/media/testimonials")

    def __str__ (self):
        return self.title