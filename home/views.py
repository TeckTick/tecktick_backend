from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from .serializers import PartnerSerializer, TestimonialSerializer
from .models import Partner, Testimonial
from rest_framework.response import Response
from rest_framework import status
from .utils import get_partner_by_pk
# Create your views here.


@api_view(['GET'])

# a test view to check if the API is working
def home(request):
    message = 'Congratulations! You have created your first API'

    # return a JSON response
    return JsonResponse({'message': message})


class ListPartners(APIView):
    def get(self, request):
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListPartnersById(APIView):
    def get(self, request, pk):
        partner = get_partner_by_pk(pk)
        serializer = PartnerSerializer(partner)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self, request, pk):
    #     partner = get_partner_by_pk(pk)
    #     serializer = PartnerSerializer(partner, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk):
    #     partner = get_partner_by_pk(pk)
    #     partner.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class PostPartners(APIView):    
    def post(self, request):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePartners(APIView):    
    def put(self, request, pk):
        partner = get_partner_by_pk(pk)
        serializer = PartnerSerializer(partner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePartners(APIView):    
    def delete(self, request, pk):
        partner = get_partner_by_pk(pk)
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Testimonial views

class Testimonials(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Testimonial(APIView):
    def get(self, request, pk):
        testimonial = get_object_or_404(Testimonial, pk=pk)
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        testimonial = get_object_or_404(Testimonial, pk=pk)
        serializer = TestimonialSerializer(testimonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        testimonial = get_object_or_404(Testimonial, pk=pk)
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)