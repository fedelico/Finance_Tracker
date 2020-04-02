import tkinter as tk
from tkinter import ttk
import matplotlib
from data_management import Data_base, encrypt

def error_msg(msg):
    warning = tk.Tk()
    warning.title("error".upper())
    warning_msg = tk.Label(warning, text = msg, font = ("bold", 14))
    warning_msg.pack()
    ok_button = tk.Button(warning, text = "OK", font = ("bold", 14), command = lambda: warning.destroy())
    ok_button.pack()
    warning.mainloop()

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

class Sign_up_Page(tk.Frame):
    def __init__(self, container):
        self.container = container
        self.name, self.password, self.password_check = tk.StringVar(), tk.StringVar(), tk.StringVar()
        super().__init__(container)
        l2 = ttk.Label(text = "This is Sign_up_Page")
        go_login = ttk.Button(self, text = "Back to login", command = lambda: container.show_page("Login_Page"))
        user_name = ttk.Label(self, text = "USER NAME", font = ("bold", 14))
        self.name_entry = Labeled_Entry(self, default_text = "Enter your user name here", textvariable = self.name)
       
        pass_word = ttk.Label(self, text = "PASS WORD", font = ("bold", 14))
        self.pswd_entry = Labeled_Entry(self, default_text = "Enter your password here", textvariable = self.password, show = '*')
        
        pass_word_confirmation = ttk.Label(self, text = "CONFIRM YOUR PASS WORD")
        self.pass_word_confirm_entry = Labeled_Entry(self, default_text = "Enter your password again", textvariable = self.password_check, show = '*')
        
        send = ttk.Button(self, text = "login", command = lambda: self.add_new_user())

        l2.grid(row = 0, column = 0, columnspan = 4, sticky = 'we')
        go_login.grid(row = 5, column = 1)
        user_name.grid(row = 1, column = 2)
        self.name_entry.grid(row = 1, column = 3)
        pass_word.grid(row = 2, column = 2)
        self.pswd_entry.grid(row = 2, column = 3)
        pass_word_confirmation.grid(row = 3, column = 2)
        self.pass_word_confirm_entry.grid(row = 3, column = 3)
        send.grid(row = 4, column = 3)
        #make buttons resizable with the page(frame)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1)
        self.grid_rowconfigure(5, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
    
    def add_new_user(self):
        if self.name.get() == '' :
            error_msg("please enter your name".upper())

        elif self.password.get() == '':
            error_msg("please enter your password".upper())
        
        elif self.password_check.get() == '':
            error_msg("please confirm your password".upper())

        elif self.password.get() != self.password_check.get():
            error_msg("pass word does not match".upper())
            
        elif self.container.db.get_name(self.name.get()) != None:
            error_msg("user name already been used".upper())

        else:
            self.container.db.insert_data("users", (self.name, self.password, 0))
            self.name_entry.delete(0, tk.END)
            self.pswd_entry.delete(0, tk.END)
            self.container.show_page("Login_Page")



class Login_Page(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        name, password = tk.StringVar(), tk.StringVar()
        l1 = ttk.Label(self, text= "This is Login_Page")
        sign_up = ttk.Label(self, text= "Sign Up", font = ("bold", 15))
        sign_up.bind("<Button-1>", lambda event: container.show_page("Sign_up_Page")) # left click to register
        user_name = ttk.Label(self, text = "USER NAME", font = ("bold", 14))
        name_entry = Labeled_Entry(self, default_text = "Enter your user name here", textvariable = name)
       
        pass_word = ttk.Label(self, text = "PASS WORD", font = ("bold", 14))
        pswd_entry = Labeled_Entry(self, default_text = "Enter your password here", textvariable = password, show = '*')
        
        send = ttk.Button(self, text = "login", command = lambda: self.check_login(container, name.get(), password.get()))

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

    def check_login(self, container, name, password):
        if name == '':
            error_msg("please enter your name")
        elif password == '':
            error_msg("please enter your password")
        else:
            
            real_pswd = container.db.get_pswd(name)
            if real_pswd == encrypt(password):
                container.current_user = name
                container.show_page("Main_Page")
                return True
            else:
                error_msg("wrong user name or password".upper())

class Labeled_Entry(ttk.Entry):
    def __init__(self, container, default_text = "", **kwargs):
        ttk.Entry.__init__(self, container, **kwargs)
        self.default_text = default_text
        self.bind("<FocusIn>", self.on_entry)
        self.bind("<FocusOut>", self.on_exit)
        self.on_exit()

    def on_entry(self, event = None):
        if self.get() == self.default_text:
            self.delete(0, tk.END)

    def on_exit(self, event = None):
        if not self.get():
            self.insert(0, self.default_text)
        


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






if __name__ == "__main__":
    app = Finance_Tracker_App()
    app.mainloop()
