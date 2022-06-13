from rest_framework import generics
from .serializers import DailyReportSerializer
from .models import DailyReport
from django_filters import rest_framework as filters
# Create your views here.


class ReportFilter(filters.FilterSet):

    # フィルタの定義
    target_date = filters.DateFilter(field_name="target_date",lookup_expr='exact')

    class Meta:
        model = DailyReport
        # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
        fields = ['user', 'tags', 'content', 'notice', 'target_date']


class ReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer


class ReportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer


class GetReportAPIView(generics.ListAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ReportFilter