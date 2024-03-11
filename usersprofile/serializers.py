from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        phone = validated_data.pop('phone', None)

        user = CustomUser.objects.create_user(**validated_data)
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.save()
        return user

    def update(self, instance, validated_data):
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        phone = validated_data.pop('phone', None)

        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        instance.first_name = first_name if first_name is not None else instance.first_name
        instance.last_name = last_name if last_name is not None else instance.last_name
        instance.phone = phone if phone is not None else instance.phone
        instance.save()

        return instance
