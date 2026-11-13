#name: docin IT article
#author: Bowen
#goal: to get the information about the article from docin IT web
#date: 2026/11/9
#stage: finished

from playwright.sync_api import sync_playwright
import csv

def get_page_data(pages):
    data_list = [['标题','链接','日期','页数']]
    with sync_playwright() as spw:
        browser = spw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.docin.com/l-10017-0-0-0-0-1.html')
        page.wait_for_timeout(1000)

        for p in range(pages):
            if p > 0:
                page.locator('xpath=//div[@class="page"]/ul/li/a').last.click()
                page.wait_for_timeout(2000)
            element_list = page.locator('xpath=//dl').all()
            for element in element_list:
                title = element.locator('xpath=./dd[1]/a').text_content()
                scheme = element.locator('xpath=./dd[1]/em').text_content()
                title = title+scheme
                print(title)
                link = element.locator('xpath=./dd[1]/a').get_attribute('href')
                print(link)
                date = element.locator('xpath=./dd[3]/ul/li[2]/span').text_content()
                print(date)
                page_count = element.locator('xpath=./dt/a/span').text_content().replace('p','').strip()
                print(page_count)

                data_list.append([title, link, date,page_count])
    return data_list


if __name__ == '__main__':
    pages = 5
    data = get_page_data(pages)
    with open('data.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)