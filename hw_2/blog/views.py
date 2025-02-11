from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = Article.objects.all().values('id', 'title', 'text', 'author')
    return JsonResponse(list(articles), safe=False)

def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
        article_data = {
            'id': article.id,
            'title': article.title,
            'text': article.text,
            'author': article.author
        }
        return JsonResponse(article_data)
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)
