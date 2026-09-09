#name: wechat read category all
#author: Bowen
#goal: to get the information about the category_all from weread web
#date: 2026/9/9
#stage: finished

import requests
from jsonpath import jsonpath
import csv

def get_page_data(url,data_list):
    #get the response
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    #select nodes
    element_list = jsonpath(response.json(),'$..books[*]')
    for element in element_list:
        #select index
        index = jsonpath(element,'$.searchIdx')[0]
        print(index)
        book_info = jsonpath(element,'$.bookInfo')[0]
        #select title
        title = jsonpath(book_info,'$.title')[0]
        print(title)
        #select author
        author = jsonpath(book_info,'$.author')[0]
        print(author)
        #select readingCount
        readingCount = jsonpath(element,'$.readingCount')[0]
        print(readingCount)
        #select newRating
        newRating = jsonpath(book_info,'$.newRating')[0]
        newRating = f'{newRating*0.1:.1f}%'
        print(newRating)
        #select commentlevel
        commentlevel = jsonpath(book_info,'$.newRatingDetail.title')[0]
        print(commentlevel)
        #select intro
        intro = jsonpath(book_info,'$.intro')[0]
        intro = intro.replace('\n','').strip()
        print(intro)

        data_list.append([index,title,author,readingCount,newRating,commentlevel,intro])
def save_data_csv(data_list):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['序号','书名','作者','今日阅读人数','推荐值','评价','简介'])
        writer.writerows(data_list)

if __name__ == '__main__':
    data_list = []
    pages = 2
    #define headers
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "baggage": "sentry-environment=production,sentry-release=dev-1786967173530,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=df11e30e9d384e81ba0795c2c351f2c3",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://weread.qq.com/web/category/all",
        "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "df11e30e9d384e81ba0795c2c351f2c3-b63ae93a5b420d99",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
        "x-wrpa-0": "bff95eb5973757d62ec54c275835acf515b5a9b87cea90b3abcec9b9e4123de469de9d98572e834cfd440085e2b2d633db3fb89c6db50adf0727a17cec4614e4,JDE2ckVOUXRlVsOzRMKow7gXNigcwpkRYGLCjTlfwrl3CcKJUcK8w63DjcORw7pofcO1w6fCk1sQwq0PwoZKfFrCp8Kmfk/CncKhwo5SKsOUw5PDgWpVwqbCp8KwwrAmwovCosOmWjNUNyLCsMK4QnTDtBwRUynCgxhuwo7CiMKbVwvCjcK6w5FRKMO9w7nDgXBLwqDDgMKQOsKCRcO8w6LCvcK4QcKjwoLDngcSwprDpsKLw7gNw71fw6zCrXvDkAEzOsKAw4cjw6MWSMKPwprCrcOBYsOUw51swo4Pwqd9wr4wwoLCmMK+w77CtkAGWUvCqAU+wrvCllEgWgM7SWtiwqbDo8O8an1nw6Y6wq/Cm8Oaw7jDvHvDi8OrecKlwqFxQH4rWBJVw57Dvn7CkWbCh0Eiw4JYD8OCKlJAe0YgwrHCh8O/w5TCscKVwqXCtsKrDTLDggFhwpd8ISM/A3/CgcOjw4HDocKHwqR6wpzCpMK+wpFjV8KCR0diFMKC,BkfCh8KwKnzDtcKKwpBWw7HCksO+w7bDmsKvVgUSw5XDkMOIw4zDr8OQw5zCiw3CvcKgGMOwD1MOCDDDkHvDqsONDC/DsUPCpcO/YMOnNB9Uw5N7w70Uw6LCsh1Ww5QaajFuGx9ODwsqcWDCiMOTwpguw44="
    }
    #define cookies
    cookies = {
        "wr_localvid": "",
        "wr_name": "",
        "wr_avatar": "",
        "wr_gender": "",
        "wr_fp": "4007784594",
        "wr_gid": "214823713"
    }
    #define web's url
    url = 'https://weread.qq.com/web/bookListInCategory/all'
    for page in range(pages):
        # define params
        params = {
            "maxIndex": f"{page*20}",
            "rank": "1"
        }
        get_page_data(url,data_list)
    save_data_csv(data_list)