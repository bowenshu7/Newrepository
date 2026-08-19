#name:Douban_movie_Top250
#author:Bowen
#goal:To get information about douban movie top250
#date:2026/8/17
#stage:finished

import requests
from lxml import etree

def main(pages):
    for i in range(pages):
        page = i*25
        #define headerss
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": "https://movie.douban.com/top250",
            "sec-ch-ua": "\"Not=A?Brand\";v=\"99\", \"Google Chrome\";v=\"151\", \"Chromium\";v=\"151\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
        }
        #define cookie
        cookies = {
            "ll": "\"118267\"",
            "bid": "ymmSsAWVc3k",
            "_pk_id.100001.4cf6": "08e98e4629f1b230.1774971212.",
            "_vwo_uuid_v2": "DCA5E04CC04B034A8D01B4202BE99DBA3|3dc700876385651cba968cdb7bba539f",
            "__yadk_uid": "GWksNKZJPuOEjKEOtvT2BJuPmf64R3Ia",
            "__utmz": "223695111.1779253580.6.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
            "_pk_ref.100001.4cf6": "%5B%22%22%2C%22%22%2C1786936244%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D",
            "_pk_ses.100001.4cf6": "1",
            "ap_v": "0,6.0",
            "__utma": "223695111.528306689.1774971212.1779349832.1786936244.12",
            "__utmb": "223695111.0.10.1786936244",
            "__utmc": "223695111"
        }
        #define website's url
        url = "https://movie.douban.com/top250"
        #define which page to be gotten
        params = {
            "start": str(page),
            "filter": ""
        }
        try:
            # get response
            response = requests.get(url, headers=headers, cookies=cookies, params=params)
            # print(response.text)
        except Exception as e:
            print("GET RESPONSE ERROR",e)
        else:
            #translate to tree structure
            html_tree = etree.HTML(response.text)
            #move to a base node
            base_list = html_tree.xpath('//ol/li/div/div[2]')
            for base in base_list:
                # print(base)

                #title
                title_element = base.xpath('./div[1]/a/span/text()')
                # print(title_element)
                title = ''.join(title_element)
                print('名称/title/别名:',title)

                #roles and types
                roles_and_types_element = base.xpath('./div[2]/p[1]/text()')
                # print(roles_and_types_element)
                roles_and_type = ''.join(roles_and_types_element).replace(' ', '')
                temp = roles_and_type.split('\n')
                roles = temp[1]
                types = temp[2]
                print('人员名单:',roles)
                print('标签:',types)

                #score and the amount of people who left comments
                score = base.xpath('./div[2]/div/span[2]/text()')[0]
                print('豆瓣评分:',score)
                amount = base.xpath('./div[2]/div/span[4]/text()')[0]
                print('评价人数:',amount)

                #classic review
                try:
                    comment = base.xpath('./div[2]/p[2]/span/text()')[0]
                    print('经典评论:',comment)
                except:
                    print('经典评论:此电影还没有经典评论喵')

                #sep
                print('='*75)

if __name__ == "__main__":
    pages = int(input("How many pages do you want to get?"))
    print('=' * 75)
    main(pages)
    print(f'{pages}页已全部获取')