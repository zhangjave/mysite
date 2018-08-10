from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# 分类数据库表
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tag = models.ForeignKey(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


