# Victor Duan
# GUI for the Puzzle & Dragons damage calculator

import Tkinter

class padcalc_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # add widgets
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = self.entryVariable)
        self.entry.grid(column = 0, row = 0, sticky = "EW")
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        # button
        button = Tkinter.Button(self, text = u"Click me!", command = self.OnButtonClick)
        button.grid(column = 1, row = 0)

        # label
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable = self.labelVariable,
                              anchor = "w", fg = "white", bg = "blue")
        label.grid(column = 0, row = 1, columnspan = 2, sticky = "EW")
        self.labelVariable.set(u"Hello!")

        # enable resizing
        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + "You clicked the button!")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + "You pressed enter!")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = padcalc_tk(None)
    app.title("Puzzle & Dragons Damage Calculator")
    app.mainloop()