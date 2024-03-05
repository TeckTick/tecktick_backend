from django.db import models
# from home.models import User
# from home.models import User

# Create your models here.



# comment model

class Comment(models.Model):
    #blog_article = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)
    #user = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment: {} by {}'.format(self.body, self.user.username)
    

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