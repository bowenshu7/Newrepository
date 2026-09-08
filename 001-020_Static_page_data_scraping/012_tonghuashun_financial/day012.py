"""
抓取多页同花顺财经要闻数据
"""
import csv
import requests
from lxml import etree


# 定义一个抓取数据的函数
def get_financial_data(pages):
    # 定义请求头
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    # 定义cookie字典
    cookies = {
        "Hm_lvt_69929b9dce4c22a060bd22d703b2a280": "1778046554",
        "_ga": "GA1.1.1687363882.1778046556",
        "Hm_lvt_722143063e4892925903024537075d0d": "1778046565",
        "Hm_lvt_929f8b362150b1f77b477230541dbbc2": "1778046565",
        "_ga_H2RK0R0681": "GS2.1.s1778046555$o1$g1$t1778046585$j30$l0$h0",
        "log": "",
        "Hm_lvt_9d25c03aef06fec6abea265b79509ba4": "1778046592,1778056540",
        "HMACCOUNT": "D95B324C32F62368",
        "Hm_lvt_05d5f2837ec9bbcd2d0f732c048f3b32": "1778046592,1778056540",
        "Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1": "1778046565,1778056540",
        "Hm_lvt_f79b64788a4e377c608617fba4c736e2": "1778046592,1778056540",
        "Hm_lpvt_f79b64788a4e377c608617fba4c736e2": "1778056556",
        "Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1": "1778056557",
        "Hm_lpvt_9d25c03aef06fec6abea265b79509ba4": "1778056557",
        "Hm_lpvt_05d5f2837ec9bbcd2d0f732c048f3b32": "1778056557",
        "v": "A3x-fvnHOfWpSQ0p-4GA784YTRErdSCTohk0Y1b9iGdKIRIPfoXwL_IpBPul"
    }

    # 定义保存多页数据的二维列表
    financial_data_list = []

    # 定义循环遍历抓取的页数
    for page in range(1, pages + 1):
        # 格式化多页请求的网址
        page_url = f'https://news.10jqka.com.cn/today_list/index_{page}.shtml'

        # 发起网络请求获取响应
        response = requests.get(page_url, headers=headers, cookies=cookies)
        # print(response.text)

        # 转换成树形结构
        html_tree = etree.HTML(response.text)

        # 筛选出所有财经要闻的节点标签
        financial_info_list = html_tree.xpath('//div[@class="list-con"]/ul/li')
        # print(len(financial_info_list), financial_info_list)

        # 循环遍历出每个财经要闻的节点标签
        for financial_info in financial_info_list:
            # print(financial_info)

            # 从当前财经要闻节点中筛选出标题
            financial_title = financial_info.xpath('./span/a/text()')[0]
            print('标题：', financial_title)

            # 从当前财经要闻节点中筛选出链接
            financial_url = financial_info.xpath('./span/a/@href')[0]
            print('链接：', financial_url)

            # 从当前财经要闻节点中筛选出发布时间
            financial_time = financial_info.xpath('./span/span/text()')[0]
            print('时间：', financial_time)

            # 从当前财经要闻节点中筛选出简介
            financial_text = financial_info.xpath('./a/text()')[0]
            print('简介：', financial_text)

            # 打印间隔
            print('=' * 75)

            # 将筛选出来的数据打包成列表，并添加到汇总的列表中
            financial_data_list.append([financial_title, financial_url, financial_time, financial_text])

        # 打印提示
        print(f'第{page}页数据抓取完毕')

    # 返回汇总的列表数据
    return financial_data_list


# 定义保存数据的函数
def sava_financial_data(financial_data_list):
    # 创建一个csv文件
    with open('同花顺财经要闻.csv', 'w', encoding='utf-8', newline='') as file:
        # 绑定csv写入对象
        writer = csv.writer(file)
        # 设置csv文件的表头
        writer.writerow(['标题', '链接', '时间', '简介'])
        # 写入多行数据
        writer.writerows(financial_data_list)

    # 保存提示
    print('【同花顺财经要闻.csv】保存成功')


if __name__ == '__main__':
    # 从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))

    # 调用get_financial_data函数获取多页数据
    financial_data_list = get_financial_data(pages)
    # 调用sava_financial_data函数保存数据
    sava_financial_data(financial_data_list)
