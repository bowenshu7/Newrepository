"""
抓取 IT 之家的博客信息，并保存到csv文件中
"""
import csv
import requests
from lxml import etree


# 定义获取数据的函数
def get_blog_data():
    # 定义请求头
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    # 定义cookie信息
    cookies = {
        "Hm_lvt_f2d5cbe611513efcf95b7f62b934c619": "1777360151",
        "Hm_lvt_cfebe79b2c367c4b89b285f412bf9867": "1777357033,1777452309",
        "HMACCOUNT": "D95B324C32F62368",
        "Hm_lpvt_cfebe79b2c367c4b89b285f412bf9867": "1777452313"
    }

    # 定义请求的网址
    url = "https://www.ithome.com/blog/"

    # 发起网络请求
    response = requests.get(url, headers=headers, cookies=cookies)
    # print(response.text)

    # 转换成树形结构
    html_tree = etree.HTML(response.text)

    # 筛选出所有博客信息的节点标签
    blog_info_list = html_tree.xpath('//ul[@class="bl"]/li')
    # print(len(blog_info_list), blog_info_list)

    # 定义一个列表用于保存所有数据
    blog_data_list = []

    # 遍历出每个博客信息的节点标签
    for blog_info in blog_info_list:
        # print(blog_info)

        # 从当前的博客节点标签中筛选出标题
        blog_title = blog_info.xpath('./div/h2/a/text()')[0]
        print('博客标题：', blog_title)

        # 从当前的博客节点标签中筛选出简介
        blog_text_list = blog_info.xpath('./div/div[@class="m"]/text()')

        # 判断是否筛选到结果
        # if blog_text_list:
        #     # 如果不是空列表，就取出字符串数据
        #     blog_text = blog_text_list[0]
        # else:
        #     blog_text = '简介为空'

        # 使用三元表达式来简化代码
        blog_text = blog_text_list[0] if blog_text_list else '简介为空'
        print('博客简介：', blog_text)

        # 从当前的博客节点标签中筛选出标签
        blog_tags_list = blog_info.xpath('./div/div[@class="o"]/div[@class="tags"]/a//text()')
        # print(blog_tags_list)

        # 将列表数据转换成字符串
        blog_tags = ', '.join(blog_tags_list) if blog_tags_list else '标签为空'
        print('博客标签：', blog_tags)

        # 从当前的博客节点标签中筛选出发布时间
        blog_time = blog_info.xpath('./div/div[@class="o"]/div[@class="d"]/span/text()')[0]
        print('发布时间：', blog_time)

        # 从当前的博客节点标签中筛选出链接
        blog_url = blog_info.xpath('./a/@href')[0]
        print('发布时间：', blog_url)

        # 打印间隔
        print('=' * 75)

        # 将筛选的结果打包成列表，并添加到汇总的列表中
        blog_data_list.append([blog_title, blog_text, blog_tags, blog_time, blog_url])

    # 返回汇总的列表数据
    return blog_data_list


# 定义保存数据的函数
def save_blog_data(blog_data_list):
    with open('IT之家的博客信息.csv', 'w', newline='', encoding='utf-8-sig') as file:
        # 绑定csv写入对象
        writer = csv.writer(file)
        # 写入表头信息
        writer.writerow(['标题', '简介', '标签', '时间', '链接'])
        # 写入多行数据
        writer.writerows(blog_data_list)


if __name__ == '__main__':
    # 调用get_blog_data函数获取数据
    blog_data_list = get_blog_data()

    # 调用save_blog_data函数保存数据
    save_blog_data(blog_data_list)
