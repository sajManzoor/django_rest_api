from rest_framework import serializers
from . import models


class StartSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects, this inhernts the modelserializer"""



    class Meta:
        """State what we need from the models"""
        model = models.UserProfile
        fields = ('id','email','name','password')
        #password should never be read through the serializer
        extra_kwargs = {'password':{'write_only':True}}


    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user