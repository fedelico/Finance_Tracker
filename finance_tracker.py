import tkinter as tk
from tkinter import ttk
import hashlib
import matplotlib

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

        # initializes pages
        self.pages = {'Home_Page':Home_Page, 'Main_Page':Main_Page, 'Plot_Page':Plot_Page}
        for name, P in self.pages.items():
            self.pages[name] = P(self)
            self.pages[name].grid(row = 0, column = 0, sticky = 'nsew')
        #make pages resizable with the main window
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0,weight = 1)

        self.show_page("Home_Page")

    def show_page(self, page):
        self.pages[page].tkraise()

class Home_Page(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        l1 = ttk.Label(self, text= "This is Home_Page")
        go_main_page = ttk.Button(self, text = "To Main_Page", command = lambda: container.show_page("Main_Page"))
        go_plot_page = ttk.Button(self, text = "To Plot_Page", command = lambda: container.show_page("Plot_Page"))
        
        l1.grid(row = 0, column = 2, sticky = 'n')
        go_main_page.grid(row = 3, column = 1, sticky = 's')
        go_plot_page.grid(row = 3, column = 3, sticky = 's')
        #make buttons resizable with the page(frame)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
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
