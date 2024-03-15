from rest_framework import serializers
from .models import Blog, Reply, Comment, Category

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model =  Category
      fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
   category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Use PrimaryKeyRelatedField for dropdown list
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
