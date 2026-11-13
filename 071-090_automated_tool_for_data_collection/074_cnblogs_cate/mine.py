#name: cnblogs cate ai-misc
#author: Bowen
#goal: to get the information about the ai-misc from cnblogs cate
#date: 2026/11/13
#stage: finished

from playwright.sync_api import sync_playwright
import pymongo

def get_page_data(pages):
    data_list = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.cnblogs.com/cate/ai-misc')
        page.wait_for_timeout(1000)

        for pn in range(1, pages+1):
            if pn>1:
                page.locator(f'xpath=//div[@class="pager"]/a[@href="/cate/ai-misc/{pn}"]').last.click()
                page.wait_for_timeout(1000)
            element_list = page.locator('xpath=//div[@id="post_list"]/article').all()
            for element in element_list:
                title = element.locator('xpath=./section/div/a').text_content()
                print(title)
                link = element.locator('xpath=./section/div/a').get_attribute('href')
                print(link)
                desc = element.locator('xpath=./section/div/p').text_content().strip()
                print(desc)
                author = element.locator('xpath=./section/footer/a[1]/span').text_content()
                print(author)
                stamp = element.locator('xpath=./section/footer/span[1]').text_content().strip()
                print(stamp)
                comment = element.locator('xpath=./section/footer/a[2]/span').text_content()
                print(comment)
                star = element.locator('xpath=./section/footer/a[3]/span').text_content()
                print(star)
                read = element.locator('xpath=./section/footer/a[4]/span').text_content()
                print(read)

                data_list.append({'标题':title,'链接':link,'简介':desc,'作者':author,'时间':stamp,'评论数':comment,'点赞数':star,'浏览量':read})
            page.wait_for_timeout(1000)
    return data_list
def save_mongo(data):
    with pymongo.MongoClient() as client:
            db = client['100_practices']
            collection = db['cnlogs']
            collection.insert_many(data)

if __name__ == '__main__':
    pages = 10
    data = get_page_data(pages)
    save_mongo(data)