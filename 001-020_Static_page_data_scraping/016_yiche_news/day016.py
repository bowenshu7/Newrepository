"""
抓取易车网全部汽车文章数据
"""
import csv
import time
import requests
from lxml import etree


# 定义抓取数据的函数
def get_news_data(pages):
    # 定义请求头
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    }

    # 定义cookie字典
    cookies = {
        "CIGUID": "02d14a03-fb2e-4b36-97e3-63494de23457",
        "selectcity": "430100",
        "selectcityid": "1301",
        "selectcityName": "%E9%95%BF%E6%B2%99",
        "selectcityPinyin": "changsha",
        "auto_id": "fb1f179b66283380bbab4669101989f9",
        "CIGDCID": "tKrJiDKscE6j3XXymGMx2CcpsBBektJG",
        "UserGuid": "02d14a03-fb2e-4b36-97e3-63494de23457",
        "suid": "mw3b7jfe0jqykbatpjnr83nda25b1ozx",
        "locatecity": "430100",
        "bitauto_ipregion": "2408%3A8352%3A444%3A78c0%3A7879%3Ab1cf%3A9745%3Af941%3A%E6%B9%96%E5%8D%97%E7%9C%81%E9%95%BF%E6%B2%99%E5%B8%82%3B1301%2C%E9%95%BF%E6%B2%99%E5%B8%82%2Cchangsha",
        "isWebP": "true",
        "Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44": "1778479231,1778572130,1778660029",
        "HMACCOUNT": "D95B324C32F62368",
        "pageCount": "2",
        "report-cookie-id": "286350685_1778660039150",
        "Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44": "1778660052"
    }

    # 定义汇总的列表
    news_data_list = []

    # 循环格式化网址
    for page in range(1, pages + 1):

        # 定义请求的网址
        page_url = f"https://news.yiche.com/info/categoryId0_p0_l0_f0_g0_c0_b0_{page}.html"
        print(page_url)

        # 发起网络请求，获取响应
        response = requests.get(page_url, headers=headers, cookies=cookies)
        # print(response.text)

        # 转换成树形结构
        html_tree = etree.HTML(response.text)

        # 筛选出所有文章的节点数据
        car_news_list = html_tree.xpath('//div[@class="article-list"]/div')
        # print(len(car_news_list), car_news_list)

        # 遍历出每个汽车的文章节点
        for car_news in car_news_list:
            # print(car_news)

            # 从当前汽车文章节点中筛选出标题
            news_title = car_news.xpath('./div/div/h2/a/text()')[0]
            print('标题：', news_title)

            # 从当前汽车文章节点中筛选出网址
            news_url = car_news.xpath('./div/div/h2/a/@href')[0]

            # 补齐协议和域名部分
            news_url = 'https://news.yiche.com' + news_url
            print('链接：', news_url)

            # 从当前汽车文章节点中筛选出新闻简介
            news_text = car_news.xpath('./div/div/p/text()')

            # 判断是否存在简介
            news_text = news_text[0] if news_text else '简介为空'
            print('简介：', news_text)

            # 从当前汽车文章节点中筛选出新闻作者
            news_author = car_news.xpath('./div/div/div/div/a/text()')[0]
            print('作者：', news_author)

            # 从当前汽车文章节点中筛选出新闻时间
            news_time = car_news.xpath('./div/div/div/div/span/text()')[0]
            print('时间：', news_time)

            # 将筛选的结果打包成一个列表, 并追加到汇总的列表中
            news_data_list.append([news_title, news_url, news_text, news_author, news_time])

            # 打印间隔
            print('=' * 75)

        # 抓取一页数据后打印提示
        print(f'第{page}页数据抓取完毕')

        # 增加等待，方式反爬
        time.sleep(1)

    # 返回汇总的列表
    return news_data_list


# 定义保存数据的函数
def sava_news_data(news_data_list):
    # 创建csv文件
    with open('易车新闻数据.csv', 'w', encoding='utf-8-sig', newline='') as file:
        # 对创建的文件绑定写入对象
        writer = csv.writer(file)
        # 写入表头信息
        writer.writerow(['标题', '链接', '简介', '作者', '时间'])
        # 将所有的汽车新闻信息写入到csv文件中
        writer.writerows(news_data_list)

    print('【易车新闻数据.csv】保存成功')


if __name__ == '__main__':
    # 从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))

    # 调用get_news_data函数获取数据，并接收返回值
    news_data_list = get_news_data(pages)

    # 调用sava_news_data函数保存数据
    sava_news_data(news_data_list)
