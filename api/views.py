from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sports
from .serializers import sportsSerializer


class sport(APIView):

    def get(self, request):
        obj = Sports.objects.all()
        serializer = sportsSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
            data = request.data
            serializer = sportsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

