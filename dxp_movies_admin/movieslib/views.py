from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .dao import MovieDAO, TypeDAO, DirectorDAO, ActorDAO, EnMovieDAO

# Create your views here.

def get_movies(request):
    """获取所有电影（使用DAO层，根据配置自动选择真实数据库或模拟数据）"""
    dao = MovieDAO()
    movies = dao.get_all_movies()
    return JsonResponse(movies, safe=False)

def delete_movie(request):
    """删除电影"""
    try:
        p_id = request.GET.get('id')
        dao = MovieDAO()
        success = dao.delete_movie(p_id)
        if success:
            return HttpResponse('删除成功！')
        else:
            return HttpResponse('电影不存在')
    except Exception as e:
        return HttpResponse(str(e))
    
def add_movie(request):
    """添加电影"""
    try:
        p_title = request.POST.get('title')
        p_rank = request.POST.get('rank')
        dao = MovieDAO()
        dao.create_movie(title=p_title, rank=int(p_rank) if p_rank else 0)
        return HttpResponse('插入成功')
    except Exception as e:
        return HttpResponse(str(e))
    
def update_movie(request):
    """更新电影"""
    try:
        p_id = request.POST.get('id')
        p_title = request.POST.get('title')
        p_rank = request.POST.get('rank')
        dao = MovieDAO()
        update_data = {}
        if p_title:
            update_data['title'] = p_title
        if p_rank:
            update_data['rank'] = int(p_rank)
        
        success = dao.update_movie(p_id, **update_data)
        if success:
            return HttpResponse('更新成功')
        else:
            return HttpResponse('电影不存在')
    except Exception as e:
        return HttpResponse(str(e))


# ========== 新增API接口 ==========

def get_types(request):
    """获取所有电影类型"""
    dao = TypeDAO()
    types = dao.get_all_types()
    return JsonResponse(types, safe=False)


def get_directors(request):
    """获取所有导演"""
    dao = DirectorDAO()
    directors = dao.get_all_directors()
    return JsonResponse(directors, safe=False)


def get_actors(request):
    """获取所有演员"""
    dao = ActorDAO()
    actors = dao.get_all_actors()
    return JsonResponse(actors, safe=False)


def get_en_movies(request):
    """获取所有艺恩电影"""
    dao = EnMovieDAO()
    en_movies = dao.get_all_en_movies()
    return JsonResponse(en_movies, safe=False)


def get_movie_detail(request):
    """获取电影详情（包含类型、导演、演员等关联信息）"""
    try:
        movie_id = request.GET.get('id')
        if not movie_id:
            return JsonResponse({'error': '缺少电影ID参数'}, status=400)
        
        # 获取电影基本信息
        movie_dao = MovieDAO()
        movie = movie_dao.get_movie_by_id(movie_id)
        
        if not movie:
            return JsonResponse({'error': '电影不存在'}, status=404)
        
        # TODO: 后续可以添加关联信息查询
        # 如：电影的类型、导演、演员等
        
        return JsonResponse(movie, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)