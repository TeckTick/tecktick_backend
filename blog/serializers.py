from rest_framework import serializers
from .models import Blog, Reply, Comment


class BlogSerializer(serializers.ModelSerializer):
   class Meta:  
      model = Blog
      fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
   user = serializers.SerializerMethodField()

   def get_user(self, obj):
      return obj.user.username  # Retrieve the username instead of user ID
   
   class Meta:  
      model = Comment
      fields = "__all__" 
      read_only_fields = ['user']  # Make the user field read-only


class ReplySerializer(serializers.ModelSerializer):
   user = serializers.SerializerMethodField()

   def get_user(self, obj):
      return obj.user.username  # Retrieve the username instead of user ID

   class Meta:  
      model = Reply
      fields = "__all__"  
      read_only_fields = ['user']  # Make the user field read-only         
