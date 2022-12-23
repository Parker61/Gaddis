import tkinter
class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.canvas=tkinter.Canvas(self.main_window,width=200,height=500)
        self.canvas.create_line(10,190,95,10,190,190,10,190)
        self.canvas.create_rectangle(10,190,190,290)
        self.canvas.pack()

        tkinter.mainloop()
my_GUI=MyGUI()