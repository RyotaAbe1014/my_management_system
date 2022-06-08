from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField('タグ名称', max_length=20)

  class Meta:
    db_table = 'tags'