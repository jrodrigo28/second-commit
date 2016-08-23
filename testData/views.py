from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'testData/article_list.html', {'articles':articles})

