from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format = None):
        """returns a ist of APIview feature"""
        an_apiview = [
        "uses hattp methods",
        "is similar",
        "gives"
        ]
        return Response({'message':'hello','an_apiview':an_apiview })

    def put(self,request,pk = None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk = None):
        """Handle a partial updating of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk = None):
        """Delete an object"""
        return Response({'method':'DELETE'})

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST )


class HelloViewSet(viewsets.ViewSet):

    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
         'Uses actions (list,create ,retrive,update)',
         "Automatically maps to URLs",
         ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk= None):
        """Handle getting an object by its ID"""
        return ({'http_method':'GET'})

    def update(self,request,pk= None):
        """Handle updating an object"""
        return ({'http_method':'PUT'})

    def partial_update(self,request,pk= None):
        """Handle updating part of an object"""
        return ({'http_method':'PATCH'})

    def destroy(self,request,pk= None):
        """Handle removing an object"""
        return ({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permision_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
