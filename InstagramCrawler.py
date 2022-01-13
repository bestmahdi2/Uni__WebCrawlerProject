from time import sleep
from pandas import DataFrame
from threading import Thread
from datetime import datetime
from bs4 import BeautifulSoup
from os import listdir, getcwd, sep
from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstagramCrawler:
    """
       This is a class for using FastText.
    """

    def __init__(self) -> None:
        """
        Constructor function,

        self.accounts_url (list): to keep urls of all accounts crawled.
        self.accounts_name (list): to keep names of all accounts crawled.
        self.posts_data (dict): to keep posts data of all accounts crawled.
        self.comments_data (list): to keep posts' comments of all accounts crawled.
        self.driver (webdriver): the driver program uses.
        """

        self.accounts_url = []
        self.accounts_name = []
        self.posts_data = {}
        self.comments_data = []
        self.driver = None

    @staticmethod
    def set_driver(save_data: bool = False, show_browser: bool = True) -> webdriver.Chrome:
        """
        A function to set driver,

        Parameters:
            save_data (bool): The boolean value if user wants to save data and cookies (or load).
            show_browser (bool): The boolean value if user wants to show or hide browser.

        Returns:
            driver (webdriver.Chrome): the driver created for Chrome browser.
        """

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        if save_data:  # if user wants to use cookies.
            options.add_argument("--user-data-dir=" + getcwd() + sep + "UserData")

        if not show_browser:  # if user wants show browser.
            options.add_argument('--headless')

        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

        return driver

    def login(self, username: str, password: str) -> None:
        """
        Login function,

        Parameters:
            username (str): The username of user.
            password (str): The password of user.
        """

        # wait until complete page loading.
        WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

        # find username and password box and fill it.
        username_box = self.driver.find_element_by_css_selector("input[name='username']")
        password_box = self.driver.find_element_by_css_selector("input[name='password']")
        username_box.clear()
        password_box.clear()
        username_box.send_keys(username)
        password_box.send_keys(password)

        # click submit.
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        # click on two Not now buttons
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def find_counted_posts_in_page(self, url: str, number: int, progress_bar={}, label_passed={},
                                   label_left={}) -> list:
        """
        Function to find number of posts in the page,

        Parameters:
            url (str): The username of user.
            number (int): The password of user.
            progress_bar: Progress bar object from tkinter.
            label_passed: Label object from tkinter.
            label_left: Label object from tkinter.
        """

        # get to the page
        self.driver.get(url)

        # keep posts links
        posts = []

        # keep errors, if it's more than 5 -> means scroll is not available anymore.
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

            if progress_bar:  # if progress_bar is given:
                self.progressbar(progress_bar, label_passed, label_left, 1)

        # remove duplicated posts.
        posts = InstagramCrawler.duplicated_remover(posts)

        # send counted posts
        if len(posts) > number:
            return posts[:number]
        return posts

    def find_accounts_url_contain_hashtag(self, hashtag: str, n: int, progress_bar={}, label_passed={},
                                          label_left={}) -> (list, list):
        """
        Function to find number of posts in the page,

        Parameters:
            hashtag (str): The accounts' urls containing hashtags.
            n (int): The number accounts need to be crawled.
            progress_bar: Progress bar object from tkinter.
            label_passed: Label object from tkinter.
            label_left: Label object from tkinter.

        Returns:
            url (list): list of all urls
            name (list): list of all names
        """

        # if a gui is using the program
        if progress_bar:
            self.max = n + (n // 10 + 5)
            self.start = datetime.now()
            self.progressbar(progress_bar, label_passed, label_left, value=0, maximum=self.max)

        # find posts in a page
        posts = self.find_counted_posts_in_page(f"https://www.instagram.com/explore/tags/{hashtag}/", n, progress_bar,
                                                label_passed, label_left)

        url = []
        name = []

        for post in posts:  # find the name and url for each post
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

            if progress_bar:
                self.progressbar(progress_bar, label_passed, label_left, 1)

        return url, name

    def find_m_last_posts_all_accounts(self, accounts_url: list, m: int, progress_bar={}, label_passed={},
                                       label_left={}) -> list:
        """
        Function to find number of posts in the pages,

        Parameters:
            accounts_url (str): The urls of all accounts crawled.
            m (int): The number posts need to be crawled in each account.
            progress_bar: Progress bar object from tkinter.
            label_passed: Label object from tkinter.
            label_left: Label object from tkinter.

        Returns:
            url (list): list of all urls
            name (list): list of all names
        """

        if progress_bar:  # if a gui is using the program:
            self.max = (m // 10 + 5) * len(accounts_url)
            self.start = datetime.now()
            self.progressbar(progress_bar, label_passed, label_left, value=0, maximum=self.max)

        posts = []

        for url in accounts_url:  # to find counted posts in each page:
            posts.extend(self.find_counted_posts_in_page(url, m, progress_bar, label_passed, label_left))
            if progress_bar:
                self.progressbar(progress_bar, label_passed, label_left, 1)

        return posts

    def crawl_comment(self, urls: list, progress_bar={}, label_passed={}, label_left={}) -> (list, list):
        """
        Function to crawl comments of a page with multi threading,

        Parameters:
            urls (list): The urls of all accounts crawled.
            progress_bar: Progress bar object from tkinter.
            label_passed: Label object from tkinter.
            label_left: Label object from tkinter.

        Returns:
            self.post (list): list of all posts
            self.comment (list): list of all comments
        """

        contents = []

        if progress_bar:  # is a gui is using the program:
            self.max = len(urls)
            self.start = datetime.now()
            self.progressbar(progress_bar, label_passed, label_left, value=0, maximum=self.max)

        for url in urls:
            # get to the page
            self.driver.get(url)

            comments = ''
            error = 0
            # check if the error is under 10 -> means there is more scrolling for comments.
            while error < 10:
                try:
                    WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "C4VMK")))
                    comments = self.driver.find_elements_by_class_name("C4VMK")

                    # load more comments:
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

            if progress_bar:
                self.progressbar(progress_bar, label_passed, label_left, 1)

        threads = []
        self.post, self.comment = {}, []
        for content in contents:  # crawl each comment with multi threading
            t = Thread(target=self.comment_thread, args=(content[0], content[1],))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        return self.post, self.comment

    def comment_thread(self, url: str, html) -> None:
        """
        Function to crawl comments on each page,

        Parameters:
            url (str): The url of account's to be crawled.
            html: The html files need to be crawled its comments.
        """

        self.post, self.comment = {}, []

        # crawl the page
        soup = BeautifulSoup(html, 'lxml')
        comments = [BeautifulSoup(str(tag), 'lxml') for tag in soup.find_all("div", class_="C4VMK")]

        # find post's username and caption
        main_username = comments[0].find_all('a')[0].text.strip()
        main_comment = BeautifulSoup(str(comments[0].find_all('span', {'class': ''})[0]).replace("<br/>", "\n"),
                                     'lxml').text.strip()
        self.post[url] = {"post": {"username": main_username, "caption": main_comment}, "comments": []}

        for user_comment in comments:  # crawl the page for comments and it's likes.
            username = [i.text.strip() for i in user_comment.find_all('a')][0]
            comment = [i.text.strip() for i in user_comment.find_all('span', {'class': ''})][0]

            like = [i.text.strip() for i in user_comment.find_all('button', {'class': 'FH9sR'}) if
                    'like' in i.text.strip()]
            like = int(like[0].split(" ")[0]) if like else 0

            self.post[url]['comments'].append({"username": username, "comment": comment, "likes": like})

            self.comment.append(
                {"username": username, "comment": comment, "likes": like, "post_username": main_username})

    def scroll_page(self) -> None:
        """
        Function to scroll the page.
        """

        scroller = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        sleep(1)
        return scroller

    def progressbar(self, progress_bar, label_passed, label_left, value: int = 0, maximum: int = 0) -> None:
        """
        Function to save the data to csv file,

        Parameters:
            progress_bar: Progress bar object from tkinter.
            label_passed: Label object from tkinter.
            label_left: Label object from tkinter.
            value (int): The value this progressbar should be now.
            maximum (int): The maximum value of progressbar.
        """

        # change progressbar maximum or value
        if maximum:
            progress_bar['maximum'] = maximum

        if not value:
            progress_bar['value'] = 0

        else:
            progress_bar['value'] += value

        # change the labels beside progressbar
        now = datetime.now()
        sec = int((now - self.start).total_seconds())
        passed = '{:02d}:{:02d}'.format(sec // 60, sec % 60)
        left = (self.max - progress_bar['value']) * sec // self.max
        label_passed['text'] = '{}/{}, {}'.format(progress_bar["value"], self.max, passed)
        label_left['text'] = '{:02d}:{:02d}'.format(left // 60, left % 60)

    @staticmethod
    def duplicated_remover(dup: list) -> list:
        """
        Function to remove duplicated items from given list.

        Parameters:
            dup (list): The list need to be duplicated cleans.

        Returns:
            self.post (list): list without duplicated items.
        """

        seen = set()
        seen_add = seen.add
        return [x for x in dup if not (x in seen or seen_add(x))]

    @staticmethod
    def save_data(data: list, path: str = "") -> None:
        """
        Function to save the data to csv file,

        Parameters:
            data (list): The list of data need to be saved.
            path (str): The path for saving the file.

        Returns:
            self.post (list): list without duplicated items.
        """

        save_data = {
            'username': [i['username'] for i in data],
            'comment': [i['comment'] for i in data],
            'post_username': [i['post_username'] for i in data],
            'likes': [i['likes'] for i in data]
        }

        data_frame = DataFrame(save_data)
        data_frame = data_frame.set_index("username")

        data_frame.to_csv(path + "dataFrame.csv", encoding='utf-8')


if __name__ == '__main__':
    # make instance of InstagramCrawler and login ot signed in.
    n, m = 1, 1
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

    # find accounts, posts, comments
    instagram.accounts_url, instagram.accounts_name = instagram.find_accounts_url_contain_hashtag(hashtag, n)
    posts_to_be_crawled = instagram.find_m_last_posts_all_accounts(instagram.accounts_url, m)
    posts_data, comments_data = instagram.crawl_comment(posts_to_be_crawled)

    print(comments_data)

    instagram.posts_data.update(posts_data)
    instagram.comments_data.extend(comments_data)

    # save the data
    InstagramCrawler.save_data(instagram.comments_data)
    print(instagram.comments_data)
