from typing import Any, Dict
from rest_framework import serializers
from .models import DailyReport
from tag.models import Tag
from drf_writable_nested.serializers import WritableNestedModelSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class DailyReportSerializer(WritableNestedModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = DailyReport
        fields = ['id', 'user', 'tags', 'content', 'notice', 'target_date']