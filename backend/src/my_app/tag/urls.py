from django.urls import path
from .views import TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('index/', TagListCreateAPIView.as_view(), name="tag_list_create_api"),
    path('<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name="tag_Retrieve_update_destroy_api"),
]
