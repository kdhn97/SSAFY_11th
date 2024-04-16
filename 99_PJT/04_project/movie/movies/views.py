from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# 메인화면 기능
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

# 정보생성 기능
def create(request):
    if request.method == 'POST': # 만약 method가 POST라면
        form = MovieForm(request.POST)
        # is_valid() - 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환
        if form.is_valid(): 
            # save() - 데이터베이스 객체를 만들고 저장
            form.save() 
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

# 정보상세페이지 기능
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)

    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)

# 정보수정 기능
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie
    }
    return render(request, 'movies/update.html', context)

# 정보삭제 기능
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')