"""
抓取下厨房网站里的菜谱信息
"""
import csv
import requests
from lxml import etree


# 定义抓取菜谱的函数
def get_recipe_data(pages):
    # 定义请求头
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://www.xiachufang.com/explore/menu/collect/",
        "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    # 定义cookie信息
    cookies = {
        "bid": "0IyugaxK",
        "__utmz": "177678124.1777361689.1.1.utmcsr=hao123.com|utmccn=(referral)|utmcmd=referral|utmcct=/link/https/",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219dd3031b7bc29-08521be5c6e89e8-26061e51-1474560-19dd3031b7c1d3d%22%2C%22%24device_id%22%3A%2219dd3031b7bc29-08521be5c6e89e8-26061e51-1474560-19dd3031b7c1d3d%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
        "Hm_lvt_ecd4feb5c351cc02583045a5813b5142": "1777361689,1777533136,1777539078",
        "HMACCOUNT": "D95B324C32F62368",
        "__utma": "177678124.1660430106.1777361689.1777533136.1777539078.3",
        "__utmc": "177678124",
        "__utmt": "1",
        "Hm_lpvt_ecd4feb5c351cc02583045a5813b5142": "1777539127",
        "__utmb": "177678124.14.9.1777539127534"
    }

    # 定义一个列表用于保存所有菜谱的信息
    recipe_data_list = []

    for page in range(1, pages+1):
        # 定义请求的网址
        # url = "https://www.xiachufang.com/recipe_list/102801533/"
        # url = "https://www.xiachufang.com/recipe_list/104448087/"
        url = f"https://www.xiachufang.com/recipe_list/104448087/?page={page}"

        # 发起网络请求
        response = requests.get(url, headers=headers, cookies=cookies)
        # print(response.text)

        # 转换成树形结构
        html_tree = etree.HTML(response.text)

        # 筛选出所有菜谱的节点数据
        recipes_info_list = html_tree.xpath('//ul[@class="plain"]/li/div')
        # print(len(recipes_info_list), recipes_info_list)

        # 遍历出每个菜谱的节点数据
        for recipe_info in recipes_info_list:
            # print(recipe_info)

            # 筛选出每个菜谱的标题
            recipe_title = recipe_info.xpath('./div[2]/p[1]/a/text()')[0]
            print('菜谱标题：', recipe_title)

            # 筛选出每个菜谱的食材
            recipe_ingredients_list = recipe_info.xpath('./div[2]/p[2]/text()')

            # 对食材列表进行处理，转换成字符串
            recipe_ingredients = ''.join(recipe_ingredients_list)

            # 去除字符串中的换行和空格
            recipe_ingredients = recipe_ingredients.replace('\n', '').replace(' ', '')
            print('菜谱食材：', recipe_ingredients)

            # 筛选出每个菜谱的评分
            recipe_score_list = recipe_info.xpath('./div[2]/p[3]//text()')

            # 对评分列表进行处理，转换成字符串
            recipe_score = ''.join(recipe_score_list)

            # 去除字符串中的换行和空格
            recipe_score = recipe_score.replace('\n', '').replace(' ', '')
            print('菜谱评分：', recipe_score)

            # 筛选出每个菜谱的作者名称
            recipe_author = recipe_info.xpath('./div[2]/p[4]/text()')[0]

            # 去除字符串中的换行和空格
            recipe_author = recipe_author.replace('\n', '').replace(' ', '')
            print('菜谱作者：', recipe_author)

            # 筛选出每个菜谱的网址
            recipe_url = recipe_info.xpath('./div[2]/p[1]/a/@href')[0]

            # 补全网址前面的域名
            recipe_url = 'https://www.xiachufang.com/' + recipe_url
            print('菜谱网址：', recipe_url)

            # 打印间隔
            print('=' * 75)

            # 将筛选的结果打包成一个列表
            recipe_data_list.append([recipe_title, recipe_ingredients, recipe_score, recipe_author, recipe_url])

    # 返回所有菜谱的信息
    return recipe_data_list


# 定义保存菜谱的函数
def sava_recipe_data(recipe_data_list):
    # 创建csv文件
    with open('下厨房菜谱.csv', 'w', newline='', encoding='utf-8-sig') as file:
        # 绑定写入对象
        writer = csv.writer(file)
        # 写入标题行
        writer.writerow(['标题', '食材', '评分', '作者', '网址'])
        # 写入多行数据
        writer.writerows(recipe_data_list)


if __name__ == '__main__':
    # 从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))

    # 调用get_recipe_data函数获取数据
    recipe_data_list = get_recipe_data(pages)

    # 调用sava_recipe_data函数保存数据
    sava_recipe_data(recipe_data_list)
