import tkinter as tk

class Finance_Tracker_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FinanceTracker")
        self.geometry("700x350")

        # initializes pages
        self.pages = {Home_Page, main_Page, Plot_Page}

        



















app = Finance_Tracker_App()
app.mainloop()
