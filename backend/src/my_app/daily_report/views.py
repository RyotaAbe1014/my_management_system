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


class GetReportAPIView(generics.ListAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer

    def get_queryset(self):
        target_date = self.kwargs['target_date']
        return DailyReport.objects.filter(target_date=target_date)
