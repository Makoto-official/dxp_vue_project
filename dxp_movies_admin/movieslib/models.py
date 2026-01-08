from django.db import models

# Create your models here.

# 豆瓣电影
class DoubanModel(models.Model):
    id= models.AutoField('主键id,自增', primary_key=True)
    code = models.IntegerField('豆瓣电影code',null=True)
    rank = models.IntegerField('排名')
    cover_url = models.CharField('封面链接', max_length=300,null=True)
    regions = models.CharField('区域，多个区域用逗号隔开', max_length=300,null=True)
    title = models.CharField('电影名', max_length=300)
    url = models.CharField('电影链接', max_length=300,null=True)
    release_date = models.CharField('上映时间', max_length=10,null=True)
    actor_count = models.IntegerField('演员人数',null=True)
    vote_count = models.IntegerField('投票人数',null=True)
    score = models.DecimalField('评分',max_digits=3, decimal_places=1,null=True)
    en_id = models.IntegerField('艺恩电影id',null=True)
    class Meta:
        db_table = 'douban_movie_info'

# 类型模型
class TypeModel(models.Model):
    id = models.AutoField('主键id,自增', primary_key=True)
    code = models.IntegerField('类型code,豆瓣获取')
    name = models.CharField('类型名称', max_length=10, null=False)
    class Meta:
        db_table='type_info'

# 导演模型
class DirectorModel(models.Model):
    id = models.AutoField('主键id,自增', primary_key=True)
    code = models.IntegerField('导演code,豆瓣获取')
    name = models.CharField('姓名', max_length=100)
    gender = models.CharField('性别',max_length=1, default='男', null=True)
    birth_time = models.CharField('出生年月', max_length=15, null=True)
    birth_area = models.CharField('出生地', max_length=200, null=True)
    posiiton = models.CharField('职业', max_length=200, null=True)
    url = models.CharField('豆瓣主页', max_length=200, null=True)
    cover_url = models.CharField('封面链接', max_length=200, null=True)
    class Meta:
       db_table='director_info'


# 演员模型
class ActorModel(models.Model):
    id = models.AutoField('主键id,自增', primary_key=True)
    code = models.IntegerField('演员code，豆瓣获取')
    name = models.CharField('姓名', max_length=100)
    gender = models.CharField('性别',max_length=1,default='男', null=True)
    birth_time = models.CharField('出生年月', max_length=15, null=True)
    birth_area = models.CharField('出生地', max_length=200, null=True)
    posiiton = models.CharField('职业', max_length=200, null=True)
    url = models.CharField('豆瓣主页', max_length=200, null=True)
    cover_url = models.CharField('封面链接', max_length=200, null=True)
    class Meta:
       db_table='actor_info'

# 艺恩电影模型
class EnModel(models.Model):
    id = models.AutoField('主键id, 自增', primary_key=True)
    code = models.IntegerField('电影code，艺恩获取')
    movie_name = models.CharField('电影名', max_length=50)
    avg_audience_count = models.IntegerField('场均人次')
    release_time = models.CharField('上映时间', max_length=10)
    avg_boxoffice = models.DecimalField('平均票价', max_digits=5, decimal_places=2)
    boxoffice = models.DecimalField('累计票房',max_digits=20, decimal_places=2)
    rank = models.IntegerField('排名')
    class Meta:
       db_table='en_movie_info'

# 电影_类型中间表
class MovieTypeModel(models.Model):
    id = models.AutoField('主键', primary_key=True)
    movie_id = models.ForeignKey('DoubanModel', to_field='id', db_column='movie_id', on_delete=models.CASCADE)
    type_id = models.ForeignKey('TypeModel', to_field='id', db_column='type_id', on_delete=models.CASCADE)
    class Meta:
        db_table = 'movie_type'

# 电影_导演中间表
class MovieDirectorModel(models.Model):
    id = models.AutoField('主键', primary_key=True)
    movie_id = models.ForeignKey('DoubanModel',to_field='id', db_column='movie_id', on_delete=models.CASCADE)
    director_id = models.ForeignKey('DirectorModel',to_field='id', db_column='director_id', on_delete=models.CASCADE)
    class Meta:
        db_table = 'movie_director'

# 电影_演员中间表
class MovieActorModel(models.Model):
    id = models.AutoField('主键', primary_key=True)
    movie_id = models.ForeignKey('DoubanModel',db_column='movie_id', on_delete=models.CASCADE)
    actor_id = models.ForeignKey('ActorModel',db_column='actor_id',on_delete=models.CASCADE)
    class Meta:
        db_table = 'movie_actor'