from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Category


def home(request):
    movies = Movie.objects.all()
    return render(request, 'rental/home.html', {'movies': movies, 'categories': categories})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'rental/movie_detail.html', {'movie': movie})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'rental/categories.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    movies = category.movies.all()
    return render(request, 'rental/category_detail.html', {'movies': movies, 'category': category})


def login_view(request):
    return render(request, 'rental/login.html')


# A list to hold downloaded movies
downloads_list = []


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'rental/movie_detail.html', {'movie': movie})


def add_to_downloads(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    downloads = request.session.get('downloads', [])

    # Check if the movie is already in the downloads list
    if movie.title not in downloads:
        downloads.append(movie.title)
        request.session['downloads'] = downloads

    return redirect('downloads')


def downloads(request):
    downloads_list = request.session.get('downloads', [])
    return render(request, 'rental/downloads.html', {'downloads': downloads_list})


def categories(request):
    search_query = request.GET.get('search', '')
    if search_query:
        categories = Category.objects.filter(name__icontains=search_query)
    else:
        categories = Category.objects.all()

    return render(request, 'rental/categories.html', {'categories': categories})


def about(request):
    return render(request, 'rental/about.html')
