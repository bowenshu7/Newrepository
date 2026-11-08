#name: CSDN NVIDIA articles
#author: Bowen
#goal: to get the information about the article from CSDN NVIDIA
#date: 2026/11/8
#stage: going

from playwright.sync_api import sync_playwright
import csv

def get_page_data(pages):
    data_list = [['标题', '链接', '简介', '日期', '阅读量', '点赞数']]
    with sync_playwright() as spw:
        browser = spw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nvidia.csdn.net/")

        for page_num in range(pages-1):
            page.locator('xpath=//span[@class="btn"]').click()
            page.wait_for_timeout(1000)

        element_list = page.locator('xpath=//ul[@class="background-white recommend-last-noborder"]/li').all()
        for element in element_list:
            title = element.locator('xpath=./div[1]/div/div/h4/a').text_content()
            print(title)
            link = element.locator('xpath=./div[1]/div/div/h4/a').get_attribute('href')
            print(link)
            describe = element.locator('xpath=./div[1]/div/div/p/a').text_content()
            print(describe)
            date = element.locator('xpath=./div[2]/div/div[1]/div').text_content().strip()
            print(date)
            read = element.locator('xpath=./div[2]/div/div[2]/div[1]/span[2]').text_content()
            print(read)
            star = element.locator('xpath=./div[2]/div/div[2]/div[2]/span[2]')
            star = 'none' if star.count() == 0 else star.text_content()
            print(star)

            data_list.append([title,link,describe,date,read,star])

        page.wait_for_timeout(3000)
    return data_list

if __name__ == '__main__':
    pages = 3
    data = get_page_data(pages)
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)