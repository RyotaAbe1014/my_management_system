from django.shortcuts import render
from rest_framework import generics
from .serializers import TargetSerializer
from .models import Target
# Create your views here.


class TargetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class TargetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class CompletedTargetListAPIView(generics.ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def get_queryset(self):
        return Target.objects.filter(status=True).order_by('-completed_at')
