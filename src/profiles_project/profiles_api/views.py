from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers


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