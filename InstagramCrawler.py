import pickle
from os import listdir, getcwd, sep
from time import sleep
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import requests
import threading


class InstagramCrawler:
    def __init__(self) -> None:
        self.accounts_url = []
        self.accounts_name = []
        self.posts_data = {}
        self.comments_data = []
        self.driver = None

    @staticmethod
    def set_driver() -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options, executable_path='chromedriver96.exe')
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Chrome/85.0.4183.102 (Windows NT 10.0; Win64; x64)'})

        return driver

    def login(self) -> None:
        # login
        username = 'origins1234'
        password = 'Instagram@ok'

        # login
        sleep(3)
        username_box = self.driver.find_element_by_css_selector("input[name='username']")
        password_box = self.driver.find_element_by_css_selector("input[name='password']")
        username_box.clear()
        password_box.clear()
        username_box.send_keys(username)
        password_box.send_keys(password)

        login = self.driver.find_element_by_css_selector("button[type='submit']").click()

        # # save your login info?
        # login_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/div/div/section/div/button').click()
        # sleep(3)
        # noti = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        # sleep(3)

    @staticmethod
    def signed_in_driver() -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("start-maximized")
        options.add_argument("--user-data-dir=" + getcwd() + sep + "UserData")
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options, executable_path='chromedriver96.exe')

        return driver

    def find_counted_posts_in_page(self, url: str, number: int) -> list:
        self.driver.get(url)

        posts = []

        error, last_scroll = 0, 0
        for i in range(number // 10 + 10):
            links = self.driver.find_elements_by_xpath("//a[@href]")

            try:
                posts += [i.get_attribute("href") for i in links if "/p/" in i.get_attribute("href")]

                if last_scroll == self.scroll_page():
                    error += 1
                    if error == 5:
                        break

            except common.exceptions.StaleElementReferenceException:
                pass

        posts = InstagramCrawler.duplicated_remover(posts)

        if len(posts) > number:
            return posts[:number]
        return posts

    def find_accounts_url_contain_hashtag(self, hashtag: str, n: int) -> (list, list):
        posts = self.find_counted_posts_in_page(f"https://www.instagram.com/explore/tags/{hashtag}/", n)

        accounts_url = []
        accounts_name = []

        for post in posts:
            self.driver.get(post)
            sleep(1)
            username = self.driver.find_element_by_xpath("//div[@class='e1e1d']").text
            accounts_name.append(username)
            accounts_url.append("https://www.instagram.com/" + username)

        return accounts_url, accounts_name

    def find_m_last_posts_all_accounts(self, accounts_url: list, m: int) -> list:
        posts = []
        for url in accounts_url:
            posts.append(self.find_counted_posts_in_page(url, m))

        return posts

    def crawl_comment(self, url: str) -> (list, list):
        self.driver.get(url)

        error = 0
        while error < 5:
            sleep(1)
            try:
                button = self.driver.find_elements_by_css_selector("[aria-label='Load more comments']")[0]
                button.click()
            except IndexError:
                error += 1

        posts_data, comments_data = {}, []

        links = self.driver.find_elements_by_class_name("C4VMK")
        if links:
            post = str(links[0].text).split("\n")
            posts_data[url] = {"post": {"username": post[0], "caption": post[1:-1]}, "comments": []}

            for link in links:
                username, comment = [i.text for i in link.find_elements_by_tag_name("span")]

                like = [i.text for i in link.find_elements_by_tag_name("button") if i.text not in ['Reply', '']]
                like = int(like[0].split(" ")[0]) if like else 0

                posts_data[url]['comments'].append({"username": username, "comment": comment, "likes": like})

                comments_data.append(
                    {"username": username, "comment": comment, "likes": like, "post_username": post[0]})

        return posts_data, comments_data

    def scroll_page(self):
        sleep(3)
        return self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")

    @staticmethod
    def duplicated_remover(dup: list) -> list:
        seen = set()
        seen_add = seen.add
        return [x for x in dup if not (x in seen or seen_add(x))]


if __name__ == '__main__':
    n, m = 100, 10
    hashtag = "pizza"
    signed_in = True

    instagram = InstagramCrawler()

    if not signed_in:
        instagram.driver = InstagramCrawler.set_driver()
        instagram.driver.get('https://www.instagram.com/')
        instagram.login()

    else:
        instagram.driver = InstagramCrawler.signed_in_driver()

    instagram.accounts_url, instagram.accounts_name = instagram.find_accounts_url_contain_hashtag(hashtag, n)
    posts_to_be_crawled = instagram.find_m_last_posts_all_accounts(instagram.accounts_url, m)

    for post in posts_to_be_crawled:
        posts_data, comments_data = instagram.crawl_comment(post)

        instagram.posts_data.update(posts_data)
        instagram.comments_data.extend(comments_data)




# posts = ['https://www.instagram.com/p/CYPXzXzv73u/', 'https://www.instagram.com/p/CYRCnqssB78/',
#          'https://www.instagram.com/p/CYO1S8VKAo0/', 'https://www.instagram.com/p/CYP7PkxrZ3u/',
#          'https://www.instagram.com/p/CYOJfr8Nudg/', 'https://www.instagram.com/p/CYQ_WjFAn8K/',
#          'https://www.instagram.com/p/CYRcl5lOQjR/', 'https://www.instagram.com/p/CYPCKbsMqFW/',
#          'https://www.instagram.com/p/CYPqCynvAM7/', 'https://www.instagram.com/p/CYRxcTztEEe/']
#
# accounts_url = ['https://www.instagram.com/80sthen80snow', 'https://www.instagram.com/lauradiana000',
#                  'https://www.instagram.com/atawich.turkiye',
#                  'https://www.instagram.com/pancakes.and.protein.shakes',
#                  'https://www.instagram.com/della_bistro', 'https://www.instagram.com/eat4naples',
#                  'https://www.instagram.com/confeitaria_simples',
#                  'https://www.instagram.com/jondanieledlund',
#                  'https://www.instagram.com/dani_branca', 'https://www.instagram.com/satuilvonen']
