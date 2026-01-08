"""
模拟数据模块
当 USE_REAL_DATABASE = False 时使用此模块提供的数据
"""

# 豆瓣电影数据
DOUBAN_MOVIES = [
    {"id": 1, "code": 1889243, "rank": 12, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.jpg", "regions": "美国,英国,加拿大", "title": "星际穿越", "url": "https://movie.douban.com/subject/1889243/", "release_date": "2014-11-12", "actor_count": 28, "vote_count": 2016530, "score": 9.4, "en_id": 52},
    {"id": 2, "code": 1929463, "rank": 48, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1784592701.jpg", "regions": "美国,中国台湾,英国,加拿大", "title": "少年派的奇幻漂流", "url": "https://movie.douban.com/subject/1929463/", "release_date": "2012-11-22", "actor_count": 19, "vote_count": 1424964, "score": 9.1, "en_id": 12},
    {"id": 3, "code": 26752088, "rank": 67, "cover_url": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2561305376.jpg", "regions": "中国大陆", "title": "我不是药神", "url": "https://movie.douban.com/subject/26752088/", "release_date": "2018-07-05", "actor_count": 36, "vote_count": 2237767, "score": 9.0, "en_id": 16},
    {"id": 4, "code": 26387939, "rank": 71, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2401676338.jpg", "regions": "印度", "title": "摔跤吧！爸爸", "url": "https://movie.douban.com/subject/26387939/", "release_date": "2017-05-05", "actor_count": 11, "vote_count": 1661247, "score": 9.0, "en_id": 63},
    {"id": 5, "code": 26683290, "rank": 273, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2910701461.jpg", "regions": "日本", "title": "你的名字。", "url": "https://movie.douban.com/subject/26683290/", "release_date": "2016-12-02", "actor_count": 26, "vote_count": 1516744, "score": 8.5, "en_id": 5},
    {"id": 6, "code": 26100958, "rank": 278, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2550755859.jpg", "regions": "美国", "title": "复仇者联盟4：终局之战", "url": "https://movie.douban.com/subject/26100958/", "release_date": "2019-04-24", "actor_count": 100, "vote_count": 1111468, "score": 8.5, "en_id": 51},
    {"id": 7, "code": 25864085, "rank": 291, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2264592493.jpg", "regions": "英国,美国,匈牙利,约旦", "title": "火星救援", "url": "https://movie.douban.com/subject/25864085/", "release_date": "2015-11-25", "actor_count": 29, "vote_count": 788004, "score": 8.5, "en_id": 2},
    {"id": 8, "code": 26794435, "rank": 334, "cover_url": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2563780504.jpg", "regions": "中国大陆", "title": "哪吒之魔童降世", "url": "https://movie.douban.com/subject/26794435/", "release_date": "2019-07-26", "actor_count": 15, "vote_count": 1883871, "score": 8.4, "en_id": 1},
    {"id": 9, "code": 26277313, "rank": 410, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2255028780.jpg", "regions": "中国大陆", "title": "西游记之大圣归来", "url": "https://movie.douban.com/subject/26277313/", "release_date": "2015-07-10", "actor_count": 16, "vote_count": 707536, "score": 8.3, "en_id": 11},
    {"id": 10, "code": 25765735, "rank": 458, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2445529009.jpg", "regions": "美国", "title": "金刚狼3：殊死一战", "url": "https://movie.douban.com/subject/25765735/", "release_date": "2017-03-03", "actor_count": 27, "vote_count": 437634, "score": 8.3, "en_id": 58},
    {"id": 11, "code": 30166972, "rank": 480, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572166063.jpg", "regions": "中国大陆,中国香港", "title": "少年的你", "url": "https://movie.douban.com/subject/30166972/", "release_date": "2019-10-25", "actor_count": 21, "vote_count": 1516795, "score": 8.2, "en_id": 18},
    {"id": 12, "code": 25662329, "rank": 6, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2323981221.jpg", "regions": "美国", "title": "疯狂动物城", "url": "https://movie.douban.com/subject/25662329/", "release_date": "2016-03-04", "actor_count": 43, "vote_count": 2102236, "score": 9.2, "en_id": 13},
    {"id": 13, "code": 20495023, "rank": 10, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2505426431.jpg", "regions": "美国", "title": "寻梦环游记", "url": "https://movie.douban.com/subject/20495023/", "release_date": "2017-11-24", "actor_count": 25, "vote_count": 1828673, "score": 9.1, "en_id": 61},
    {"id": 14, "code": 11026735, "rank": 33, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2224568669.jpg", "regions": "美国", "title": "超能陆战队", "url": "https://movie.douban.com/subject/11026735/", "release_date": "2015-02-28", "actor_count": 23, "vote_count": 1086766, "score": 8.8, "en_id": 45},
    {"id": 15, "code": 1297995, "rank": 107, "cover_url": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2238467474.jpg", "regions": "美国", "title": "美女与野兽", "url": "https://movie.douban.com/subject/1297995/", "release_date": "1991-09-29", "actor_count": 41, "vote_count": 201975, "score": 8.5, "en_id": 21},
    {"id": 16, "code": 26258779, "rank": 145, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2887887081.jpg", "regions": "美国", "title": "银河护卫队3", "url": "https://movie.douban.com/subject/26258779/", "release_date": "2023-05-05", "actor_count": 62, "vote_count": 548231, "score": 8.3, "en_id": 33},
    {"id": 17, "code": 35725869, "rank": 200, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2901057189.jpg", "regions": "中国大陆", "title": "年会不能停！", "url": "https://movie.douban.com/subject/35725869/", "release_date": "2023-12-29", "actor_count": 31, "vote_count": 961479, "score": 8.1, "en_id": 27},
    {"id": 18, "code": 3233635, "rank": 219, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p877183898.jpg", "regions": "美国", "title": "功夫熊猫2", "url": "https://movie.douban.com/subject/3233635/", "release_date": "2011-05-28", "actor_count": 27, "vote_count": 468261, "score": 8.1, "en_id": 62},
    {"id": 19, "code": 25964071, "rank": 291, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2264377763.jpg", "regions": "中国大陆", "title": "夏洛特烦恼", "url": "https://movie.douban.com/subject/25964071/", "release_date": "2015-09-30", "actor_count": 33, "vote_count": 1062739, "score": 7.9, "en_id": 47},
    {"id": 20, "code": 11589036, "rank": 365, "cover_url": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2265177361.jpg", "regions": "美国,中国大陆", "title": "功夫熊猫3", "url": "https://movie.douban.com/subject/11589036/", "release_date": "2016-01-29", "actor_count": 42, "vote_count": 386348, "score": 7.8, "en_id": 37},
    {"id": 21, "code": 34841067, "rank": 402, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2629056068.jpg", "regions": "中国大陆", "title": "你好，李焕英", "url": "https://movie.douban.com/subject/34841067/", "release_date": "2021-02-12", "actor_count": 41, "vote_count": 1495645, "score": 7.7, "en_id": 15},
    {"id": 22, "code": 6873143, "rank": 428, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2432493858.jpg", "regions": "美国", "title": "一条狗的使命", "url": "https://movie.douban.com/subject/6873143/", "release_date": "2017-03-03", "actor_count": 23, "vote_count": 388968, "score": 7.7, "en_id": 57},
    {"id": 23, "code": 3642835, "rank": 434, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1731774258.jpg", "regions": "美国", "title": "黑衣人3", "url": "https://movie.douban.com/subject/3642835/", "release_date": "2012-05-25", "actor_count": 33, "vote_count": 296449, "score": 7.7, "en_id": 68},
    {"id": 24, "code": 36369452, "rank": 466, "cover_url": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2903066285.jpg", "regions": "中国大陆", "title": "飞驰人生2", "url": "https://movie.douban.com/subject/36369452/", "release_date": "2024-02-10", "actor_count": 20, "vote_count": 710785, "score": 7.6, "en_id": 54},
    {"id": 25, "code": 1652587, "rank": 17, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2180085848.jpg", "regions": "美国", "title": "阿凡达", "url": "https://movie.douban.com/subject/1652587/", "release_date": "2010-01-04", "actor_count": 49, "vote_count": 1502000, "score": 8.8, "en_id": 35},
    {"id": 26, "code": 4920389, "rank": 32, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2516578307.jpg", "regions": "美国", "title": "头号玩家", "url": "https://movie.douban.com/subject/4920389/", "release_date": "2018-03-30", "actor_count": 33, "vote_count": 1446871, "score": 8.6, "en_id": 17},
    {"id": 27, "code": 2973079, "rank": 42, "cover_url": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2219406504.jpg", "regions": "美国,新西兰", "title": "霍比特人3：五军之战", "url": "https://movie.douban.com/subject/2973079/", "release_date": "2015-01-23", "actor_count": 52, "vote_count": 402239, "score": 8.6, "en_id": 41},
    {"id": 28, "code": 23761370, "rank": 56, "cover_url": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2233706697.jpg", "regions": "美国,中国大陆,日本", "title": "速度与激情7", "url": "https://movie.douban.com/subject/23761370/", "release_date": "2015-04-12", "actor_count": 42, "vote_count": 491879, "score": 8.4, "en_id": 39},
    {"id": 29, "code": 3068206, "rank": 67, "cover_url": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1382432968.jpg", "regions": "美国", "title": "碟中谍4", "url": "https://movie.douban.com/subject/3068206/", "release_date": "2012-01-28", "actor_count": 42, "vote_count": 450329, "score": 8.4, "en_id": 36},
]

# 类型数据
TYPE_INFO = [
    {"id": 1, "code": 11, "name": "剧情"},
    {"id": 2, "code": 24, "name": "喜剧"},
    {"id": 3, "code": 5, "name": "动作"},
    {"id": 4, "code": 13, "name": "爱情"},
    {"id": 5, "code": 17, "name": "科幻"},
    {"id": 6, "code": 25, "name": "动画"},
]

# 导演数据（示例数据）
DIRECTOR_INFO = [
    {"id": 1, "code": 27260291, "name": "克里斯托弗·诺兰", "gender": "男", "birth_time": "1970年7月30日", "birth_area": "英国,伦敦", "posiiton": "制片人/编剧/导演/作者", "url": "https://www.douban.com/personage/27260291/", "cover_url": "https://img2.doubanio.com/view/celebrity/m/public/p21241.jpg"},
    {"id": 2, "code": 27223738, "name": "拉斯·霍尔斯道姆", "gender": "男", "birth_time": "1946年6月2日", "birth_area": "瑞典,斯德哥尔摩", "posiiton": "导演/编剧/剪辑", "url": "https://www.douban.com/personage/27223738/", "cover_url": "https://img3.doubanio.com/view/celebrity/m/public/p4333.jpg"},
    {"id": 3, "code": 27298093, "name": "詹姆斯·古恩", "gender": "男", "birth_time": "1966年8月5日", "birth_area": "美国,密苏里州,圣路易斯", "posiiton": "编剧/制片人/演员", "url": "https://www.douban.com/personage/27298093/", "cover_url": "https://img9.doubanio.com/view/personage/m/public/0b93cff6c8a71252496cfa00b84996e6.jpg"},
    {"id": 4, "code": 27548252, "name": "贾玲", "gender": "女", "birth_time": "1982年4月29日", "birth_area": "中国,湖北,襄阳", "posiiton": "演员/编剧/导演", "url": "https://www.douban.com/personage/27548252/", "cover_url": "https://img3.doubanio.com/view/personage/m/public/4dc2b98f1d05c305f5c715d423fcb727.jpg"},
]

# 演员数据（示例数据）
ACTOR_INFO = [
    {"id": 1, "code": 27250747, "name": "佩吉·奥哈拉", "gender": None, "birth_time": "1956年5月10日", "birth_area": "美国,佛罗里达州", "posiiton": "配音/演员", "url": "https://www.douban.com/personage/27250747/", "cover_url": "https://img1.doubanio.com/view/celebrity/m/public/p1490089335.19.jpg"},
    {"id": 2, "code": 27246551, "name": "塔布", "gender": "女", "birth_time": "1970年11月4日", "birth_area": "印度,安得拉,海得拉巴", "posiiton": "演员", "url": "https://www.douban.com/personage/27246551/", "cover_url": "https://img3.doubanio.com/view/celebrity/m/public/p1556895756.37.jpg"},
]

# 艺恩电影数据（示例数据）
EN_MOVIE_INFO = [
    {"id": 1, "code": 1001, "movie_name": "哪吒之魔童降世", "avg_audience_count": 28, "release_time": "2019-07-26", "avg_boxoffice": 35.50, "boxoffice": 5036940000.00, "rank": 1},
    {"id": 2, "code": 1002, "movie_name": "火星救援", "avg_audience_count": 12, "release_time": "2015-11-25", "avg_boxoffice": 38.50, "boxoffice": 609000000.00, "rank": 2},
]

# 电影-类型关系数据（示例数据）
MOVIE_TYPE = [
    {"id": 1, "movie_id": 1, "type_id": 1},  # 星际穿越 - 剧情
    {"id": 2, "movie_id": 1, "type_id": 5},  # 星际穿越 - 科幻
    {"id": 3, "movie_id": 3, "type_id": 1},  # 我不是药神 - 剧情
    {"id": 4, "movie_id": 12, "type_id": 2}, # 疯狂动物城 - 喜剧
    {"id": 5, "movie_id": 12, "type_id": 6}, # 疯狂动物城 - 动画
]

# 电影-导演关系数据（示例数据）
MOVIE_DIRECTOR = [
    {"id": 1, "movie_id": 1, "director_id": 1},  # 星际穿越 - 克里斯托弗·诺兰
    {"id": 2, "movie_id": 21, "director_id": 4}, # 你好，李焕英 - 贾玲
]

# 电影-演员关系数据（示例数据）
MOVIE_ACTOR = [
    {"id": 1, "movie_id": 15, "actor_id": 1},  # 美女与野兽 - 佩吉·奥哈拉
    {"id": 2, "movie_id": 4, "actor_id": 2},   # 摔跤吧！爸爸 - 塔布
]


# 辅助函数：获取下一个ID
def get_next_id(data_list):
    """获取列表中的下一个可用ID"""
    if not data_list:
        return 1
    return max(item['id'] for item in data_list) + 1


# 辅助函数：根据ID查找数据
def find_by_id(data_list, item_id):
    """根据ID在列表中查找数据"""
    for item in data_list:
        if item['id'] == item_id:
            return item
    return None


# 辅助函数：根据ID删除数据
def delete_by_id(data_list, item_id):
    """根据ID在列表中删除数据"""
    for i, item in enumerate(data_list):
        if item['id'] == item_id:
            del data_list[i]
            return True
    return False
