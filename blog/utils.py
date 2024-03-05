from .models import Blog
from rest_framework.response import Response
from rest_framework import status

def get_partner_by_pk(pk):
    try:
        blog = Blog.objects.get(pk=pk)
        return blog
    except blog.DoesNotExist:
        raise Response({"Error": "Partner does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
