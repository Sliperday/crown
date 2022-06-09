import datetime
from django.db import models

from django.utils import timezone


# Create your models here.
class Article(models.Model):
    Article_title = models.CharField("Название статьи", max_length=200)
    Article_text = models.TextField("Текст статьи")
    pub_data = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.Article_title

    def was_published_recently(self):
        return self.pub_data >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Имя Автора", max_length=50)
    comment_text = models.CharField("Текст коментария", max_length=200)

    def __str__(self):
        return self.author_name
