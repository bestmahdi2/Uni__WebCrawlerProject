import tkinter as tk
from tkinter import ttk, HORIZONTAL, LEFT, VERTICAL, simpledialog, filedialog
import tkinter.font as tk_font
from functools import partial


class GraphicalMenu:
    """
        This is a class for gui use.

        Arguments:
            root (tk): root frame of application
    """

    def __init__(self, root):
        self.stay_loggedin = True
        self.show_browser = True

        self.initialize_labels(root)
        self.initialize_buttons(root)
        self.initialize_entries(root)
        self.initialize_checkboxes(root)

        self.combobox = ttk.Combobox(root, values=('value1', 'value2', 'value3'))
        self.combobox.place(x=180, y=250, width=270, height=30)

        progress_bar = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient="horizontal", length=600,
                                       mode="determinate", maximum=100, value=0)
        progress_bar.place(x=105, y=550, width=390, height=30)

        self.initialize_seprator(root)

    def initialize_labels(self, root):
        # initialize labels, same properties were set to variables
        font_bold = tk_font.Font(family='Calibri bold', size=11)
        font = tk_font.Font(family='Calibri', size=11)
        bg = '#F0EAD6'
        fg = "#333333"
        height = 30

        self.Label(root, bg, '#CC397B', tk_font.Font(family='Calibri bold', size=23), "Instagram Crawler",
                   {'x': 10, 'y': 20, 'w': 680, 'h': 45}, 'center')
        self.Label(root, bg, fg, tk_font.Font(family='Calibri bold', size=13), "Login",
                   {'x': 10, 'y': 70, 'w': 50, 'h': height})
        self.Label(root, bg, fg, font, "Username:", {'x': 10, 'y': 110, 'w': 80, 'h': height})
        self.Label(root, bg, fg, font, "Password:", {'x': 290, 'y': 110, 'w': 80, 'h': height})
        self.Label(root, bg, fg, font_bold, "Accounts", {'x': 10, 'y': 170, 'w': 73, 'h': height})
        self.Label(root, bg, fg, font, "Accounts Number (n):", {'x': 10, 'y': 210, 'w': 150, 'h': height})
        self.Label(root, bg, fg, font, "Founded Accounts:", {'x': 10, 'y': 250, 'w': 135, 'h': height})
        self.Label(root, bg, fg, font_bold, "Posts", {'x': 10, 'y': 310, 'w': 48, 'h': height})
        self.Label(root, bg, fg, font, "Posts Number (m):", {'x': 10, 'y': 350, 'w': 130, 'h': height})
        self.Label(root, bg, fg, font_bold, "Save Location", {'x': 10, 'y': 410, 'w': 95, 'h': height})
        self.Label(root, bg, fg, font_bold, "Progress", {'x': 10, 'y': 510, 'w': 95, 'h': height})
        self.label_passed = self.Label(root, bg, fg, tk_font.Font(family='Calibri', size=10),
                                       "100/300, 10:02", {'x': 10, 'y': 550, 'w': 100, 'h': height})
        self.label_left = self.Label(root, bg, fg, tk_font.Font(family='Calibri', size=10),
                                     "10:02", {'x': 500, 'y': 550, 'w': 167, 'h': height})
        self.label_error_login = self.Label(root, bg, "#FF0038", tk_font.Font(family='Calibri', size=10),
                                            "label_error_login", {'x': 10, 'y': 140, 'w': 520, 'h': height})
        self.label_error_accounts = self.Label(root, bg, "#FF0038", tk_font.Font(family='Calibri', size=10),
                                               "label_error_accounts", {'x': 10, 'y': 280, 'w': 520, 'h': height})
        self.label_error_posts = self.Label(root, bg, "#FF0038", tk_font.Font(family='Calibri', size=10),
                                            "label_error_posts", {'x': 10, 'y': 380, 'w': 520, 'h': height})
        self.label_error_loc = self.Label(root, bg, "#FF0038", tk_font.Font(family='Calibri', size=10),
                                          "label_error_posts", {'x': 10, 'y': 480, 'w': 520, 'h': height})

    def initialize_buttons(self, root):
        # initialize buttons, same properties were set to variables
        bg = "#CC397B"
        fg = "#ffffff"
        font = tk_font.Font(family='Calibri bold', size=11)
        width = 110
        height = 30

        self.Button(root, bg, fg, font, "Login", {'x': 570, 'y': 110, 'w': width, 'h': height},
                    partial(self.commander, "Login"))
        self.Button(root, bg, fg, font, "Find Accounts", {'x': 570, 'y': 150, 'w': width, 'h': height},
                    partial(self.commander, "Find Accounts"))
        self.Button(root, bg, fg, font, "Find Posts", {'x': 570, 'y': 190, 'w': width, 'h': height},
                    partial(self.commander, "Find Posts"))
        self.Button(root, bg, fg, font, "Save", {'x': 570, 'y': 230, 'w': width, 'h': height},
                    partial(self.commander, "Save"))
        self.Button(root, bg, fg, font, "➕", {'x': 460, 'y': 250, 'w': 30, 'h': height}, self.adder)
        self.Button(root, bg, fg, font, "➖", {'x': 500, 'y': 250, 'w': 30, 'h': height}, self.remover)
        self.Button(root, bg, fg, font, "Open", {'x': 460, 'y': 450, 'w': 70, 'h': height}, self.open_directory)

    def initialize_entries(self, root):
        # initialize entries, same properties were set to variables
        fg = "#333333"
        font = tk_font.Font(family='Calibri bold', size=10)
        height = 30

        self.entry_username = self.Entry(root, fg, font, {'x': 100, 'y': 110, 'w': 150, 'h': height})
        self.entry_password = self.Entry(root, fg, font, {'x': 380, 'y': 110, 'w': 150, 'h': height}, show="*")
        self.entry_account_number = self.Entry(root, fg, font, {'x': 180, 'y': 210, 'w': 110, 'h': height}, "center")
        self.entry_post_number = self.Entry(root, fg, font, {'x': 180, 'y': 350, 'w': 110, 'h': height}, "center")
        self.entry_save_loc = self.Entry(root, fg, font, {'x': 15, 'y': 450, 'w': 435, 'h': height})

    def initialize_checkboxes(self, root):
        # initialize checkbox, same properties were set to variables
        bg = '#F0EAD6'
        fg = "#333333"
        font = tk_font.Font(family='Calibri bold', size=10)
        width = 110
        height = 30

        self.Checkbutton(root, bg, fg, font, "Show Browser", {'x': 570, 'y': 280, 'w': width, 'h': height},
                         partial(self.commander, "Show Browser"))
        self.Checkbutton(root, bg, fg, font, "Stay Logged In", {'x': 570, 'y': 310, 'w': width, 'h': height},
                         partial(self.commander, "Stay Logged In"))

    def initialize_seprator(self, root):
        ttk.Separator(root, orient=HORIZONTAL).place(x=60, y=85, w=470, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=80, y=185, w=450, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=55, y=325, w=475, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=105, y=425, w=425, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=70, y=525, w=460, h=1)
        ttk.Separator(root, orient=VERTICAL).place(x=550, y=85, w=1, h=500)

    def Button(self, root, bg: str, fg: str, font: tk_font.Font, text: str, place: dict, command,
               justify: str = "center", relief: str = "flat") -> tk.Button:
        """
        The function to create and return a new TK button

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (tk_font.Font): font of the button's text
            text (str): text of the button
            place (dict): position of the button
            command : the function with its parameter
            justify (str): button text justify
            relief (str): relief of the button

        Returns:
            temp_button: A tk.Button object of button created with given information
        """

        temp_button = tk.Button(root, relief=relief, cursor="hand2")
        temp_button["bg"] = bg
        temp_button["font"] = font
        temp_button["fg"] = fg
        temp_button["justify"] = justify
        temp_button["text"] = text
        temp_button.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])
        temp_button["command"] = command

        return temp_button

    def Label(self, root, bg: str, fg: str, font: tk_font.Font, text: str, place: dict,
              anchor: str = 'w') -> tk.Label:
        """
        The function to create and return a new TK label

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (tk_font.Font): font of the label's text
            text (str): text of the label
            place (dict): position of the label
            justify (str): label text justify

        Returns:
            temp_label: A tk.Label object of label created with given information
        """

        temp_label = tk.Label(root, anchor=anchor)
        temp_label["bg"] = bg
        temp_label["font"] = font
        temp_label["fg"] = fg
        temp_label["text"] = text
        temp_label.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_label

    def Entry(self, root, fg: str, font: tk_font.Font, place: dict, justify: str = "left",
              borderwidth="1px", show="") -> tk.Entry:
        """
        The function to create and return a new TK entry

        Parameters:
            root : root frame of application
            fg (str): foreground color
            font (tk_font.Font): font of the entry's text
            place (dict): position of the entry
            justify (str): entry text justify
            borderwidth (str): entry border width

        Returns:
            temp_entry: A tk.Entry object of entry created with given information
        """

        temp_entry = tk.Entry(root)
        temp_entry["font"] = font
        temp_entry["fg"] = fg
        temp_entry["justify"] = justify
        temp_entry["borderwidth"] = borderwidth
        if show:
            temp_entry["show"] = show
        temp_entry.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_entry

    def Checkbutton(self, root, bg, fg: str, font: tk_font.Font, text: str, place: dict, command,
                    justify: str = "center") -> tk.Checkbutton:
        """
        The function to create and return a new TK checkbox

        Parameters:
            root : root frame of application
            bg (str): background color
            fg (str): foreground color
            font (tk_font.Font): font of the checkbox's text
            text (str): text of the checkbox
            place (dict): position of the checkbox
            command : the function with its parameter
            justify (str): checkbox text justify


        Returns:
            temp_checkbox: A tk.Checkbutton object of checkbox created with given information
        """

        temp_checkbox = tk.Checkbutton(root, cursor="hand2")
        temp_checkbox["bg"] = bg
        temp_checkbox["font"] = font
        temp_checkbox["fg"] = fg
        temp_checkbox["justify"] = justify
        temp_checkbox["text"] = text
        temp_checkbox["offvalue"] = "0"
        temp_checkbox["onvalue"] = "1"
        temp_checkbox["command"] = command
        temp_checkbox.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_checkbox

    def commander(self, command: str) -> None:
        """
        The function to clear lineEdit and message_show_result and set command's text to label_mode

        Parameters:
            command (str): The command user clicked on
        """
        pass
        # self.lineEdit.delete(0, "end")
        # self.message_show_result["text"] = ""
        # self.label_mode["text"] = command

    def adder(self):
        inputer = simpledialog.askstring(title="Accont Adding", prompt="Enter the new account name !")
        self.combobox['values'] += tuple([inputer])
        self.combobox.current(len(self.combobox['values']) - 1)

    def remover(self):
        self.combobox['values'] = tuple([i for i in self.combobox['values'] if i != self.combobox.get()])

    def open_directory(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.label_error_loc['text'] = ""
            self.entry_save_loc.delete(0, "end")
            self.entry_save_loc.insert(0, folder_selected)
        else:
            self.label_error_loc['text'] = "The location can't be selected !"


if __name__ == "__main__":
    roots = tk.Tk()
    roots.title("Instagram Crawler")

    widths, heights = 700, 650
    screenwidth, screenheight = roots.winfo_screenwidth(), roots.winfo_screenheight()
    align_str = '%dx%d+%d+%d' % (widths, heights, (screenwidth - widths) / 2, (screenheight - heights) / 2)
    roots.geometry(align_str)
    roots.resizable(width=False, height=False)
    roots.configure(background='#F0EAD6')

    app = GraphicalMenu(root=roots)
    roots.mainloop()
