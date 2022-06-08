from django.shortcuts import render
from rest_framework import generics
from .serializers import DailyReportSerializer
from .models import DailyReport
# Create your views here.


class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer


class ReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
