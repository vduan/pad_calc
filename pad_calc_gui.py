# Victor Duan
# GUI for the Puzzle & Dragons damage calculator

import Tkinter

class padcalc_tk(Tkinter.Tk):
    def __init__(self, parent):        
        # data
        self.types = ['fire', 'water', 'wood', 'dark', 'light', 'heart']
        self.typeDmg = [0, 0, 0, 0, 0, 0]
        self.entryVariables = []

        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.grid()

        ### Type Damage entering
        # type damage label
        typeHeadStrVar = Tkinter.StringVar()
        typeHeadLabel = Tkinter.Label(self, textvariable = typeHeadStrVar,
                                anchor = "w", fg = "black", bg = "white")
        typeHeadLabel.grid(column = 0, row = 0, columnspan = 2, sticky = "EW")
        typeHeadStrVar.set("Type Damage")

        for i, t in enumerate(self.types):
            # add label to you know what it is
            typeStrVar = Tkinter.StringVar()
            typeLabel = Tkinter.Label(self, textvariable = typeStrVar,
                                anchor = "w", fg = "black", bg = "white")
            typeLabel.grid(column = 0, row = i + 1, sticky = "EW")
            typeStrVar.set(t)

            x = Tkinter.StringVar()
            self.entryVariables.append(x)
            self.entry = Tkinter.Entry(self, textvariable = x)
            self.entry.grid(column = 1, row = i + 1, sticky = "EW")
            self.entry.bind("<Return>",
                lambda event, arg=i: self.OnPressEnter(event, arg))
            x.set(u"Enter " + t + " damage here.")


        # update label
        self.updateLabel = Tkinter.StringVar()
        updateLabel = Tkinter.Label(self, textvariable = self.updateLabel,
                            anchor = "w", fg = "white", bg = "blue")
        updateLabel.grid(column = 0, row = 7, columnspan = 2, sticky = "EW")


        # damage label
        self.damageLabel = Tkinter.StringVar()
        damageLabel = Tkinter.Label(self, textvariable = self.damageLabel,
                              anchor = "w", fg = "white", bg = "blue")
        damageLabel.grid(column = 0, row = 8, columnspan = 2, sticky = "EW")
        self.damageLabel.set(self.getTypeDmg())



        ### Combos



        # enable resizing
        self.grid_columnconfigure(1, weight = 1)
        self.resizable(True, False)
        self.update()
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.damageLabel.set(self.entryVariable.get() + "You clicked the button!")
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event, index):
        self.updateLabel.set("You updated " + self.types[index])
        self.typeDmg[index] = int(self.entryVariables[index].get())
        # now update the damage label
        self.damageLabel.set(self.getTypeDmg())

    # return a string that displays type damage
    def getTypeDmg(self):
        pieces = []
        for i, t in enumerate(self.types):
            pieces.append(t + ": " + str(self.typeDmg[i]))

        return '\t\t'.join(pieces)

if __name__ == "__main__":
    app = padcalc_tk(None)
    app.title("Puzzle & Dragons Damage Calculator")
    app.mainloop()