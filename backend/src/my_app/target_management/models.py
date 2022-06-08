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
    tags = models.ManyToManyField(Tag)
    name = models.CharField('目標名', max_length=50)
    completed_at = models.DateTimeField()
    class Meta:
        db_table = 'targets'
