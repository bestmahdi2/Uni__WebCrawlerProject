import re
from pickle import dump, load

from InstagramCrawler import InstagramCrawler
import fasttext


class FastText:
    def __init__(self, icrawler: InstagramCrawler):
        super().__init__()
        # model = fasttext.train_supervised(input="cooking.train", lr=1.0, epoch=25, wordNgrams=2)
        self.comments = {}
        self.cleaned_comments = {}
        self.labeled_comments = {}
        self.icrawler = icrawler

    def comments_getter(self, tashtags: list, number_of_posts: int) -> dict:
        comments = {}
        for hashtag in tashtags:
            comments_data = []

            posts = self.icrawler.find_counted_posts_in_page(f"https://www.instagram.com/explore/tags/{hashtag}/", number_of_posts)
            print(f"posts found for {hashtag}")

            for post in posts:
                print(f"crawl {post}")
                _, comments_data = self.icrawler.crawl_comment(post)
                print("length of comments were found: ", len(comments_data))

            comments[hashtag] = comments_data

        return comments

    @staticmethod
    def comments_labeling(cleaned_comments: dict) -> dict:
        labeled_comments = {}
        deleted_comments = {}

        print(", ".join([f'{key}: {len(cleaned_comments[key])} comments' for key in cleaned_comments.keys()]))

        print("Enter 'g'/'b'/'i' for good/bad/inactive and enter nothing for deleting this comment.")

        for key in cleaned_comments.keys():
            labeled_comments[key] = {'good': [], 'bad': [], 'inactive': []}
            deleted_comments[key] = []

            length = len(cleaned_comments[key])

            print('\nhashtag:', key)

            x = 1
            for comment in cleaned_comments[key]:
                inputer = input(f'{x}/{length}) {comment} > ')

                if inputer.lower() == 'g':
                    labeled_comments[key]['good'].append(comment)

                elif inputer.lower() == 'b':
                    labeled_comments[key]['bad'].append(comment)

                elif inputer.lower() == 'i':
                    labeled_comments[key]['inactive'].append(comment)

                else:
                    deleted_comments[key].append(comment)

                x += 1

        print(labeled_comments)
        print("--------------")
        print(deleted_comments)

        return labeled_comments

    @staticmethod
    def comments_train_preparing(labeled_comments: dict):
        for key in labeled_comments.keys():
            temp_comments_keeper = []
            for label in labeled_comments[key].keys():
                temp_comments_keeper += [f"__label__{label} {comment}" for comment in labeled_comments[key][label]]

            FastText.save_train(temp_comments_keeper, key)

    @staticmethod
    def clean_comments(comments: dict) -> dict:
        cleaned_comments = {}

        for key in comments.keys():
            cleaned_comments[key] = []
            for comment in comments[key]:
                text = FastText.hashtag_account_remover(comment['comment'])
                text = FastText.emoji_remover(text).lower().replace("\n", " ").replace("  ", " ")
                text = FastText.non_ascii_remover(text)
                text = FastText.useless_remover(text)

                if len(text) > 3:  # remove comments under 3 characters
                    cleaned_comments[key].append(text)

            seen = set()
            seen_add = seen.add
            cleaned_comments[key] = [x for x in cleaned_comments[key] if not (x in seen or seen_add(x))]

        return cleaned_comments

    @staticmethod
    def emoji_remover(text):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", re.UNICODE)

        return emoji_pattern.sub(r'', text)

    @staticmethod
    def hashtag_account_remover(text):
        hashtag_account_pattern = re.compile("(@[A-Za-z0-9_]+)|(#[A-Za-z0-9_]+)")
        return hashtag_account_pattern.sub(r'', text)

    @staticmethod
    def non_ascii_remover(text):
        encoded_string = text.encode("ascii", "ignore")
        return encoded_string.decode()

    @staticmethod
    def useless_remover(text):
        for i in ['`', '~', '@', '#', '$', '%', '^', '*', '/', '\\', '\"', '(', ')', '[', ']', '-', '<', '>', ',', '_',
                  '+', '-', '_', '=']:
            text = text.replace(i, "")

        if text.startswith(" "):
            text = text[1:]

        if text.endswith(" "):
            text = text[:-1]

        text = re.sub("\s{2,}", " ", text)  # userless space
        text = text.replace(" . ", ".").replace(". ", ".").replace(" .", ".")
        text = re.sub("\s{2,}", " ", text)  # userless space

        return text

    def save_comments(self):
        with open('saved_comments.pkl', 'wb') as f:
            dump(self.labeled_comments, f)

    def load_comments(self):
        with open('saved_comments.pkl', 'rb') as f:
            self.labeled_comments = load(f)

    @staticmethod
    def save_train(labeled_train: list, key: str):
        """save each key"""

        with open(f'saved_train_{key}.txt', 'w') as f:
            f.write("\n".join(labeled_train))

    @staticmethod
    def load_train(keys: list) -> dict:
        """load all keys"""
        labeled_train = {}

        for key in keys:
            with open(f'saved_train_{key}.txt', 'r') as f:
                labeled_train[key] = f.readlines()

        return labeled_train


if __name__ == '__main__':
    signed_in = True
    icrawler = InstagramCrawler()

    if not signed_in:
        username = 'origins1234'
        password = 'Instagram@ok'
        icrawler.driver = InstagramCrawler.set_driver()
        icrawler.driver.get('https://www.instagram.com/')
        icrawler.login(username, password)

    else:
        icrawler.driver = InstagramCrawler.signed_in_driver()

    F = FastText(icrawler)

    comments = F.comments_getter(["applewatch", "macbookpro", "appleiphone"], 10)
    F.comments.update(comments)

    cleaned_comments = FastText.clean_comments(comments)
    F.cleaned_comments.update(cleaned_comments)

    F.labeled_comments = FastText.comments_labeling(F.cleaned_comments)
    F.save_comments()
    FastText.comments_train_preparing(F.labeled_comments)
