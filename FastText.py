import re
from pickle import dump, load
from selenium.common.exceptions import TimeoutException
from InstagramCrawler import InstagramCrawler


class FastText:
    def __init__(self, icrawler: InstagramCrawler = None):
        super().__init__()
        self.comments = {}
        self.cleaned_comments = {}
        self.labeled_comments = {}
        self.icrawler = icrawler
        self.model = None
        self.path_ft_files = "FasttextFiles/"

    def comments_getter(self, tashtags: list, number_of_posts: int):
        comments = {}
        print("$ Found comments > ", end="")
        for hashtag in tashtags:
            posts = self.icrawler.find_counted_posts_in_page(f"https://www.instagram.com/explore/tags/{hashtag}/",
                                                             number_of_posts)

            _, comments_data = self.icrawler.crawl_comment(posts)
            print(f"{hashtag}: {len(comments_data)}", end="")

            comments[hashtag] = comments_data

        print()
        self.icrawler.driver.close()

        self.comments.update(comments)

    def make_model(self, make: bool = False):
        import fasttext
        labeled_data = self.load_labeled()

        if make:
            self.model = fasttext.train_supervised(input=labeled_data["train"], lr=1.0, epoch=25, wordNgrams=3)
            self.model.save_model(self.path_ft_files + "model_hashtags.bin")

        else:
            self.model = fasttext.load_model(self.path_ft_files + "model_hashtags.bin")

        # test the model:
        # print(self.model.test(labeled_data["valid"]))

    def fasttext(self, predict: str = ""):
        self.load_comments()

        results = {"good": 0, "bad": 0, "inactive": 0}

        if predict:
            return self.model.predict(predict)[0][0].replace("__label__", "")

        else:
            for predict in self.comments:
                results[self.model.predict(predict)[0][0].replace("__label__", "")] += 1

            return results

    def comments_labeling(self):
        labeled_comments = {}
        deleted_comments = {}

        print("$ Cleaned comments > " + ", ".join(
            [f'{key}: {len(self.cleaned_comments[key])}' for key in self.cleaned_comments.keys()]))

        print("\n% Enter 'g'/'b'/'i' for good/bad/inactive and enter nothing for deleting this comment.")

        for key in self.cleaned_comments.keys():
            labeled_comments[key] = {'good': [], 'bad': [], 'inactive': []}
            deleted_comments[key] = []

            length = len(self.cleaned_comments[key])

            print('# Hashtag:', key)

            x = 1
            for comment in self.cleaned_comments[key]:
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

        print("\nLabeled comments: ", labeled_comments)
        print("--------------")
        print("Deleted comments: ", deleted_comments)

        self.labeled_comments = labeled_comments

    def comments_train_preparing(self, labeled_comments: dict):
        temp_comments_keeper = []

        for key in labeled_comments.keys():
            for label in labeled_comments[key].keys():
                temp_comments_keeper += [f"__label__{label} {comment}" for comment in labeled_comments[key][label]]

            self.save_labeled(temp_comments_keeper)

    def save_comments(self):
        with open(self.path_ft_files + 'labeled_comments.pkl', 'ab') as f:
            dump(self.labeled_comments, f)

        with open(self.path_ft_files + 'saved_comments.pkl', 'ab') as f:
            dump(self.comments, f)

    def load_comments(self):
        with open(self.path_ft_files + 'labeled_comments.pkl', 'rb') as f:
            self.labeled_comments = load(f)

        try:
            with open(self.path_ft_files + 'saved_comments.pkl', 'rb') as f:
                self.comments = load(f)

        except IOError:
            saved_comments = []
            pattern = re.compile("(__label__)[a-zA-Z]+\ ")

            with open(self.path_ft_files + f'saved.train', 'r') as f:
                saved_comments += [i.replace("\n", "") for i in f.readlines()]

            with open(self.path_ft_files + f'saved.valid', 'r') as f:
                saved_comments += [i.replace("\n", "") for i in f.readlines()]

            saved_comments = [pattern.sub(r'', i) for i in saved_comments]

            self.comments = saved_comments

    def save_labeled(self, labeled_train: list):
        """save each key"""

        index_percent = int(len(labeled_train) * 0.8)

        with open(self.path_ft_files + f'saved.train', 'a') as f:
            f.write("\n".join(labeled_train[:index_percent]))
            f.write("\n")

        with open(self.path_ft_files + f'saved.valid', 'a') as f:
            f.write("\n".join(labeled_train[index_percent:]))
            f.write("\n")

    def load_labeled(self) -> dict:
        """load all keys"""

        labeled_data = {}

        labeled_data['train'] = self.path_ft_files + f'saved.train'
        labeled_data['valid'] = self.path_ft_files + f'saved.valid'

        return labeled_data

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


if __name__ == '__main__':
    signed_in = True
    icrawler = InstagramCrawler()

    if not signed_in:
        username = 'origins1234'
        password = 'Instagram@ok'
        icrawler.driver = InstagramCrawler.set_driver()
        icrawler.driver.get('https://www.instagram.com/')
        try:
            icrawler.login(username, password)
        except TimeoutException:
            print("No Internet")

    else:
        icrawler.driver = InstagramCrawler.set_driver(True)

    F = FastText(icrawler)

    ##############

    # F.comments_getter(["applewatch", "macbookpro", "appleiphone"], 1)
    # print("Comments:", F.comments)
    # F.cleaned_comments = FastText.clean_comments(F.comments)
    # print("Cleaned Comments:", F.cleaned_comments)
    # F.comments_labeling()
    # F.save_comments()
    # F.comments_train_preparing(F.labeled_comments)

    ################

    F.make_model(make=False)
    print(F.fasttext("good"))
    print(F.fasttext())
