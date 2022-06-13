from django.urls import path
from .views import ReportListCreateAPIView, ReportRetrieveUpdateDestroyAPIView, GetReportAPIView

urlpatterns = [
    path('index/', ReportListCreateAPIView.as_view(), name="report_list_create_api"),
    path('<int:pk>/', ReportRetrieveUpdateDestroyAPIView.as_view(), name="report_Retrieve_update_destroy_api"),
    path('<target_date>/', GetReportAPIView.as_view(), name="report_search_api"),
]
