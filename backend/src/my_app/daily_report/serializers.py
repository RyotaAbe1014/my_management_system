from rest_framework import serializers
from .models import DailyReport
from tag.serializers import TagSerializer

class DailyReportSerializer(serializers.ModelSerializer):
    # user = ユーザーシリアライザ
    tags = TagSerializer(many=True)
    class Meta:
        model = DailyReport
        fields = ['user', 'tags', 'content', 'notice', 'target_date']