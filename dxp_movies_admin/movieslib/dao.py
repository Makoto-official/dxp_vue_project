"""
数据访问层（Data Access Object）
根据 settings.USE_REAL_DATABASE 开关决定使用真实数据库还是模拟数据
"""
from django.conf import settings
from decimal import Decimal


class MovieDAO:
    """电影数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
        
    def get_all_movies(self):
        """获取所有电影"""
        if self.use_real_db:
            from .models import DoubanModel
            return list(DoubanModel.objects.values())
        else:
            from .mock_data import DOUBAN_MOVIES
            return DOUBAN_MOVIES.copy()
    
    def get_movie_by_id(self, movie_id):
        """根据ID获取电影"""
        if self.use_real_db:
            from .models import DoubanModel
            try:
                return DoubanModel.objects.get(id=movie_id)
            except DoubanModel.DoesNotExist:
                return None
        else:
            from .mock_data import find_by_id, DOUBAN_MOVIES
            return find_by_id(DOUBAN_MOVIES, int(movie_id))
    
    def create_movie(self, **kwargs):
        """创建电影"""
        if self.use_real_db:
            from .models import DoubanModel
            movie = DoubanModel.objects.create(**kwargs)
            return movie
        else:
            from .mock_data import DOUBAN_MOVIES, get_next_id
            new_movie = {
                'id': get_next_id(DOUBAN_MOVIES),
                'code': kwargs.get('code'),
                'rank': kwargs.get('rank'),
                'cover_url': kwargs.get('cover_url'),
                'regions': kwargs.get('regions'),
                'title': kwargs.get('title'),
                'url': kwargs.get('url'),
                'release_date': kwargs.get('release_date'),
                'actor_count': kwargs.get('actor_count'),
                'vote_count': kwargs.get('vote_count'),
                'score': kwargs.get('score'),
                'en_id': kwargs.get('en_id'),
            }
            DOUBAN_MOVIES.append(new_movie)
            return new_movie
    
    def update_movie(self, movie_id, **kwargs):
        """更新电影"""
        if self.use_real_db:
            from .models import DoubanModel
            try:
                movie = DoubanModel.objects.get(id=movie_id)
                for key, value in kwargs.items():
                    setattr(movie, key, value)
                movie.save()
                return True
            except DoubanModel.DoesNotExist:
                return False
        else:
            from .mock_data import find_by_id, DOUBAN_MOVIES
            movie = find_by_id(DOUBAN_MOVIES, int(movie_id))
            if movie:
                movie.update(kwargs)
                return True
            return False
    
    def delete_movie(self, movie_id):
        """删除电影"""
        if self.use_real_db:
            from .models import DoubanModel
            try:
                movie = DoubanModel.objects.get(id=movie_id)
                movie.delete()
                return True
            except DoubanModel.DoesNotExist:
                return False
        else:
            from .mock_data import delete_by_id, DOUBAN_MOVIES
            return delete_by_id(DOUBAN_MOVIES, int(movie_id))


class TypeDAO:
    """类型数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_types(self):
        """获取所有类型"""
        if self.use_real_db:
            from .models import TypeModel
            return list(TypeModel.objects.values())
        else:
            from .mock_data import TYPE_INFO
            return TYPE_INFO.copy()


class DirectorDAO:
    """导演数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_directors(self):
        """获取所有导演"""
        if self.use_real_db:
            from .models import DirectorModel
            return list(DirectorModel.objects.values())
        else:
            from .mock_data import DIRECTOR_INFO
            return DIRECTOR_INFO.copy()


class ActorDAO:
    """演员数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_actors(self):
        """获取所有演员"""
        if self.use_real_db:
            from .models import ActorModel
            return list(ActorModel.objects.values())
        else:
            from .mock_data import ACTOR_INFO
            return ACTOR_INFO.copy()


class EnMovieDAO:
    """艺恩电影数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_en_movies(self):
        """获取所有艺恩电影"""
        if self.use_real_db:
            from .models import EnModel
            return list(EnModel.objects.values())
        else:
            from .mock_data import EN_MOVIE_INFO
            return EN_MOVIE_INFO.copy()


class MovieTypeDAO:
    """电影-类型关系数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_movie_types(self):
        """获取所有电影-类型关系"""
        if self.use_real_db:
            from .models import MovieTypeModel
            return list(MovieTypeModel.objects.values())
        else:
            from .mock_data import MOVIE_TYPE
            return MOVIE_TYPE.copy()
    
    def get_types_by_movie(self, movie_id):
        """根据电影ID获取类型"""
        if self.use_real_db:
            from .models import MovieTypeModel
            return list(MovieTypeModel.objects.filter(movie_id=movie_id).values())
        else:
            from .mock_data import MOVIE_TYPE
            return [mt for mt in MOVIE_TYPE if mt['movie_id'] == int(movie_id)]


class MovieDirectorDAO:
    """电影-导演关系数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_movie_directors(self):
        """获取所有电影-导演关系"""
        if self.use_real_db:
            from .models import MovieDirectorModel
            return list(MovieDirectorModel.objects.values())
        else:
            from .mock_data import MOVIE_DIRECTOR
            return MOVIE_DIRECTOR.copy()
    
    def get_directors_by_movie(self, movie_id):
        """根据电影ID获取导演"""
        if self.use_real_db:
            from .models import MovieDirectorModel
            return list(MovieDirectorModel.objects.filter(movie_id=movie_id).values())
        else:
            from .mock_data import MOVIE_DIRECTOR
            return [md for md in MOVIE_DIRECTOR if md['movie_id'] == int(movie_id)]


class MovieActorDAO:
    """电影-演员关系数据访问对象"""
    
    def __init__(self):
        self.use_real_db = getattr(settings, 'USE_REAL_DATABASE', True)
    
    def get_all_movie_actors(self):
        """获取所有电影-演员关系"""
        if self.use_real_db:
            from .models import MovieActorModel
            return list(MovieActorModel.objects.values())
        else:
            from .mock_data import MOVIE_ACTOR
            return MOVIE_ACTOR.copy()
    
    def get_actors_by_movie(self, movie_id):
        """根据电影ID获取演员"""
        if self.use_real_db:
            from .models import MovieActorModel
            return list(MovieActorModel.objects.filter(movie_id=movie_id).values())
        else:
            from .mock_data import MOVIE_ACTOR
            return [ma for ma in MOVIE_ACTOR if ma['movie_id'] == int(movie_id)]
