from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    all_list_article = Article.objects.all()
    context = {
        'object_list': all_list_article,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
