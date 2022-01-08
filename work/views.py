from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, response
from rest_framework import status
from rest_framework.response import Response

from .models import Store, Worker

from .serializers import WorkerSerializer, StoreSerializer,VisitSerializer

# Create your views here.

class WorkerListAPIView(generics.ListAPIView):
    serializer_class = WorkerSerializer
    
    
    
    def get_queryset(self):
        return Worker.objects.all()
    
    
    
class WorkerInfoAPIView(generics.ListAPIView):
    
    serializer_class= WorkerSerializer
    
    def get(self, request, slug):
        
        query_set = Worker.objects.filter(slug=slug).first()
        
        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        
        return response.Response('Not found', status = status.HTTP_404_NOT_FOUND)
    
    
class StoreListAPIView(generics.ListAPIView):
    serializer_class = StoreSerializer
    
    
    
    def get_queryset(self):
        return Store.objects.all()
    
    
class CreateStoreAPIView(generics.CreateAPIView):
    serializer_class = StoreSerializer
    
    
    
    def get_queryset(self):
        return Store.objects.all()
    
    
class VisitStoreAPIView(generics.CreateAPIView):
    serializer_class = VisitSerializer
    
    
    
    def get_queryset(self):
        return Store.objects.all()
    