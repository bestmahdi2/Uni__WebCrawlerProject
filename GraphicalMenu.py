import tkinter as tk
from tkinter import ttk, HORIZONTAL, LEFT, VERTICAL
import tkinter.font as tk_font
from functools import partial


class GraphicalMenu:
    """
        This is a class for gui use.

        Arguments:
            root (tk): root frame of application
    """

    def __init__(self, root):
        # region labels

        w, h = 700, 800


        # ttk.Separator(root, orient=HORIZONTAL).pack(side=LEFT, fill="y", padx=345, pady=177)

        # initialize labels, same properties were set to variables
        font_bold = tk_font.Font(family='Calibri bold', size=11)
        font = tk_font.Font(family='Calibri', size=11)
        bg = '#F0EAD6'
        fg = "#333333"
        height = 30

        label_main = self.Label(root, bg, '#CC397B', tk_font.Font(family='Calibri bold', size=23), "Instagram Crawler",
                                {'x': 10, 'y': 20, 'w': 680, 'h': 45}, "center")

        label_enter_data = self.Label(root, bg, fg, tk_font.Font(family='Calibri bold', size=13),
                                      "Login",
                                      {'x': 10, 'y': 70, 'w': 50, 'h': height})

        label_username = self.Label(root, bg, fg, font, "Username:",
                                    {'x': 10, 'y': 110, 'w': 80, 'h': height})

        label_password = self.Label(root, bg, fg, font, "Password:",
                                    {'x': 290, 'y': 110, 'w': 80, 'h': height})

        label_acounts = self.Label(root, bg, fg, font_bold, "Accounts",
                                   {'x': 10, 'y': 170, 'w': 73, 'h': height})

        label_acounts_number = self.Label(root, bg, fg, font, "Accounts Number (n):",
                                          {'x': 10, 'y': 210, 'w': 150, 'h': height})

        label_founded = self.Label(root, bg, fg, font, "Founded Accounts:",
                                   {'x': 10, 'y': 250, 'w': 135, 'h': height})

        label_posts = self.Label(root, bg, fg, font_bold, "Posts",
                                   {'x': 10, 'y': 310, 'w': 48, 'h': height})

        label_posts_number = self.Label(root, bg, fg, font, "Posts Number (m):",
                                        {'x': 10, 'y': 350, 'w': 130, 'h': height})

        label_save_loc = self.Label(root, bg, fg, font_bold, "Save Location",
                                    {'x': 10, 'y': 410, 'w': 95, 'h': height})

        label_times = self.Label(root, bg, fg, tk_font.Font(family='Calibri bold', size=10),
                                    "1/3, 10:02 passed, 01:02 left",
                                    {'x': 10, 'y': 550, 'w': 167, 'h': height})

        # endregions

        # region buttons

        # initialize buttons, same properties were set to variables
        bg = "#CC397B"
        fg = "#ffffff"
        font = tk_font.Font(family='Calibri bold', size=10)
        width = 110
        height = 30

        button_login = self.Button(root, bg, fg, font, "Login", {'x': 570, 'y': 110, 'w': width, 'h': height},
                                   partial(self.commander, "Login"))

        button_find_accounts = self.Button(root, bg, fg, font, "Find Accounts",
                                           {'x': 570, 'y': 150, 'w': width, 'h': height},
                                           partial(self.commander, "Find Accounts"))

        button_find_posts = self.Button(root, bg, fg, font, "Find Posts", {'x': 570, 'y': 190, 'w': width, 'h': height},
                                        partial(self.commander, "Find Posts"))

        button_save = self.Button(root, bg, fg, font, "Save", {'x': 570, 'y': 230, 'w': width, 'h': height},
                                  partial(self.commander, "Save"))

        button_add = self.Button(root, bg, fg, font, "➕", {'x': 460, 'y': 250, 'w': 30, 'h': height},
                                 partial(self.commander, "➕"))

        button_remove = self.Button(root, bg, fg, font, "➖", {'x': 500, 'y': 250, 'w': 30, 'h': height},
                                    partial(self.commander, "➖"))

        button_open = self.Button(root, bg, fg, font, "Open", {'x': 460, 'y': 450, 'w': 70, 'h': height},
                                  partial(self.commander, "Open"))

        # endregion

        # region entries
        # initialize entries, same properties were set to variables
        fg = "#333333"
        font = tk_font.Font(family='Calibri bold', size=10)
        height = 30

        entry_account_number = self.Entry(root, fg, font, "5", {'x': 180, 'y': 210, 'w': 110, 'h': height}, "center")

        entry_post_number = self.Entry(root, fg, font, "5", {'x': 180, 'y': 350, 'w': 110, 'h': height}, "center")

        entry_found_account = self.Entry(root, fg, font, "", {'x': 180, 'y': 250, 'w': 270, 'h': height})

        entry_username = self.Entry(root, fg, font, "", {'x': 100, 'y': 110, 'w': 150, 'h': height})

        entry_password = self.Entry(root, fg, font, "", {'x': 380, 'y': 110, 'w': 150, 'h': height})

        entry_save_loc = self.Entry(root, fg, font, "", {'x': 15, 'y': 450, 'w': 435, 'h': height})

        # endregion

        # region checkbox
        # initialize checkbox, same properties were set to variables
        bg = '#F0EAD6'
        fg = "#333333"
        font = tk_font.Font(family='Calibri bold', size=10)
        width = 110
        height = 30

        checkbox_browser = self.Checkbutton(root, bg, fg, font, "Show Browser",
                                            {'x': 570, 'y': 280, 'w': width, 'h': height},
                                            partial(self.commander, "Show Browser"))

        checkbox_stay_loggedin = self.Checkbutton(root, bg, fg, font, "Stay Logged In",
                                                  {'x': 570, 'y': 310, 'w': width, 'h': height},
                                                  partial(self.commander, "Stay Logged In"))

        # endregion

        # progress_bar = tk.Entry(root)
        # progress_bar["borderwidth"] = "1px"
        # ft = tk_font.Font(family='Calibri bold', size=10)
        # progress_bar["font"] = ft
        # progress_bar["fg"] = "#333333"
        # progress_bar["justify"] = "center"
        # progress_bar["text"] = ""
        # progress_bar.place(x=170, y=550, width=511, height=30)

        ttk.Separator(root, orient=HORIZONTAL).place(x=60, y=85, w=470, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=80, y=185, w=450, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=55, y=325, w=475, h=1)
        ttk.Separator(root, orient=HORIZONTAL).place(x=105, y=425, w=425, h=1)
        ttk.Separator(root, orient=VERTICAL).place(x=550, y=85, w=1, h=395)


        # ttk.Separator(root, orient=HORIZONTAL).place(x=10, y=155, w=520, h=1)
        # ttk.Separator(root, orient=HORIZONTAL).place(x=10, y=295, w=520, h=1)
        # ttk.Separator(root, orient=HORIZONTAL).place(x=10, y=395, w=520, h=1)

    def Button(self, root, bg: str, fg: str, font: tk_font.Font, text: str, place: dict, command,
               justify: str = "center",
               relief: str = "flat") -> tk.Button:
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
              justify: str = "left") -> tk.Label:
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

        temp_label = tk.Label(root)
        temp_label["bg"] = bg
        temp_label["font"] = font
        temp_label["fg"] = fg
        temp_label["text"] = text
        temp_label["justify"] = justify
        temp_label.place(x=place['x'], y=place['y'], width=place['w'], height=place['h'])

        return temp_label

    def Entry(self, root, fg: str, font: tk_font.Font, text: str, place: dict, justify: str = "left",
              borderwidth="1px") -> tk.Entry:
        """
        The function to create and return a new TK entry

        Parameters:
            root : root frame of application
            fg (str): foreground color
            font (tk_font.Font): font of the entry's text
            text (str): text of the entry
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
        temp_entry["text"] = text
        temp_entry["borderwidth"] = borderwidth
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

        temp_checkbox = tk.Checkbutton(root)
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


if __name__ == "__main__":
    roots = tk.Tk()
    roots.title("Instagram Crawler")

    widths, heights = 700, 800
    screenwidth, screenheight = roots.winfo_screenwidth(), roots.winfo_screenheight()
    align_str = '%dx%d+%d+%d' % (widths, heights, (screenwidth - widths) / 2, (screenheight - heights) / 2)
    roots.geometry(align_str)
    roots.resizable(width=False, height=False)
    roots.configure(background='#F0EAD6')

    app = GraphicalMenu(root=roots)
    roots.mainloop()
