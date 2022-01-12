import pickle
from os import listdir, getcwd, sep
from time import sleep
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import requests
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class InstagramCrawler:
    def __init__(self) -> None:
        self.accounts_url = []
        self.accounts_name = []
        self.posts_data = {}
        self.comments_data = []
        self.driver = None

    @staticmethod
    def set_driver(save_data: bool = False, show_browser: bool = True) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        if save_data:
            options.add_argument("--user-data-dir=" + getcwd() + sep + "UserData")

        if not show_browser:
            options.add_argument('--headless')

        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options, executable_path='chromedriver96.exe')

        return driver

    def login(self, username, password) -> None:
        WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

        username_box = self.driver.find_element_by_css_selector("input[name='username']")
        password_box = self.driver.find_element_by_css_selector("input[name='password']")
        username_box.clear()
        password_box.clear()
        username_box.send_keys(username)
        password_box.send_keys(password)

        self.driver.find_element_by_css_selector("button[type='submit']").click()

        # Not now buttons
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def find_counted_posts_in_page(self, url: str, number: int) -> list:
        self.driver.get(url)

        posts = []

        error, last_scroll = 0, 0
        for i in range(number // 10 + 5):
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

        url = []
        name = []

        for post in posts:
            xpath_user = '//*[@id="react-root"]/div/div/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/' + \
                         'header/div[2]/div[1]/div[1]/span/a'

            self.driver.get(post)

            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_user)))

                username = self.driver.find_element_by_xpath(xpath_user).text
                name.append(username)
                url.append("https://www.instagram.com/" + username)

            except common.exceptions.NoSuchElementException:
                pass

            except TimeoutException:
                pass

        return url, name

    def find_m_last_posts_all_accounts(self, accounts_url: list, m: int) -> list:
        posts = []
        for url in accounts_url:
            posts.extend(self.find_counted_posts_in_page(url, m))

        return posts

    def crawl_comment(self, urls: list) -> (list, list):
        contents = []
        for url in urls:
            self.driver.get(url)

            comments = ''
            error = 0
            while error < 10:
                try:
                    WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "C4VMK")))
                    comments = self.driver.find_elements_by_class_name("C4VMK")

                    button = self.driver.find_elements_by_css_selector("[aria-label='Load more comments']")[0]
                    button.click()

                    # if no more comments available while there is a "load more comments" button.
                    if comments == self.driver.find_elements_by_class_name("C4VMK"):
                        error += 1

                except IndexError:
                    error += 1

                except TimeoutException:
                    pass

            if comments:
                contents.append([url, self.driver.page_source])

        threads = []
        self.post, self.comment = {}, []
        for content in contents:
            t = threading.Thread(target=self.comment_thread, args=(content[0], content[1],))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        return self.post, self.comment

    def comment_thread(self, url: str, html):
        self.post, self.comment = {}, []

        soup = BeautifulSoup(html, 'lxml')
        comments = [BeautifulSoup(str(tag), 'lxml') for tag in soup.find_all("div", class_="C4VMK")]
        main_username = comments[0].find_all('a')[0].text.strip()
        main_comment = BeautifulSoup(str(comments[0].find_all('span', {'class': ''})[0]).replace("<br/>", "\n"),
                                     'lxml').text.strip()
        self.post[url] = {"post": {"username": main_username, "caption": main_comment}, "comments": []}

        for user_comment in comments:
            username = [i.text.strip() for i in user_comment.find_all('a')][0]
            comment = [i.text.strip() for i in user_comment.find_all('span', {'class': ''})][0]

            like = [i.text.strip() for i in user_comment.find_all('button', {'class': 'FH9sR'}) if
                    'like' in i.text.strip()]
            like = int(like[0].split(" ")[0]) if like else 0

            self.post[url]['comments'].append({"username": username, "comment": comment, "likes": like})

            self.comment.append(
                {"username": username, "comment": comment, "likes": like, "post_username": main_username})

    def scroll_page(self):
        scroller = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        sleep(1)
        return scroller

    @staticmethod
    def duplicated_remover(dup: list) -> list:
        seen = set()
        seen_add = seen.add
        return [x for x in dup if not (x in seen or seen_add(x))]

    @staticmethod
    def save_date(data: list, path: str = "") -> None:
        save_data = {
            'username': [i['username'] for i in data],
            'comment': [i['comment'] for i in data],
            'post_username': [i['post_username'] for i in data],
            'likes': [i['likes'] for i in data]
        }

        data_frame = pd.DataFrame(save_data)
        data_frame = data_frame.set_index("username")

        data_frame.to_csv(path + "dateFrame.csv", encoding='utf-8')


if __name__ == '__main__':
    n, m = 4, 1
    hashtag = "pizza"

    instagram = InstagramCrawler()

    if "UserData" not in listdir("."):
        username = 'origins1234'
        password = 'Instagram@ok'
        instagram.driver = InstagramCrawler.set_driver()
        instagram.driver.get('https://www.instagram.com/')
        try:
            instagram.login(username, password)
        except TimeoutException:
            print("No Internet")

    else:
        instagram.driver = InstagramCrawler.set_driver(True)

    instagram.accounts_url, instagram.accounts_name = instagram.find_accounts_url_contain_hashtag(hashtag, n)
    posts_to_be_crawled = instagram.find_m_last_posts_all_accounts(instagram.accounts_url, m)
    posts_data, comments_data = instagram.crawl_comment(posts_to_be_crawled)

    instagram.posts_data.update(posts_data)
    instagram.comments_data.extend(comments_data)

    InstagramCrawler.save_date(instagram.comments_data)
    print(instagram.comments_data)
