import tkinter as tk
from tkinter import ttk
import hashlib
import matplotlib
from data_management import Data_base


class Finance_Tracker_App(tk.Tk):
    """
    This is a desktop program that allows multiple people to
        (1)record their daily expenses/revenues 
        (2)provides them with visualization tools
    """
    def __init__(self):
        super().__init__()
        self.title("FinanceTracker")
        self.geometry("700x350")

        #initialize data_base
        self.db = Data_base("test")
        self.current_user = ""

        # initializes pages
        self.pages = {'Login_Page':Login_Page, 'Main_Page':Main_Page, 'Plot_Page':Plot_Page, 'Sign_up_Page':Sign_up_Page}
        for name, P in self.pages.items():
            self.pages[name] = P(self)
            self.pages[name].grid(row = 0, column = 0, sticky = 'nsew')
        #make pages resizable with the main window
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0,weight = 1)

        self.show_page("Login_Page")
        

    def show_page(self, page):
        self.pages[page].tkraise()

class Login_Page(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        name, password = tk.StringVar(), tk.StringVar()
        l1 = ttk.Label(self, text= "This is Login_Page")
        sign_up = ttk.Label(self, text= "Sign Up", font = ("bold", 15))
        sign_up.bind("<Button-1>", container.show_page("Sign_up_Page")) # left click to register
        user_name = ttk.Label(self, text = "USER NAME", font = ("bold", 14))
        name_entry = ttk.Entry(self, textvariable = name)
       
        pass_word = ttk.Label(self, text = "PASS WORD", font = ("bold", 14))
        pswd_entry = ttk.Entry(self, textvariable = password, show = '*')
        
        send = ttk.Button(self, text = "login", command = lambda: container.db.check_login(container, name, password))

        l1.grid(row = 0, column = 0, columnspan = 4, sticky = 'we')
        sign_up.grid(row = 0, column = 3)
        user_name.grid(row = 1, column = 2)
        name_entry.grid(row = 1, column = 3)
        pass_word.grid(row = 2, column = 2)
        pswd_entry.grid(row = 2, column = 3)
        send.grid(row = 3, column = 3)
        #make buttons resizable with the page(frame)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        


class Main_Page(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        l1 = ttk.Label(self, text= "This is Main_Page")
        go_home_page = ttk.Button(self, text = "To Home_Page", command =lambda: container.show_page("Home_Page"))
        go_plot_page = ttk.Button(self, text = "To Plot_Page", command =lambda: container.show_page("Plot_Page"))
        
        l1.grid(row = 0, column = 2, sticky = 'n')
        go_home_page.grid(row = 3, column = 1, sticky = 's')
        go_plot_page.grid(row = 3, column = 3, sticky = 's')
        #make buttons resizable with the page(frame)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(3, weight = 1)

class Plot_Page(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        l1 = ttk.Label(self, text= "This is Plot_Page")
        go_home_page = ttk.Button(self, text = "To Home_Page", command = lambda: container.show_page("Home_Page"))
        go_main_page = ttk.Button(self, text = "To Main_Page", command = lambda: container.show_page("Main_Page"))
        
        l1.grid(row = 0, column = 2, sticky = 'n')
        go_main_page.grid(row = 3, column = 1, sticky = 's')
        go_home_page.grid(row = 3, column = 3, sticky = 's')
        #make buttons resizable with the page(frame)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(3, weight = 1)







app = Finance_Tracker_App()
app.mainloop()
