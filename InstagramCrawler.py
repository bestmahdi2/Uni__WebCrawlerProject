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
        self.accounts_name = []
        self.accounts_url = []
        self.posts_data = {}
        self.comments_data = []

    def set_driver(self) -> webdriver.Chrome:
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

    def signed_in_driver(self) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("start-maximized")
        options.add_argument("--user-data-dir=" + getcwd() + sep + "UserData")
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options, executable_path='chromedriver96.exe')

        return driver

    def find_posts_in_page(self, number: int) -> list:
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

        # remove duplicated and keeping order
        seen = set()
        seen_add = seen.add
        posts = [x for x in posts if not (x in seen or seen_add(x))]

        if len(posts) > number:
            return posts[:number]
        return posts

    def find_accounts_name_contain_hashtag(self, hashtag: str, n: int):
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        posts = self.find_posts_in_page(n)

        # x = 0
        # links = self.driver.find_elements_by_xpath("//a[@href]")
        # while x < n:
        #     post = links[x].get_attribute("href")
        #     if "/p/" in post:
        #         posts.append(post)
        #         x += 1

        for post in posts:
            self.driver.get(post)
            sleep(1)
            self.accounts_name.append(
                "https://www.instagram.com/" + self.driver.find_element_by_xpath("//div[@class='e1e1d']").text)

    def find_m_last_posts(self, url: str, m: int) -> list:
        self.driver.get(url)
        posts = self.find_posts_in_page(m)

        return posts

    def CrawlComment(self, url: str):
        self.driver.get(url)

        error = 0
        while error < 5:
            sleep(1)
            try:
                button = self.driver.find_elements_by_css_selector("[aria-label='Load more comments']")[0]
                button.click()
            except IndexError:
                error += 1

        links = self.driver.find_elements_by_class_name("C4VMK")
        if links:
            post = str(links[0].text).split("\n")
            self.posts_data[url] = {"post": {"username": post[0], "caption": post[1:-1]}, "comments": []}

            for link in links:
                username, comment = [i.text for i in link.find_elements_by_tag_name("span")]

                like = [i.text for i in link.find_elements_by_tag_name("button") if i.text not in ['Reply', '']]
                like = int(like[0].split(" ")[0]) if like else 0

                self.posts_data[url]['comments'].append({"username": username, "comment": comment, "likes": like})

                self.comments_data.append(
                    {"username": username, "comment": comment, "likes": like, "post_username": post[0]})

    def scroll_page(self):
        sleep(3)
        return self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")


if __name__ == '__main__':
    instagram = InstagramCrawler()

    signed_in = True

    if not signed_in:
        instagram.driver = instagram.set_driver()
        instagram.driver.get('https://www.instagram.com/')
        instagram.login()

    else:
        instagram.driver = instagram.signed_in_driver()

    instagram.find_accounts_name_contain_hashtag()
    # lister = self.find_m_last_posts("https://www.instagram.com/rubic979/", 200)
    # print(len(lister), lister, sep="\n")

    # print(self.comments_data)




# posts = ['https://www.instagram.com/p/CYPXzXzv73u/', 'https://www.instagram.com/p/CYRCnqssB78/',
#          'https://www.instagram.com/p/CYO1S8VKAo0/', 'https://www.instagram.com/p/CYP7PkxrZ3u/',
#          'https://www.instagram.com/p/CYOJfr8Nudg/', 'https://www.instagram.com/p/CYQ_WjFAn8K/',
#          'https://www.instagram.com/p/CYRcl5lOQjR/', 'https://www.instagram.com/p/CYPCKbsMqFW/',
#          'https://www.instagram.com/p/CYPqCynvAM7/', 'https://www.instagram.com/p/CYRxcTztEEe/']
#
# accounts_name = ['https://www.instagram.com/80sthen80snow', 'https://www.instagram.com/lauradiana000',
#                  'https://www.instagram.com/atawich.turkiye',
#                  'https://www.instagram.com/pancakes.and.protein.shakes',
#                  'https://www.instagram.com/della_bistro', 'https://www.instagram.com/eat4naples',
#                  'https://www.instagram.com/confeitaria_simples',
#                  'https://www.instagram.com/jondanieledlund',
#                  'https://www.instagram.com/dani_branca', 'https://www.instagram.com/satuilvonen']