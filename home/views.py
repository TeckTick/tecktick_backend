from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from .serializers import TeamSerializer
from .models import Team
from rest_framework.response import Response
from rest_framework import status
from .utils import get_team_by_pk

class TeamList(APIView):
    def get(self, request):
        print("GET request received for TeamList")
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print("POST request received for TeamList")
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListTeamById(APIView):
    def get(self, request, pk):
        print("GET request received for ListTeamById with pk =", pk)
        team = get_object_or_404(Team, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        print("PUT request received for ListTeamById with pk =", pk)
        team = get_object_or_404(Team, pk=pk)
        serializer = Team(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print("DELETE request received for ListTeamById with pk =", pk)
        team = get_object_or_404(Team, pk=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
