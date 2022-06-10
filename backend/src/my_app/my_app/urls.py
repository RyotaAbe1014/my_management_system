from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api/daily_report/', include('daily_report.urls')),
    path('api/tag/', include('tag.urls')),
    path('api/target_management/', include('target_management.urls')),
]
