from rest_framework import serializers
from profile_api import models


class HelloSerializers(serializers.Serializer):
    """Serializers to name field for testing api"""
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {
            'write_only': True,
            'style': {'input_type': 'password'}
        }}

    def create(self, validated_data):
        """create an retuern new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
