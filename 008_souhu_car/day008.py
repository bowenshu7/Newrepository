import requests
from lxml import etree

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
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# 定义cookie字典
cookies = {
    "IPLOC": "CN4419",
    "SUV": "26042614271488V1",
    "_sa_84db345b": "1777279381",
    "_sa": "pafQiM3sOrB5EJs"
}

# 定义请求的网址
url = "https://db.auto.sohu.com/carsales"

# 发起网络请求
response = requests.get(url, headers=headers, cookies=cookies)
# print(response.text)

# 转换成树形结构
html_tree = etree.HTML(response.text)

# 使用xpath筛选目标数据

# 筛选出全国销量的标题
car_buy_title = html_tree.xpath('//div[@class="sale-data-province--label"]/text()')[0]
# print(car_buy_title)

# 筛选出全国销量的月份
car_buy_month = html_tree.xpath('//span[@class="sale-data--month"]/text()')[0]
# print(car_buy_month)

# 给标题字符串进行格式化
print(f'{car_buy_title} - {car_buy_month}')

# 筛选汽车总销量
car_buy_count = html_tree.xpath('//ul[@class="sale-data-total"]//text()')
# print(f'{car_buy_count}')

# 将筛选的列表数据转换成字符串
car_buy_count_string = ''.join(car_buy_count)
# print(f'{car_buy_count_string}')

# 对字符串进行切割
buy_count_list = car_buy_count_string.split('万辆')
# print(f'{buy_count_list}')

# 格式化输出
print(f'\t{buy_count_list[0]}万辆')
print(f'\t{buy_count_list[1]}万辆')

# 筛选出价格占比标题
car_price_title = html_tree.xpath('//div[@class="sale-data-price"]/h4[@class="sub-title"]/text()')[0]
print('\n' + car_price_title + ':')

# 筛选出价格占比的所有节点
car_price_list = html_tree.xpath('//li[@class="sale-data-price--item"]')

# 遍历出每个节点
for car_price in car_price_list:
    # 从节点中筛选出价格级别
    price_level = car_price.xpath('./div[1]/text()')[0]
    # print(price_level)

    # 从节点中筛选出价格占比
    price_proportion = car_price.xpath('./div[3]/text()')[0]
    # print(price_proportion)

    # 格式化字符串
    print(f'\t{price_level} - {price_proportion}')

# 筛选级别占比标题
level_proportion_title = html_tree.xpath('//div[@class="sale-data-level"]/h4[@class="sub-title"]/text()')[0]
print('\n' + level_proportion_title + ':')

# 筛选轿车相关信息
sedan_proportion = html_tree.xpath('//div[@class="sale-data-level"]/ul[1]//text()')
# print(sedan_proportion)

# 格式化字符串
print(f'\t{sedan_proportion[0]} - {sedan_proportion[1]} - {sedan_proportion[2]}')
print(f'\t{sedan_proportion[3]} - {sedan_proportion[4]} - {sedan_proportion[5]}')

# 筛选SUV相关信息
suv_proportion = html_tree.xpath('//div[@class="sale-data-level"]/ul[2]//text()')
# print(suv_proportion)

# 格式化字符串
print(f'\t{suv_proportion[0]} - {suv_proportion[1]} - {suv_proportion[2]}')
print(f'\t{suv_proportion[3]} - {suv_proportion[4]} - {suv_proportion[5]}')

# 筛选轿车相关信息
mpv_proportion = html_tree.xpath('//div[@class="sale-data-level"]/ul[3]//text()')
# print(mpv_proportion)

# 格式化字符串
print(f'\t{mpv_proportion[0]} - {mpv_proportion[1]} - {mpv_proportion[2]}')
print(f'\t{mpv_proportion[3]} - {mpv_proportion[4]} - {mpv_proportion[5]}')