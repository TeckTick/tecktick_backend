from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import CommentSerializer
from rest_framework.views import APIView
from .models import Comment
from rest_framework.response import Response
from rest_framework import status






#  Comment views
class CommentList(APIView):
    def get(self, request, pk):

        # sample object with comments 

        comments = [
            {
                "id": 1,
                "body": "This is a comment",
                "created_on": "2021-08-02T08:00:00Z"
            },
            {
                "id": 2,
                "body": "This is another comment",
                "created_on": "2021-08-02T08:00:00Z"
            }


        ]

        return JsonResponse(comments, safe=False)