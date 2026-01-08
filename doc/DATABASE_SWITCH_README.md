# 数据库开关配置说明

## 功能概述

后端代码已实现数据库开关功能，可以在不部署真实数据库的情况下调试后端代码。

## 配置方法

在 `dxp_movies_admin/settings.py` 中找到以下配置：

```python
# ================== 数据库开关配置 ==================
# True: 使用真实数据库
# False: 使用模拟数据（无需部署数据库，数据写死在代码中）
USE_REAL_DATABASE = False
# ==================================================
```

### 两种模式

1. **模拟数据模式** (`USE_REAL_DATABASE = False`)
   - 无需部署数据库
   - 数据存储在内存中（重启后数据会重置）
   - 适用于前端开发和后端API调试
   - 数据定义在 `movieslib/mock_data.py` 中

2. **真实数据库模式** (`USE_REAL_DATABASE = True`)
   - 使用真实的达梦数据库
   - 数据持久化存储
   - 适用于生产环境

## 文件结构

```
dxp_movies_admin/
├── dxp_movies_admin/
│   └── settings.py          # 配置文件，包含 USE_REAL_DATABASE 开关
├── movieslib/
│   ├── models.py            # Django 数据模型定义
│   ├── mock_data.py         # 模拟数据（从 dataset/*.sql 提取）
│   ├── dao.py               # 数据访问层，根据开关选择数据源
│   └── views.py             # 视图层，使用 DAO 访问数据
```

## 现有 API 接口

### 1. 获取所有电影
- **URL**: `/movies/get_movies/`
- **方法**: `GET`
- **返回**: JSON 数组，包含所有电影信息

### 2. 删除电影
- **URL**: `/movies/delete_movie/?id={movie_id}`
- **方法**: `GET`
- **参数**: `id` - 电影ID
- **返回**: 删除成功或失败信息

### 3. 添加电影
- **URL**: `/movies/add_movie/`
- **方法**: `POST`
- **参数**: 
  - `title` - 电影名称
  - `rank` - 排名
- **返回**: 插入成功或失败信息

### 4. 更新电影
- **URL**: `/movies/update_movie/`
- **方法**: `POST`
- **参数**: 
  - `id` - 电影ID
  - `title` - 电影名称（可选）
  - `rank` - 排名（可选）
- **返回**: 更新成功或失败信息

## 数据说明

### 模拟数据内容

模拟数据包含以下表的数据：

1. **DOUBAN_MOVIES** - 豆瓣电影信息（29条数据）
   - 包含：星际穿越、我不是药神、疯狂动物城等热门电影

2. **TYPE_INFO** - 电影类型（6条数据）
   - 剧情、喜剧、动作、爱情、科幻、动画

3. **DIRECTOR_INFO** - 导演信息（4条示例数据）
   - 克里斯托弗·诺兰、贾玲等

4. **ACTOR_INFO** - 演员信息（2条示例数据）

5. **EN_MOVIE_INFO** - 艺恩电影信息（2条示例数据）

6. **关系表数据** - 电影与类型、导演、演员的关联关系

### 扩展模拟数据

如需添加更多模拟数据，请编辑 `movieslib/mock_data.py` 文件：

```python
# 添加更多电影数据
DOUBAN_MOVIES.append({
    "id": 30,
    "code": 123456,
    "title": "新电影",
    "rank": 1,
    # ... 其他字段
})
```

## 使用建议

1. **前端开发阶段**: 使用 `USE_REAL_DATABASE = False`
   - 无需配置数据库连接
   - 快速启动和调试
   - 数据可控，便于测试各种场景

2. **后端开发阶段**: 使用 `USE_REAL_DATABASE = False`
   - 专注于业务逻辑开发
   - 无需关心数据库环境问题

3. **集成测试阶段**: 使用 `USE_REAL_DATABASE = True`
   - 测试真实数据库连接
   - 验证数据持久化

4. **生产环境**: 使用 `USE_REAL_DATABASE = True`
   - 使用真实数据库
   - 确保数据安全和持久化

## 注意事项

1. 模拟数据存储在内存中，服务重启后会恢复到初始状态
2. 模拟模式下的增删改操作不会影响真实数据库
3. 切换模式后需要重启 Django 服务才能生效
4. 模拟数据中的 ID 是自动生成的，每次重启后会重置

## 快速开始

1. 确保 `settings.py` 中 `USE_REAL_DATABASE = False`
2. 启动 Django 服务：
   ```bash
   cd dxp_movies_admin
   python manage.py runserver
   ```
3. 访问 API：`http://localhost:8000/movies/get_movies/`
4. 查看返回的电影数据

## 未来扩展

可以根据需要添加更多 DAO 类和 API 接口：

- `TypeDAO` - 类型数据访问
- `DirectorDAO` - 导演数据访问
- `ActorDAO` - 演员数据访问
- `EnMovieDAO` - 艺恩电影数据访问

所有 DAO 类都会自动根据 `USE_REAL_DATABASE` 配置选择数据源。
