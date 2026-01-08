from django.urls import path
from . import views

urlpatterns = [
    # 电影相关接口
    path('get_movies/', views.get_movies, name='get_movies'),
    path('get_movie_detail/', views.get_movie_detail, name='get_movie_detail'),
    path('delete_movie/', views.delete_movie, name='delete_movie'),
    path('update_movie', views.update_movie, name='update_movie'),
    path('add_movie', views.add_movie, name='add_movie'),
    
    # 其他数据接口
    path('get_types/', views.get_types, name='get_types'),
    path('get_directors/', views.get_directors, name='get_directors'),
    path('get_actors/', views.get_actors, name='get_actors'),
    path('get_en_movies/', views.get_en_movies, name='get_en_movies'),
]
