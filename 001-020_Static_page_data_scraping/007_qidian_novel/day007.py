import requests
from lxml import etree

# 定义请求头
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.qidian.com/finish/vip0/",
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

# 定义cookie字典
cookies = {
    "e1": "%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A17%22%7D",
    "e2": "%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D",
    "newstatisticUUID": "1775738744_37784929",
    "fu": "623259667",
    "abPolicies": "%7B%22g17%22%3A1%2C%22g16%22%3A0%2C%22g18%22%3A1%2C%22g19%22%3A1%2C%22g14%22%3A1%7D",
    "supportwebp": "true",
    "supportWebp": "true",
    "traffic_search_engine": "",
    "_csrfToken": "fce7d350-b70e-4866-b87b-4deb4e11dd66",
    "x-waf-captcha-referer": "",
    "traffic_utm_referer": "",
    "Hm_lvt_f00f67093ce2f38f215010b699629083": "1775738750,1777095846,1777095965,1777193795",
    "HMACCOUNT": "D95B324C32F62368",
    "Hm_lpvt_f00f67093ce2f38f215010b699629083": "1777193813",
    "w_tsfp": "ltvuV0MF2utBvS0Q7q3onUimFDEudzw4h0wpEaR0f5thQLErU5mC1odzvcP1OXzc5cxnvd7DsZoyJTLYCJI3dwMRQp/AId8SjQyYxokj1Y5BAEJkQs/YXlBOI+p96TEUKnhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5W7V5Aj5L1IhAbIQ0UWbhCgcXXh15hO/JboONEmuKs+rSqA="
}

# 定义小说首页网址
url = "https://www.qidian.com/book/1048498623/"

# 发起网络请求
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 筛选出小说的名称
book_title = html_tree.xpath('//h1[@id="bookName"]/text()')[0]
print(book_title)

# 筛选出所有章节的节点
chapter_info_list = html_tree.xpath('//ul[@class="volume-chapters"]/li')
# print(len(chapter_info_list), chapter_info_list)

# 遍历出每章的节点
for chapter_info in chapter_info_list:
    # print(chapter_info)

    # 筛选出章节的标题
    chapter_title = chapter_info.xpath('./a/text()')[0]
    print(chapter_title)

    # 筛选出章节的链接
    chapter_url = chapter_info.xpath('./a/@href')[0]
    # print(chapter_url)

    # 补全协议
    chapter_url = 'https:' + chapter_url
    print(chapter_url)

    # 向每章小说的链接发起请求
    response = requests.get(chapter_url, headers=headers, cookies=cookies)
    # print(response.text)

    # 转换成树形结构
    html_tree = etree.HTML(response.text)

    # 筛选出章节小说的内容
    chapter_list = html_tree.xpath('//main/p/text()')
    # print(chapter_list)

    # 将小说章节筛选出来的内容列表转换成字符串, 并使用\n给每个段落添加换行
    chapter_text = '\n'.join(chapter_list)
    print(chapter_text)

    # 拼接章节标题和章节内容
    chapter_content = chapter_title + '\n\n' + chapter_text + '\n\n'

    # 创建一个txt文件用于保存小说里每章的文字内容
    with open(f'{book_title}.txt', 'a', encoding='utf-8') as file:
        file.write(chapter_content)

    # 提示章节保存成功
    print(f'章节：{chapter_title} - 保存成功')

