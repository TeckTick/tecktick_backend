from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from .serializers import PartnerSerializer, TestimonialSerializer, TeamSerializer
from .models import Partner, Testimonial,Team
from rest_framework.response import Response
from rest_framework import status, generics
from .utils import get_partner_by_pk
# Create your views here.


# Partner views
class PartnerList(APIView):
    def get(self, request):
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListPartnersById(APIView):
    def get(self, request, pk):
        partner = get_partner_by_pk(pk)
        serializer = PartnerSerializer(partner)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        partner = get_partner_by_pk(pk)
        serializer = PartnerSerializer(partner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        partner = get_partner_by_pk(pk)
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Testimonial views
class TestimonialList(APIView):
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
    

class ListTestimonialsById(APIView):
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
    

# Team views
class TeamList(APIView):
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListTeamById(APIView):
    def get(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Partner, Testimonial, Team
# from .serializers import PartnerSerializer, TestimonialSerializer, TeamSerializer

# partner routes
# @api_view(['GET', 'POST'])
# def partner_list(request):
#     if request.method == 'GET':
#         partners = Partner.objects.all()
#         serializer = PartnerSerializer(partners, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PartnerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def partners_by_id(request, pk):
#     try:
#         partner = Partner.objects.get(pk=pk)
#     except Partner.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PartnerSerializer(partner)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PartnerSerializer(partner, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         partner.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # team routes
# @api_view(['GET', 'POST'])
# def team_list(request):
#     if request.method == 'GET':
#         teams = Team.objects.all()
#         serializer = TeamSerializer(teams, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def team_by_id(request, pk):
#     try:
#         team = Team.objects.get(pk=pk)
#     except Team.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TeamSerializer(team)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TeamSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # testimonial routes
# @api_view(['GET', 'POST'])
# def testimonial_list(request):
#     if request.method == 'GET':
#         testimonials = Testimonial.objects.all()
#         serializer = TestimonialSerializer(testimonials, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TestimonialSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def testimonial_by_id(request, pk):
#     try:
#         testimonial = Testimonial.objects.get(pk=pk)
#     except Testimonial.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TestimonialSerializer(testimonial)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TestimonialSerializer(testimonial, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         testimonial.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

