from django.db import models
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэг'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Тематика статьи'
        ordering = ['-is_main', 'tag__name']
