from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Article
from .forms import ArticleForm

# Create your views here.

@login_required
def article_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'testData/article_list.html', {'articles':articles})

@login_required
def team_article_list(request,team):
    if team=="myArticles":
        articles = Article.objects.filter(created_date__lte=timezone.now(),author=request.user).order_by('created_date')
    else:
        articles = Article.objects.filter(created_date__lte=timezone.now(),team=team).order_by('created_date')
    return render(request, 'testData/article_list.html', {'articles':articles})

def article_detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    return render(request,'testData/article_detail.html',{'article':article})

@login_required
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

@login_required
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

@login_required
def delete_article(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('article_list')
