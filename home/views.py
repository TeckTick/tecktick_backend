from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])

# a test view to check if the API is working
def home(request):
    message = 'Congratulations! You have created your first API'

    # return a JSON response
    return JsonResponse({'message': message})