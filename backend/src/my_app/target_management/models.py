from django.db import models
from django.contrib.auth import get_user_model
from tag.models import Tag

User = get_user_model()

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Target(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('目標名', max_length=50)
    status = models.BooleanField(default=False)
    completed_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'targets'
        ordering = ['-created_at']
