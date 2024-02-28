from .models import Partner
from rest_framework.response import Response
from rest_framework import status

def get_partner_by_pk(pk):
    try:
        partner = Partner.objects.get(pk=pk)
        return partner
    except Partner.DoesNotExist:
        raise Response({"Error": "Partner does not exist"}, status=status.HTTP_404_NOT_FOUND)
