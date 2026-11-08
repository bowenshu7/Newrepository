#name: gitee AI project information
#author: Bowen
#goal: to get the information about AI project from gitee web
#date: 2026/10/28
#stage: finished

from playwright.sync_api import sync_playwright
import csv

def get_gitee_data():
    with sync_playwright() as spw:
        browser = spw.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.gitee.com/explore/Artificial-Intelligence")
        page.wait_for_timeout(3000)
        gitee_data = [["标题","星数","简介","更新日期"]]

        for page_num in range(3):
            element_list = page.locator('xpath=//div[@class="content"]').all()
            for element in element_list:
                title = element.locator('xpath=./div[1]/div[1]/h3/a').text_content()
                print(title)

                star = element.locator('xpath=./div[1]/div[2]/div/div').text_content()
                print(star)

                content = element.locator('xpath=./div[2]').text_content()
                print(content)

                date = element.locator('xpath=./div[@class="project-item-bottom d-flex-between gap-1"]/div/div[2]').text_content().strip()
                print(date)

                gitee_data.append([title, star, content, date])
            if page_num < 3:
                page.locator('xpath=//div[@class="ui tiny pagination menu"]/a[@rel="next"]').last.click()
            page.wait_for_timeout(1000)
        return gitee_data

if __name__ == '__main__':
    data = get_gitee_data()
    with open("gitee_data.csv", "w", encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("done")
