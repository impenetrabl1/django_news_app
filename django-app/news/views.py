from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    articles = list(Article.objects.all())
    template = loader.get_template('news/index.html')
    context = {
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))
