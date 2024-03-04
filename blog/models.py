from django.db import models
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
    