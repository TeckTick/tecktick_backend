# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# from rest_framework.decorators import api_view

from rest_framework.views import APIView
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework import status
from .utils import get_partner_by_pk
# Create your views here.


# Blog views
class BlogList(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListBlogById(APIView):
    def get(self, request, pk):
        blog = get_partner_by_pk(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        blog = get_partner_by_pk(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog = get_partner_by_pk(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
