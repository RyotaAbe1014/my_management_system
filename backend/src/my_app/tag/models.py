from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField('タグ名称', max_length=20)

  def __str__(self):
        return self.name 

  class Meta:
    db_table = 'tags'
    ordering = ['name']