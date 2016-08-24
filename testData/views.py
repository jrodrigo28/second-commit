from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'testData/article_list.html', {'articles':articles})

def article_detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    return render(request,'testData/article_detail.html',{'article':article})

def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.created_date = timezone.now()
            article.save()
            return redirect('article_detail',pk=article.pk)
    else:
        form = ArticleForm()
    return render(request,'testData/article_edit.html',{'form':form})

def edit_article(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.created_date = timezone.now()
            article.save()
            return redirect('article_detail',pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request,'testData/article_edit.html',{'form':form})

