#name: xiachufang recipe
#author: Bowen
#goal: to get the information about the recipes from xiachufang
#date: 2026/9/2
#stage: finished

import csv
from lxml import etree
import requests


def get_recipe_data(url):
    #get the response
    response = requests.get(url, headers=headers)
    #translate response to tree structure
    html_tree = etree.HTML(response.text)
    #create a list
    recipe_data_list = []
    #select nodes
    element_list = html_tree.xpath('//div[@class="normal-recipe-list"]/ul/li/div/div[2]')
    for element in element_list:
        #select title
        title = element.xpath('./p[1]/a/text()')[0]
        print(title)
        #select url
        recipe_url = element.xpath('./p[1]/a/@href')[0]
        #fix up url
        recipe_url = 'https://www.xiachufang.com'+recipe_url
        print(recipe_url)
        #select content
        content = element.xpath('./p[2]/text()')[0]
        content = content.replace('\n', '').strip()
        print(content)
        #select commit
        commit_list = element.xpath('./p[3]/span/text()')
        commit = f'综合评分{commit_list[0]} ({commit_list[1]}做过)' if len(commit_list)==2 else f'{commit_list[0]}做过'
        print(commit)
        #select author
        author = element.xpath('./p[4]/text()')
        author = author[0].replace('\n', '').strip()
        print(author)

        #sep
        print('='*75)
        recipe_data_list.append([title, content, commit, author, recipe_url])
    return recipe_data_list

def save_recipe_data(recipe_data_list):
    with open('recipe_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['菜名', '简介', '评价', '作者', '链接'])
        writer.writerows(recipe_data_list)

if __name__ == '__main__':
    #define headers
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
    }
    recipe_data_list = []
    for page in range(1,4):
        #define web's url
        url = f'https://www.xiachufang.com/recipe_list/102801533/?page={page}'
        recipe_data = get_recipe_data(url)
        recipe_data_list.extend(recipe_data)
    save_recipe_data(recipe_data_list)