from django.urls import path
from .views import TargetListCreateAPIView, TargetRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('index/', TargetListCreateAPIView.as_view(), name="target_list_create_api"),
    path('<int:pk>/', TargetRetrieveUpdateDestroyAPIView.as_view(), name="target_Retrieve_update_destroy_api"),
]
