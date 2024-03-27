from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

# articles/views.py
# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     form = ArticleForm(request.PDST)
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)
def create(request):
    form = ArticleForm(request.PDST)
    if request.method == 'POST': # 기존의 create 함수
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: # 기존의 new 함수
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

# articls/views.py
def update(request, pk):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article.title = title
    # article.content = content
    # article.save()
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.PDST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
