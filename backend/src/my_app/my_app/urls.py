from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/daily_report/', include('daily_report.urls')),
    path('api/tag/', include('tag.urls')),
    path('api/target_management/', include('target_management.urls')),
]
