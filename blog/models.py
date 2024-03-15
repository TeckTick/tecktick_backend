from django.db import models
from usersprofile.models import CustomUser
# Create your models here.

# blog model

class Blog(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to="blog/media", blank=True, null=True)
    content = models.TextField()
    # profile_picture = models.ImageField(upload_to="blog/media", blank=True, null=True)
    category= models.CharField(max_length=100)
    likes = models.ManyToManyField(CustomUser, related_name="liked_blogs", null=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title


# comment model

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment: {} by {}'.format(self.body, self.user.username)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Reply: {} by {}'.format(self.body, self.user.username)    