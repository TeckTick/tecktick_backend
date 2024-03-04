from django.db import models

# Create your models here.

class Blog(models.Model):
    username = models.CharField(max_length=80)
    blog_title = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to="blog/media", blank=True, null=True)
    blog_article = models.TextField()
    likes= models.CharField(max_length=100)
    comments= models.TextField()
    profile_picture = models.ImageField(upload_to="blog/media", blank=True, null=True)
    category= models.CharField(max_length=100)
    createdat= models.DateTimeField()
    
    def __str__ (self):
        return self.username