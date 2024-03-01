from rest_framework import serializers
from .models import Partner, Testimonial

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"