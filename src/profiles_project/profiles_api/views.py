from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


# Create your views here.

class StartApiView(APIView):
    """Test API View."""
    serializer_class = serializers.StartSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'It is similar to a tradional Django view',
            'Gives you the most control ober your logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'API VIEW','an_apiview': an_apiview})


    def post(self, request):
        """Create a message with a value"""

        serializer = serializers.StartSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Start {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Hnadles updating an object."""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""


        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method': 'delete'})


class StartViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.StartSerializer
    def list(self, request):
        """Return a message"""
        a_viewset = [
            'uses actions (list, create, retrievev, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code.'

        ]
        return Response({'message':'StartViewSet',"list":a_viewset})


    def create(self, request):
        """Create a new hello message."""
        serializer = serializers.StartSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Name {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID , corresponds to http get method"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object  , corresponds to http update method"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object by its ID , corresponds to http patch method"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles destroying an object  , corresponds to http delete method"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating model profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)



