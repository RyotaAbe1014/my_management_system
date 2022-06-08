from rest_framework import serializers
from .models import DailyReport

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['user', 'tags', 'content', 'notice', 'target_date']