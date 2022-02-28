import selenium
from enum import Enum
from threading import Thread
from FastText import FastText
from functools import partial
from tkinter.font import Font
import matplotlib.pyplot as plt
from InstagramCrawler import InstagramCrawler
from os import getcwd, sep, listdir, path as path_
from selenium.common.exceptions import TimeoutException
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, HORIZONTAL, VERTICAL, simpledialog, filedialog, Button, Label, Entry, Checkbutton, Toplevel, \
    BOTH, LEFT, Tk, BooleanVar

class State(Enum):
    """
       Enum class for State,
       for limiting user from clicking on buttons > order clicking
    """

    LOGIN = 0
    ACCOUNT = 1
    POST = 2
    SAVE = 3


class GraphicalMenu:
    """
        This is a class for gui use.

        Arguments:
            root (tkinter.Tk): root frame of application
    """

    def __init__(self, root: Tk) -> None:
        """
        Constructor function,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize the labels, buttons, entries, comboboxex, progressbar and separators:
        self.state = State.LOGIN
        self.instagram = InstagramCrawler()
        self.F = FastText()

        # boolean variables for having cookies and showing browser
        self.use_cookies = BooleanVar(value=True)
        self.show_browser = BooleanVar(value=True)

        self.initialize_labels(root)
        self.initialize_buttons(root)
        self.initialize_entries(root)
        self.initialize_checkboxes(root)

        self.combobox = ttk.Combobox(root)
        self.combobox.place(x=180, y=250, width=270, height=30)

        self.progress_bar = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient="horizontal", length=600,
                                            mode="determinate", maximum=100, value=0)
        self.progress_bar.place(x=105, y=550, width=390, height=30)
        # self.progress_bar.place(x=105, y=550, width=425, height=30)

        GraphicalMenu.initialize_seprator(root)

    def initialize_labels(self, root: Tk) -> None:
        """
        Constructor function for labels,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize labels, same properties were set to variables
        font_bold = Font(family='Calibri bold', size=11)
        font = Font(family='Calibri', size=11)
        bg = '#F0EAD6'
        fg = "#333333"
        height = 30

        GraphicalMenu.Label(root, bg, '#CC397B', Font(family='Calibri bold', size=23), "Instagram Crawler",
                            {'x': 10, 'y': 20, 'w': 680, 'h': 45}, 'center')
        GraphicalMenu.Label(root, bg, fg, Font(family='Calibri bold', size=13), "Login",
                            {'x': 10, 'y': 70, 'w': 50, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Username:", {'x': 10, 'y': 110, 'w': 80, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Password:", {'x': 290, 'y': 110, 'w': 80, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font_bold, "Accounts", {'x': 10, 'y': 170, 'w': 73, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Accounts Number (n):", {'x': 10, 'y': 210, 'w': 150, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Hashtag:", {'x': 310, 'y': 210, 'w': 80, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Founded Accounts:", {'x': 10, 'y': 250, 'w': 135, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font_bold, "Posts", {'x': 10, 'y': 310, 'w': 48, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font, "Posts Number (m):", {'x': 10, 'y': 350, 'w': 130, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font_bold, "Save Location", {'x': 10, 'y': 410, 'w': 95, 'h': height})
        GraphicalMenu.Label(root, bg, fg, font_bold, "Progress", {'x': 10, 'y': 510, 'w': 95, 'h': height})
        self.label_passed = GraphicalMenu.Label(root, bg, fg, Font(family='Calibri', size=10),
                                                "0/0, 00:00", {'x': 10, 'y': 550, 'w': 100, 'h': height})
        self.label_left = GraphicalMenu.Label(root, bg, fg, Font(family='Calibri', size=10),
                                              "00:00", {'x': 500, 'y': 550, 'w': 167, 'h': height})
        self.label_error_login = GraphicalMenu.Label(root, bg, "#FF0038", Font(family='Calibri', size=10),
                                                     "", {'x': 10, 'y': 140, 'w': 520, 'h': height})
        self.label_error_accounts = GraphicalMenu.Label(root, bg, "#FF0038", Font(family='Calibri', size=10),
                                                        "", {'x': 10, 'y': 280, 'w': 520, 'h': height})
        self.label_error_posts = GraphicalMenu.Label(root, bg, "#FF0038", Font(family='Calibri', size=10),
                                                     "", {'x': 10, 'y': 380, 'w': 520, 'h': height})
        self.label_error_loc = GraphicalMenu.Label(root, bg, "#FF0038", Font(family='Calibri', size=10),
                                                   "", {'x': 10, 'y': 480, 'w': 520, 'h': height})
        self.label_notif = GraphicalMenu.Label(root, bg, "#20B2AA", Font(family='Calibri', size=11),
                                               "", {'x': 570, 'y': 350, 'w': 110, 'h': 200}, 'n', wraplength=110)

    def initialize_buttons(self, root: Tk) -> None:
        """
        Constructor function for buttons,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize buttons, same properties were set to variables
        bg = "#CC397B"
        fg = "#ffffff"
        font = Font(family='Calibri bold', size=11)
        width = 110
        height = 30

        GraphicalMenu.Button(root, bg, fg, font, "Login/Prepare", {'x': 570, 'y': 110, 'w': width, 'h': height},
                             partial(self.commander, "Login"))
        GraphicalMenu.Button(root, bg, fg, font, "Find Accounts", {'x': 570, 'y': 150, 'w': width, 'h': height},
                             partial(self.commander, "Find Accounts"))
        GraphicalMenu.Button(root, bg, fg, font, "Find Posts", {'x': 570, 'y': 190, 'w': width, 'h': height},
                             partial(self.commander, "Find Posts"))
        GraphicalMenu.Button(root, bg, fg, font, "Save", {'x': 570, 'y': 230, 'w': width, 'h': height},
                             partial(self.commander, "Save"))
        GraphicalMenu.Button(root, bg, fg, font, "➕", {'x': 460, 'y': 250, 'w': 30, 'h': height}, self.adder)
        GraphicalMenu.Button(root, bg, fg, font, "➖", {'x': 500, 'y': 250, 'w': 30, 'h': height}, self.remover)
        GraphicalMenu.Button(root, bg, fg, font, "Open", {'x': 460, 'y': 450, 'w': 70, 'h': height},
                             self.open_directory)
        GraphicalMenu.Button(root, bg, fg, font, "Special", {'x': 570, 'y': 550, 'w': width, 'h': height},
                             partial(self.open_special, root))

    def initialize_entries(self, root: Tk) -> None:
        """
        Constructor function for entries,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize entries, same properties were set to variables
        fg = "#333333"
        font = Font(family='Calibri bold', size=10)
        height = 30

        self.entry_username = GraphicalMenu.Entry(root, fg, font, {'x': 100, 'y': 110, 'w': 150, 'h': height})
        self.entry_password = GraphicalMenu.Entry(root, fg, font, {'x': 380, 'y': 110, 'w': 150, 'h': height}, show="*")
        self.entry_account_number = GraphicalMenu.Entry(root, fg, font, {'x': 180, 'y': 210, 'w': 110, 'h': height},
                                                        "center")
        self.entry_hashtag = GraphicalMenu.Entry(root, fg, font, {'x': 380, 'y': 210, 'w': 150, 'h': height})
        self.entry_post_number = GraphicalMenu.Entry(root, fg, font, {'x': 180, 'y': 350, 'w': 110, 'h': height},
                                                     "center")
        self.entry_save_loc = GraphicalMenu.Entry(root, fg, font, {'x': 15, 'y': 450, 'w': 435, 'h': height})

        # set value of entry of location to current working location
        self.entry_save_loc.delete(0, "end")
        self.entry_save_loc.insert(0, getcwd())

        # set value of entry of account number to 5
        self.entry_account_number.delete(0, "end")
        self.entry_account_number.insert(0, "5")

        # set value of entry of post number to 5
        self.entry_post_number.delete(0, "end")
        self.entry_post_number.insert(0, "5")

    def initialize_checkboxes(self, root: Tk) -> None:
        """
        Constructor function for checkboxes,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize checkbox, same properties were set to variables
        bg = '#F0EAD6'
        fg = "#333333"
        font = Font(family='Calibri bold', size=10)
        width = 110
        height = 30

        self.checkbox_browser = GraphicalMenu.Checkbutton(root, bg, fg, font, "Show Browser",
                                                          {'x': 570, 'y': 280, 'w': width, 'h': height},
                                                          partial(self.commander, "Show Browser"), self.show_browser)
        self.checkbox_cookies = GraphicalMenu.Checkbutton(root, bg, fg, font, "Use Cookies",
                                                          {'x': 564, 'y': 310, 'w': width, 'h': height},
                                                          partial(self.commander, "Use Cookies"), self.use_cookies)

    @staticmethod
    def initialize_seprator(root: Tk):
        """
        Constructor function for seprators,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        ttk.Separator(root, orient=HORIZONTAL).place(x=60, y=85, w=470, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=80, y=185, w=450, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=55, y=325, w=475, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=105, y=425, w=425, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=70, y=525, w=460, h=1)
        ttk.Separator(root, orient=VERTICAL).place(x=550, y=85, w=1, h=500)

    @staticmethod
    def Button(root: Tk, bg: str, fg: str, font: Font, text: str, place: dict, command,
               justify: str = "center", relief: str = "flat") -> Button:
        """
        The function to create and return a new TK button

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (Font): font of the button's text
            text (str): text of the button
            place (dict): position of the button
            command : the function with its parameter
            justify (str): button text justify
            relief (str): relief of the button

        Returns:
            temp_button: A Button object of button created with given information
        """

        temp_button = Button(root, relief=relief, cursor="hand2")
        temp_button["bg"] = bg
        temp_button["font"] = font
        temp_button["fg"] = fg
        temp_button["justify"] = justify
        temp_button["text"] = text
        temp_button.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])
        temp_button["command"] = command

        return temp_button

    @staticmethod
    def Label(root: Tk, bg: str, fg: str, font: Font, text: str, place: dict,
              anchor: str = 'w', wraplength: int = 0) -> Label:
        """
        The function to create and return a new TK label

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (Font): font of the label's text
            text (str): text of the label
            place (dict): position of the label
            anchor (str): label text justify
            wraplength (int): label text justify

        Returns:
            temp_label: A Label object of label created with given information
        """

        temp_label = Label(root, anchor=anchor)
        temp_label["bg"] = bg
        temp_label["font"] = font
        temp_label["fg"] = fg
        temp_label["text"] = text
        if wraplength:
            temp_label["wraplength"] = wraplength
        temp_label.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_label

    @staticmethod
    def Entry(root: Tk, fg: str, font: Font, place: dict, justify: str = "left",
              borderwidth="1px", show="") -> Entry:
        """
        The function to create and return a new TK entry

        Parameters:
            root : root frame of application
            fg (str): foreground color
            font (Font): font of the entry's text
            place (dict): position of the entry
            justify (str): entry text justify
            borderwidth (str): entry border width

        Returns:
            temp_entry: A Entry object of entry created with given information
        """

        temp_entry = Entry(root)
        temp_entry["font"] = font
        temp_entry["fg"] = fg
        temp_entry["justify"] = justify
        temp_entry["borderwidth"] = borderwidth
        if show:
            temp_entry["show"] = show
        temp_entry.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_entry

    @staticmethod
    def Checkbutton(root: Tk, bg, fg: str, font: Font, text: str, place: dict, command, variable,
                    justify: str = "center") -> Checkbutton:
        """
        The function to create and return a new TK checkbox

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (Font): font of the checkbox's text
            text (str): text of the checkbox
            place (dict): position of the checkbox
            command : the command to control checkbox
            justify (str): checkbox text justify


        Returns:
            temp_checkbox: A Checkbutton object of checkbox created with given information
        """

        temp_checkbox = Checkbutton(root, cursor="hand2")
        temp_checkbox["bg"] = bg
        temp_checkbox["font"] = font
        temp_checkbox["fg"] = fg
        temp_checkbox["justify"] = justify
        temp_checkbox["text"] = text
        temp_checkbox["offvalue"] = "0"
        temp_checkbox["onvalue"] = "1"
        temp_checkbox["command"] = command
        temp_checkbox["variable"] = variable
        temp_checkbox.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_checkbox

    def commander(self, command: str) -> None:
        """
        The function for commands connected to buttons

        Parameters:
            command (str): The command user clicked on
        """

        self.clean_errors()
        self.label_notif['text'] = "Wait please ! Program's speed depends on your internet connection !"

        if command == "Login":
            self.clean_errors()

            def login(self):
                # logged in before
                if "UserData" in listdir("."):
                    self.instagram.driver = InstagramCrawler.set_driver(True, self.show_browser.get())
                    self.label_notif['text'] = "Logged in successfully !"
                    self.state = State.ACCOUNT

                # not logged in before and empty username or password
                elif not self.entry_username.get() or not self.entry_password.get():
                    self.label_notif['text'] = ""
                    if not self.entry_username.get():
                        self.label_error_login['text'] = "Username is empty !"

                    elif not self.entry_password.get():
                        self.label_error_login['text'] = "Password is empty !"

                # not logged in before and gave username or password
                elif self.entry_username.get() and self.entry_password.get():
                    username = self.entry_username.get()
                    password = self.entry_password.get()
                    self.instagram.driver = InstagramCrawler.set_driver(self.use_cookies.get(), self.show_browser.get())

                    try:
                        self.instagram.driver.get('https://www.instagram.com/')

                    except selenium.common.exceptions.WebDriverException:
                        self.label_notif['text'] = ""
                        self.label_error_login['text'] = "You're not connected to Internet !"

                    try:
                        self.instagram.login(username, password)
                        self.label_notif['text'] = "Logged in successfully !"
                        self.state = State.ACCOUNT

                    except TimeoutException:
                        self.label_notif['text'] = ""
                        self.label_error_login['text'] = "Weak internet connection or wrong username/password !"

            t = Thread(target=login, args=(self,))
            t.start()

        elif command == "Find Accounts":
            self.clean_errors()  # clean the label's errors

            if self.state.value > 0:
                self.entry_hashtag.get()

                if self.entry_hashtag.get():
                    def find_acounts(self):
                        try:
                            hashtag = self.entry_hashtag.get()
                            hashtag = hashtag[1:] if hashtag.startswith("#") else hashtag

                            # find accounts containing hashtag
                            self.instagram.accounts_url, self.instagram.accounts_name = self.instagram.find_accounts_url_contain_hashtag(
                                self.entry_hashtag.get(), int(self.entry_account_number.get()), self.progress_bar,
                                self.label_passed, self.label_left)

                            # update values of combo box
                            self.combobox['values'] = tuple(self.instagram.accounts_name)
                            self.combobox.current(len(self.combobox['values']) - 1 if self.combobox['values'] else 0)

                            # change value of notification label
                            self.label_notif['text'] = f"{len(self.combobox['values'])} accounts were found !"
                            self.state = State.POST

                        except:
                            self.label_error_accounts['text'] = "Weak internet connection !"

                    t = Thread(target=find_acounts, args=(self,))
                    t.start()

                else:
                    self.label_error_accounts['text'] = "Enter the hashtag you want to search !"

            else:
                self.label_error_login['text'] = "You haven't login yet !"

        elif command == "Find Posts":
            self.clean_errors()  # clean the label's errors

            self.instagram.accounts_url = [f"https://www.instagram.com/{i}/" for i in self.combobox['values']]

            if self.state.value > 1:
                def find_posts(self):
                    # find last posts off all accounts
                    posts_to_be_crawled = self.instagram.find_m_last_posts_all_accounts(self.instagram.accounts_url,
                                                                                        int(self.entry_post_number.get()),
                                                                                        self.progress_bar)
                    # crawl the comments
                    posts_data, comments_data = self.instagram.crawl_comment(posts_to_be_crawled, self.progress_bar)

                    self.instagram.posts_data.update(posts_data)
                    self.instagram.comments_data.extend(comments_data)

                    self.label_notif['text'] = f"{len(self.instagram.comments_data)} comment(s) were found !"
                    self.state = State.SAVE

                t = Thread(target=find_posts, args=(self,))
                t.start()

            else:
                self.label_notif['text'] = ""
                self.label_error_accounts['text'] = "You haven't find accounts yet !"

        elif command == "Save":
            self.clean_errors()  # clean the label's errors

            if self.state.value > 2:
                if not self.entry_save_loc.get():  # if location entry is empty
                    self.label_notif['text'] = ""
                    self.label_error_loc['text'] = "Location can't be empty !"

                elif path_.isdir(self.entry_save_loc.get()):  # if location entry is not empty and it's a path
                    location = self.entry_save_loc.get().replace(sep, "/")
                    location = location if location.endswith("/") else location + "/"
                    InstagramCrawler.save_data(self.instagram.comments_data, location)
                    self.label_notif['text'] = "Done !"

                    self.state = State.SAVE

                else:  # if location entry is not empty and it's not a path
                    self.label_notif['text'] = ""
                    self.label_error_loc['text'] = "This location does not exist !"

            else:
                self.label_notif['text'] = ""
                self.label_error_posts['text'] = "You haven't find posts yet !"

        else:  # if any checkboxes were checked or unchecked
            self.state = State.LOGIN
            self.label_notif['text'] = "Done ! re-login please !"

    def clean_errors(self) -> None:
        """
        The function to clear error labels
        """

        self.label_error_login['text'] = ""
        self.label_error_posts['text'] = ""
        self.label_error_accounts['text'] = ""
        self.label_error_loc['text'] = ""

    def adder(self) -> None:
        """
        The function to open a simple dialog and get a name of account
        """

        inputer = simpledialog.askstring(title="Accont Adding", prompt="Enter the new account name !")
        self.combobox['values'] += tuple([inputer])
        self.combobox.current(len(self.combobox['values']) - 1)

    def remover(self) -> None:
        """
        The function to remove current value of combobox.
        """

        self.combobox['values'] = tuple([i for i in self.combobox['values'] if i != self.combobox.get()])

    def open_directory(self) -> None:
        """
        The function to open the directory path.
        """

        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.label_error_loc['text'] = ""
            self.entry_save_loc.delete(0, "end")
            self.entry_save_loc.insert(0, folder_selected)
        else:
            self.label_error_loc['text'] = "The location can't be selected !"

    def open_special(self, root: Tk) -> None:
        """
        Function for opening and making the window of specials,

        Parameters:
            root (tkinter.Tk): root frame of application
        """

        # initialize window and root
        special = Toplevel(root)
        special.title("Special Part")

        widths, heights = 700, 650
        screenwidth, screenheight = special.winfo_screenwidth(), special.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (widths, heights, (screenwidth - widths) / 2, (screenheight - heights) / 2)
        special.geometry(align_str)
        special.resizable(width=False, height=False)
        special.configure(background='#F0EAD6')

        # initialize labels
        self.Label(special, '#F0EAD6', '#CC397B', Font(family='Calibri bold', size=23), "Prediction Part",
                   {'x': 10, 'y': 20, 'w': 680, 'h': 45}, 'center')
        self.Label(special, "#F0EAD6", "#000000", Font(family='Calibri bold', size=11), "Single Prediction",
                   {'x': 10, 'y': 70, 'w': 120, 'h': 30})
        self.Label(special, "#F0EAD6", "#000000", Font(family='Calibri bold', size=11), "Multiple Prediction",
                   {'x': 10, 'y': 170, 'w': 130, 'h': 30})
        self.Label(special, '#F0EAD6', "#333333", Font(family='Calibri bold', size=11), "Results",
                   {'x': 10, 'y': 270, 'w': 80, 'h': 30})

        self.Label(special, '#F0EAD6', "#333333", Font(family='Calibri', size=11), "Comment:",
                   {'x': 10, 'y': 110, 'w': 80, 'h': 30})
        self.Label(special, '#F0EAD6', "#333333", Font(family='Calibri', size=11), "Address:",
                   {'x': 10, 'y': 215, 'w': 80, 'h': 30})
        self.Label(special, '#ffffff', "#333333", Font(family='Calibri', size=11),
                   f".../{getcwd().split(sep)[-1]}/FasttextFiles/", {'x': 100, 'y': 215, 'w': 450, 'h': 30})
        chart = self.Label(special, '#F0EAD6', "#FF0000", Font(family='Calibri', size=15),
                           "Please wait for process to be finished !", {'x': 10, 'y': 310, 'w': 680, 'h': 325},
                           'center')

        # initialize buttons
        self.Button(special, "#CC397B", "#ffffff", Font(family='Calibri bold', size=11), "Predict",
                    {'x': 560, 'y': 110, 'w': 110, 'h': 30}, partial(self.single_predict, special))
        self.Button(special, "#CC397B", "#ffffff", Font(family='Calibri bold', size=11), "Predict",
                    {'x': 560, 'y': 215, 'w': 110, 'h': 30}, partial(self.multi_predict, special))

        # initialize entry
        self.comment = self.Entry(special, "#333333", Font(family='Calibri bold', size=10),
                                  {'x': 100, 'y': 110, 'w': 450, 'h': 30})

        # initialize seprators
        ttk.Separator(special, orient=HORIZONTAL).place(x=125, y=85, w=550, h=1)
        ttk.Separator(special, orient=HORIZONTAL).place(x=140, y=185, w=530, h=1)
        ttk.Separator(special, orient=HORIZONTAL).place(x=65, y=285, w=610, h=1)

        # make thread to prepare the model
        t = Thread(target=self.prepare_fasttext, args=(chart,))
        t.start()

    def prepare_fasttext(self, chart) -> None:
        """
        Function for preparing the model for using it,
        It's better to make a model every time instead of loading it !

        Parameters:
            chart: root frame of application
        """

        # make = "model_hashtags.bin" in listdir(getcwd() + f"{sep}FasttextFiles{sep}")
        self.F.make_model(True)
        chart["text"] = "Now you use this window !"

    def single_predict(self, special: Tk) -> None:
        """
        Function for single prediction button,
        gets the text and predict it using model.

        Parameters:
            special (tkinter.Tk): root frame of application
        """

        # make label to access it and showing the diagram on it
        chart = self.Label(special, '#F0EAD6', "#FF0000", Font(family='Calibri', size=15),
                           "Please wait for process to be finished !", {'x': 10, 'y': 310, 'w': 680, 'h': 325},
                           'center')

        if self.comment.get() == "":  # if entry is empty
            chart["text"] = "Please write your command in entry !"
            return

        # get the results of prediction
        result = self.F.fasttext(self.comment.get())

        chart["text"] = ""

        # creating the diagram and connecting it to the label
        labels = [result]
        sizes = [100]
        fig1, ax1 = plt.subplots()
        fig1.set_facecolor('#F0EAD6')
        bar1 = FigureCanvasTkAgg(fig1, chart)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.tight_layout()

    def multi_predict(self, special: Tk) -> None:
        """
        Function for multi prediction button,
        gets the all comments and predict them using model.

        Parameters:
            special (tkinter.Tk): root frame of application
        """

        # make label to access it and showing the diagram on it
        chart = self.Label(special, '#F0EAD6', "#FF0000", Font(family='Calibri', size=15),
                           "Please wait for process to be finished !", {'x': 10, 'y': 310, 'w': 680, 'h': 325},
                           'center')

        # get the results of prediction
        results = self.F.fasttext()

        # creating the diagram and connecting it to the label
        labels = ['Good', 'Bad', 'Inactive']
        sizes = [results['good'], results['bad'], results['inactive']]
        explode = (0.1, 0, 0)
        fig1, ax1 = plt.subplots()
        fig1.set_facecolor('#F0EAD6')
        bar1 = FigureCanvasTkAgg(fig1, chart)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.tight_layout()


if __name__ == "__main__":
    # create the instance of Tk, set window, configure and show it
    roots = Tk()
    roots.title("Instagram Crawler")

    widths, heights = 700, 650
    screenwidth, screenheight = roots.winfo_screenwidth(), roots.winfo_screenheight()
    align_str = '%dx%d+%d+%d' % (widths, heights, (screenwidth - widths) / 2, (screenheight - heights) / 2)
    roots.geometry(align_str)
    roots.resizable(width=False, height=False)
    roots.configure(background='#F0EAD6')

    app = GraphicalMenu(root=roots)
    roots.mainloop()
