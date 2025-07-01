from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
