from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('movie/<int:movie_id>/', views.movie_detail,
         name='movie_detail'),  # Movie detail page
    path('categories/', views.categories, name='categories'),  # Categories list
    path('categories/<int:category_id>/', views.category_detail,
         name='category_detail'),  # Movies in a category
    path('add-to-downloads/<int:movie_id>/', views.add_to_downloads,
         name='add_to_downloads'),  # Add to downloads
    path('downloads/', views.downloads, name='downloads'),  # Downloads page
    # Other paths...
    path('categories/', views.categories, name='categories'),  # Categories page
    # Other paths...
    path('about/', views.about, name='about'),  # About page
]
