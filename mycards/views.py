from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  serializers, status
from .models import Flashcards
from .serializers import FlashcardsSerializer


# Create your views here.



class Flash(APIView):
    
    def get(self, request):
        proflash = Flashcards.objects.all()
        serializers = FlashcardsSerializer(proflash, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        
        serializers = FlashcardsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()  

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  


class Flashbyid(APIView):
    
    def get_object(self,id):
        try:
            return Flashcards.objects.get(id=id)
        except Flashcards.DoesNotExist as e:
            return Response({"error": "Not found"},status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializers = FlashcardsSerializer(instance)
        return Response(serializers.data)

    def put(self,request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializers = FlashcardsSerializer(instance,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        serializers = FlashcardsSerializer(instance)
        instance.delete()
        return Response(serializers.data)

