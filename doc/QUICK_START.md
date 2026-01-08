# 快速使用指南

## 1. 配置数据库开关

编辑 `dxp_movies_admin/dxp_movies_admin/settings.py`：

```python
# 使用模拟数据（推荐用于开发调试）
USE_REAL_DATABASE = False

# 或使用真实数据库（需要配置数据库连接）
USE_REAL_DATABASE = True
```

## 2. 启动服务

```bash
cd dxp_movies_admin
python manage.py runserver
```

## 3. 测试 API

### 方式一：浏览器访问

在浏览器中打开：
```
http://localhost:8000/movies/get_movies/
```

### 方式二：使用测试脚本

```bash
cd dxp_movies_admin
python test_database_switch.py
```

### 方式三：使用 curl

```bash
# 获取所有电影
curl http://localhost:8000/movies/get_movies/

# 获取电影详情
curl http://localhost:8000/movies/get_movie_detail/?id=1

# 获取所有类型
curl http://localhost:8000/movies/get_types/

# 获取所有导演
curl http://localhost:8000/movies/get_directors/

# 添加电影
curl -X POST http://localhost:8000/movies/add_movie/ \
  -d "title=新电影" \
  -d "rank=100"

# 更新电影
curl -X POST http://localhost:8000/movies/update_movie/ \
  -d "id=1" \
  -d "title=更新后的标题" \
  -d "rank=50"

# 删除电影
curl http://localhost:8000/movies/delete_movie/?id=30
```

## 4. 可用的 API 接口

| 接口 | 方法 | URL | 说明 |
|------|------|-----|------|
| 获取所有电影 | GET | `/movies/get_movies/` | 返回所有电影列表 |
| 获取电影详情 | GET | `/movies/get_movie_detail/?id={id}` | 返回指定电影详情 |
| 获取所有类型 | GET | `/movies/get_types/` | 返回所有电影类型 |
| 获取所有导演 | GET | `/movies/get_directors/` | 返回所有导演信息 |
| 获取所有演员 | GET | `/movies/get_actors/` | 返回所有演员信息 |
| 获取艺恩电影 | GET | `/movies/get_en_movies/` | 返回艺恩电影数据 |
| 添加电影 | POST | `/movies/add_movie/` | 添加新电影 |
| 更新电影 | POST | `/movies/update_movie/` | 更新电影信息 |
| 删除电影 | GET | `/movies/delete_movie/?id={id}` | 删除指定电影 |

## 5. 响应示例

### 获取电影列表

```json
[
  {
    "id": 1,
    "code": 1889243,
    "rank": 12,
    "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.jpg",
    "regions": "美国,英国,加拿大",
    "title": "星际穿越",
    "url": "https://movie.douban.com/subject/1889243/",
    "release_date": "2014-11-12",
    "actor_count": 28,
    "vote_count": 2016530,
    "score": 9.4,
    "en_id": 52
  },
  ...
]
```

### 获取类型列表

```json
[
  {"id": 1, "code": 11, "name": "剧情"},
  {"id": 2, "code": 24, "name": "喜剧"},
  {"id": 3, "code": 5, "name": "动作"},
  {"id": 4, "code": 13, "name": "爱情"},
  {"id": 5, "code": 17, "name": "科幻"},
  {"id": 6, "code": 25, "name": "动画"}
]
```

## 6. 模拟数据说明

- 模拟数据存储在内存中，服务重启后会恢复初始状态
- 当前包含 29 部热门电影数据
- 包含 6 种电影类型
- 包含少量导演和演员示例数据

## 7. 切换到真实数据库

当需要使用真实数据库时：

1. 修改 `settings.py`：
   ```python
   USE_REAL_DATABASE = True
   ```

2. 确保数据库配置正确：
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django_dmPython',
           'NAME': 'DXP_BOXOFFICE',
           'USER': 'SYSDBA',
           'PASSWORD': 'SYSDBA123',
           'HOST': 'localhost',
           'PORT': '5236',
           # ...
       }
   }
   ```

3. 运行数据库迁移：
   ```bash
   python manage.py migrate
   ```

4. 导入初始数据（如果需要）：
   ```bash
   # 使用 dataset 目录下的 SQL 文件
   ```

## 8. 前端集成示例

### JavaScript/Fetch

```javascript
// 获取电影列表
fetch('http://localhost:8000/movies/get_movies/')
  .then(response => response.json())
  .then(data => {
    console.log('电影列表:', data);
  });

// 添加电影
fetch('http://localhost:8000/movies/add_movie/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: 'title=新电影&rank=100'
})
  .then(response => response.text())
  .then(data => {
    console.log('添加结果:', data);
  });
```

### Vue.js/Axios

```javascript
// 获取电影列表
axios.get('http://localhost:8000/movies/get_movies/')
  .then(response => {
    this.movies = response.data;
  });

// 添加电影
axios.post('http://localhost:8000/movies/add_movie/', {
  title: '新电影',
  rank: 100
}, {
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
})
  .then(response => {
    console.log('添加成功:', response.data);
  });
```

## 9. 常见问题

### Q: 为什么我的修改在重启后消失了？
A: 在模拟数据模式下（USE_REAL_DATABASE = False），数据存储在内存中，重启服务会重置数据。

### Q: 如何添加更多模拟数据？
A: 编辑 `movieslib/mock_data.py` 文件，在对应的列表中添加数据。

### Q: 如何确认当前使用的是哪种模式？
A: 可以在视图中添加日志，或查看 `settings.py` 中的 `USE_REAL_DATABASE` 配置。

### Q: CORS 错误怎么办？
A: 已经在 `settings.py` 中配置了 CORS，如果仍有问题，请检查 `corsheaders` 是否正确安装。

## 10. 下一步

- 添加更多 API 接口
- 完善电影详情接口，返回关联的类型、导演、演员信息
- 添加分页功能
- 添加搜索和筛选功能
- 添加数据验证
