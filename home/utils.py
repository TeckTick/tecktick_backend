from .models import Team
from rest_framework.response import Response
from rest_framework import status

def get_team_by_pk(pk):
    try:
        team = Team.objects.get(pk=pk)
        return team
    except Team.DoesNotExist:
        raise Response({"Error": "team does not exist"}, status=status.HTTP_404_NOT_FOUND)