"""
抓取多页网易地产要闻的数据
"""
import csv
import requests
from lxml import etree


# 定义获取数据的函数
def get_home_data(pages):
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
        "_ntes_nnid": "d1802d854cfd17d973b45b17e37782b8,1775798558348",
        "_ntes_nuid": "d1802d854cfd17d973b45b17e37782b8",
        "timing_user_id": "time_XnnISZSsGf",
        "_ga": "GA1.1.1593732914.1777382281",
        "_clck": "1yjllqb%5E2%5Eg5n%5E0%5E2309",
        "_ga_C6TGHFPQ1H": "GS2.1.s1777550765$o2$g1$t1777550792$j33$l0$h0",
        "pver_n_f_l_n3": "a",
        "vjuids": "-1942cf780.19df6cd448c.0.1f0b4869c81398",
        "vjlast": "1777962141.1777962141.30",
        "WM_NI": "UoG3m3iGBGL65x9yAWNwgnDnVyEQePFDdVCbyDhbpmtRPORu8ZsL3rRztE7ERiz%2FAZ3QCseCtvUnuBhzVXDCot5NA%2BXqXa0Isnc14OvT20VXoIIfeuOQ5lwudSdyi%2BTcdXE%3D",
        "WM_NIKE": "9ca17ae2e6ffcda170e2e6eeb4c42195a7fd94e673a5928aa7c84b979f9eacd765b7e7c091cf43b0b1858ef02af0fea7c3b92a97b189d4f039ab998ea8cf3ef7a8f79ac45d8ea9a98fc76696a78bb2e85c869cacb7c26abb9ca883f367b88ea0b0d17ffc86bdadb27a92a6bca6b64f92b7b6d0c452f18f8d94e849b8aa9b8ff84aaca69ab9c749adacfbafc4219caf9882b343b1b2add2b745b68cfed1d554ad978787e87f8d8ffb8df67fa88dac9aec2198bdacb9c837e2a3",
        "WM_TID": "723t5JOoXZdBERFEUEPC9vospbY15Lj3",
        "Hm_lvt_db91d2aef1b333f155cccbb9496c8424": "1777961081,1777967023",
        "Hm_lpvt_db91d2aef1b333f155cccbb9496c8424": "1777967023",
        "HMACCOUNT": "D95B324C32F62368",
        "ne_analysis_trace_id": "1777967035435",
        "s_n_f_l_n3": "08fa9f00fbb7baa51777967035436",
        "_antanalysis_s_id": "1777967035629",
        "UserProvince": "%u5168%u56FD",
        "vinfo_n_f_l_n3": "08fa9f00fbb7baa5.1.1.1777960993707.1777962218415.1777967038140"
    }

    # 定义列表保存每页中所有的数据
    home_data_list = []

    # 循环遍历抓取多页数据
    for page in range(1, pages + 1):

        # 判断是否为第一页数据
        if page == 1:
            # 定义第一页的网址
            page_url = "https://cs.house.163.com/special/021198NN/DCTT.html"
        else:
            # 定义后面页数的网址
            page_url = f"https://cs.house.163.com/special/021198NN/DCTT_{page:02}.html"

        # print(page_url)

        # 发起网络请求，并获取服务器响应
        response = requests.get(page_url, headers=headers, cookies=cookies)
        # print(response.text)

        # 转换成树形结构
        html_tree = etree.HTML(response.text)

        # 筛选出所有的地产信息节点
        home_info_list = html_tree.xpath('//div[@class="ep-content-main"]/div[@class="list-item clearfix"]')
        # print(len(home_info_list), home_info_list)

        # 遍历出每个地产信息标签节点
        for home_info in home_info_list:
            # print(home_info)

            # 从当前地产信息标签节点中筛选出标题
            home_title = home_info.xpath('./h2/a/text()')[0]
            print('标题：', home_title)

            # 从当前地产信息标签节点中筛选出详情页链接
            home_url = home_info.xpath('./h2/a/@href')[0]
            print('网页：', home_url)

            # 从当前地产信息标签节点中筛选出图片链接
            image_url = home_info.xpath('./a/img/@src')[0]
            print('图片：', image_url)

            # 从当前地产信息标签节点中筛选出发布时间
            home_time = home_info.xpath('./p/span/text()')[0]
            print('时间：', home_time)

            # 打印间隔
            print('=' * 75)

            # 将筛选的结果以列表的格式追加到汇总的列表中
            home_data_list.append([home_title, home_url, image_url, home_time])

        # 抓取一页数据后打印提示
        print(f'第{page}页数据抓取完毕')

    # 返回汇总的列表
    return home_data_list


# 定义保存数据的函数
def sava_home_data(home_data_list):
    # 创建csv文件
    with open('网易地产要闻.csv', 'w', newline='', encoding='utf-8-sig') as file:
        # 绑定写入对象
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['标题', '网页', '图片', '时间'])
        # 写入多行数据
        writer.writerows(home_data_list)


if __name__ == '__main__':
    # 从键盘输入抓取的页数
    pages = int(input('请输入抓取的页数：'))

    # 调用get_home_data函数获取多页数据
    home_data_list = get_home_data(pages)

    # 调用sava_home_data函数保存数据
    sava_home_data(home_data_list)
