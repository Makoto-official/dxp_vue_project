"""
数据库开关功能测试脚本

使用方法：
1. 确保 Django 服务已启动
2. 运行此脚本：python test_database_switch.py
"""

import requests
import json

BASE_URL = "http://localhost:8000/movies"


def test_get_movies():
    """测试获取所有电影"""
    print("\n========== 测试获取所有电影 ==========")
    url = f"{BASE_URL}/get_movies/"
    response = requests.get(url)
    
    if response.status_code == 200:
        movies = response.json()
        print(f"✓ 成功获取 {len(movies)} 部电影")
        if movies:
            print(f"  示例电影: {movies[0].get('title', 'N/A')}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def test_get_types():
    """测试获取所有类型"""
    print("\n========== 测试获取所有类型 ==========")
    url = f"{BASE_URL}/get_types/"
    response = requests.get(url)
    
    if response.status_code == 200:
        types = response.json()
        print(f"✓ 成功获取 {len(types)} 个类型")
        print(f"  类型列表: {', '.join([t.get('name', 'N/A') for t in types])}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def test_get_directors():
    """测试获取所有导演"""
    print("\n========== 测试获取所有导演 ==========")
    url = f"{BASE_URL}/get_directors/"
    response = requests.get(url)
    
    if response.status_code == 200:
        directors = response.json()
        print(f"✓ 成功获取 {len(directors)} 位导演")
        if directors:
            print(f"  示例导演: {directors[0].get('name', 'N/A')}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def test_get_actors():
    """测试获取所有演员"""
    print("\n========== 测试获取所有演员 ==========")
    url = f"{BASE_URL}/get_actors/"
    response = requests.get(url)
    
    if response.status_code == 200:
        actors = response.json()
        print(f"✓ 成功获取 {len(actors)} 位演员")
        if actors:
            print(f"  示例演员: {actors[0].get('name', 'N/A')}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def test_add_movie():
    """测试添加电影"""
    print("\n========== 测试添加电影 ==========")
    url = f"{BASE_URL}/add_movie/"
    data = {
        'title': '测试电影',
        'rank': 999
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print(f"✓ 添加电影成功: {response.text}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def test_get_movie_detail():
    """测试获取电影详情"""
    print("\n========== 测试获取电影详情 ==========")
    url = f"{BASE_URL}/get_movie_detail/?id=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie = response.json()
        print(f"✓ 成功获取电影详情")
        print(f"  电影名: {movie.get('title', 'N/A')}")
        print(f"  评分: {movie.get('score', 'N/A')}")
        print(f"  地区: {movie.get('regions', 'N/A')}")
    else:
        print(f"✗ 请求失败: {response.status_code}")


def main():
    print("=" * 50)
    print("数据库开关功能测试")
    print("=" * 50)
    print("\n提示：请确保 Django 服务已在 http://localhost:8000 上运行")
    print("提示：请检查 settings.py 中 USE_REAL_DATABASE 的配置")
    
    try:
        # 运行所有测试
        test_get_movies()
        test_get_types()
        test_get_directors()
        test_get_actors()
        test_get_movie_detail()
        test_add_movie()
        
        print("\n" + "=" * 50)
        print("测试完成！")
        print("=" * 50)
        
    except requests.exceptions.ConnectionError:
        print("\n✗ 连接失败：请确保 Django 服务已启动")
        print("  启动命令: cd dxp_movies_admin && python manage.py runserver")
    except Exception as e:
        print(f"\n✗ 测试过程中出现错误: {str(e)}")


if __name__ == "__main__":
    main()
