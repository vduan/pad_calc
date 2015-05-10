# Victor Duan
# GUI for the Puzzle & Dragons damage calculator

import Tkinter

class padcalc_tk(Tkinter.Tk):
    def __init__(self, parent):        
        # data
        self.types = ['fire', 'water', 'wood', 'dark', 'light', 'heart']
        self.typeDmg = [0, 0, 0, 0, 0, 0]
        self.typeCombos = [[], [], [], [], [], []]
        self.typeRe = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.ls1Atk = 1.0
        self.ls2Atk = 1.0
        self.ls1Rcv = 1.0
        self.ls2Rcv = 1.0
        self.atkEntryVariables = []
        self.comboEntryVariables = []
        self.reEntryVariables1 = []
        self.reEntryVariables2 = []
        # self.lsEntryVariables1 = []
        # self.lsEntryVariables2 = []

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
            # add label so you know what it is
            typeStrVar = Tkinter.StringVar()
            typeLabel = Tkinter.Label(self, textvariable = typeStrVar,
                                anchor = "w", fg = "black", bg = "white")
            typeLabel.grid(column = 0, row = i + 1, sticky = "EW")
            typeStrVar.set(t + " attack")

            x = Tkinter.StringVar()
            self.atkEntryVariables.append(x)
            self.entry = Tkinter.Entry(self, textvariable = x)
            self.entry.grid(column = 1, row = i + 1, sticky = "EW")
            self.entry.bind("<Return>",
                lambda event, arg=i: self.OnPressEnterAttack(event, arg))
            x.set(u"Enter " + t + " attack here.")


        # attack and combo update label
        self.atkComboUpdateLabel = Tkinter.StringVar()
        atkComboUpdateLabel = Tkinter.Label(self, textvariable = self.atkComboUpdateLabel,
                            anchor = "w", fg = "white", bg = "blue")
        atkComboUpdateLabel.grid(column = 0, row = 7, columnspan = 4, sticky = "EW")


        # damage label
        self.damageLabel = Tkinter.StringVar()
        damageLabel = Tkinter.Label(self, textvariable = self.damageLabel,
                              anchor = "w", fg = "white", bg = "blue")
        damageLabel.grid(column = 0, row = 8, columnspan = 4, sticky = "EW")
        self.damageLabel.set(self.getTypeDmg())

        ### Combos
        # combo label
        comboHeadStrVar = Tkinter.StringVar()
        comboHeadLabel = Tkinter.Label(self, textvariable = comboHeadStrVar,
                                anchor = "w", fg = "black", bg = "white")
        comboHeadLabel.grid(column = 2, row = 0, columnspan = 2, sticky = "EW")
        comboHeadStrVar.set("Combos: e.g. fire: 3 3 6 for two sets of 3 and a set of 6")

        for i, t in enumerate(self.types):
            # add label so you know what it is
            typeStrVar = Tkinter.StringVar()
            typeLabel = Tkinter.Label(self, textvariable = typeStrVar,
                                anchor = "w", fg = "black", bg = "white")
            typeLabel.grid(column = 2, row = i + 1, sticky = "EW")
            typeStrVar.set(t + " combos") 

            x = Tkinter.StringVar()
            self.comboEntryVariables.append(x)
            self.entry = Tkinter.Entry(self, textvariable = x)
            self.entry.grid(column = 3, row = i + 1, sticky = "EW")
            self.entry.bind("<Return>",
                lambda event, arg = i: self.OnPressEnterCombo(event, arg))
            x.set(u"Enter " + t + " combos here.")

        # combo label
        self.comboLabel = Tkinter.StringVar()
        comboLabel = Tkinter.Label(self, textvariable = self.comboLabel,
                            anchor = "w", fg = "white", bg = "blue")
        comboLabel.grid(column = 0, row = 9, columnspan = 4, sticky = "EW")
        self.comboLabel.set(self.getCombos())

        ### Row enhance
        # RE label
        reHeadStrVar = Tkinter.StringVar()
        reHeadLabel = Tkinter.Label(self, textvariable = reHeadStrVar,
                            anchor = "w", fg = "black", bg = "white")
        reHeadLabel.grid(column = 0, row = 10, sticky = "EW")
        reHeadStrVar.set("Row Enhance")

        for i, t in enumerate(self.types):
            # add label so you know what it is
            typeStrVar = Tkinter.StringVar()
            typeLabel = Tkinter.Label(self, textvariable = typeStrVar,
                            anchor = "w", fg = "black", bg = "white")
            typeLabel.grid(column = 0, row = i + 11, sticky = "EW")
            typeStrVar.set(t + " RE")

            x = Tkinter.StringVar()
            y = Tkinter.StringVar()
            self.reEntryVariables1.append(x)
            self.reEntryVariables2.append(y)
            self.entry = Tkinter.Entry(self, textvariable = x)
            self.entry.grid(column = 1, row = i + 11, sticky = "EW")
            self.entry.bind("<Return>",
                lambda event, arg = i: self.OnPressEnterRe1(event, arg))
            x.set(u"Enter " + t + " rows here.")
            self.entry = Tkinter.Entry(self, textvariable = y)
            self.entry.grid(column = 2, row = i + 11, columnspan = 2, sticky = "EW")
            self.entry.bind("<Return>",
                lambda event, arg = i: self.OnPressEnterRe2(event, arg))
            y.set(u"Enter " + t + " RE awakenings here.")

        # row enhance update label
        self.reUpdateLabel = Tkinter.StringVar()
        reUpdateLabel = Tkinter.Label(self, textvariable = self.reUpdateLabel,
                            anchor = "w", fg = "white", bg = "blue")
        reUpdateLabel.grid(column = 0, row = 17, columnspan = 4, sticky = "EW")

        # row enhance label
        self.reLabel = Tkinter.StringVar()
        reLabel = Tkinter.Label(self, textvariable = self.reLabel,
                        anchor = "w", fg = "white", bg = "blue")
        reLabel.grid(column = 0, row = 18, columnspan = 4, sticky = "EW")
        self.reLabel.set(self.getRe())

        ### leader skill boosts
        # LS label
        lsHeadStrVar = Tkinter.StringVar()
        lsHeadLabel = Tkinter.Label(self, textvariable = lsHeadStrVar,
                            anchor = "w", fg = "black", bg = "white")
        lsHeadLabel.grid(column = 0, row = 19, sticky = "EW")
        lsHeadStrVar.set("Leader Skills")

        ls1AtkStrVar = Tkinter.StringVar()
        ls1AtkLabel = Tkinter.Label(self, textvariable = ls1AtkStrVar,
                        anchor = "w", fg = "black", bg = "white")
        ls1AtkLabel.grid(column = 0, row = 20, sticky = "EW")
        ls1AtkStrVar.set("Leader Skill 1 Atk Multiplier")

        ls2AtkStrVar = Tkinter.StringVar()
        ls2AtkLabel = Tkinter.Label(self, textvariable = ls2AtkStrVar,
                        anchor = "w", fg = "black", bg = "white")
        ls2AtkLabel.grid(column = 2, row = 20, sticky = "EW")
        ls2AtkStrVar.set("Leader Skill 2 Atk Multiplier")

        x = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = x)
        self.entry.grid(column = 1, row = 20, sticky = "EW")
        self.entry.bind("<Return>", self.OnPressEnterLs1)
        x.set(u"Enter Leader Skill 1 Atk Multiplier")
        self.lsEntryVariables1 = x

        y = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = y)
        self.entry.grid(column = 3, row = 20, sticky = "EW")
        self.entry.bind("<Return>", self.OnPressEnterLs2)
        y.set(u"Enter Leader Skill 2 Atk Multiplier")
        self.lsEntryVariables2 = y

        ls1RcvStrVar = Tkinter.StringVar()
        ls1RcvLabel = Tkinter.Label(self, textvariable = ls1RcvStrVar,
                        anchor = "w", fg = "black", bg = "white")
        ls1RcvLabel.grid(column = 0, row = 21, sticky = "EW")
        ls1RcvStrVar.set("Leader Skill 1 Rcv Multiplier")

        ls2RcvStrVar = Tkinter.StringVar()
        ls2RcvLabel = Tkinter.Label(self, textvariable = ls2RcvStrVar,
                        anchor = "w", fg = "black", bg = "white")
        ls2RcvLabel.grid(column = 2, row = 21, sticky = "EW")
        ls2RcvStrVar.set("Leader Skill 2 Rcv Multiplier")

        x = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = x)
        self.entry.grid(column = 1, row = 21, sticky = "EW")
        self.entry.bind("<Return>", self.OnPressEnterLs3)
        x.set(u"Enter Leader Skill 1 Rcv Multiplier")
        self.lsEntryVariables3 = x

        y = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = y)
        self.entry.grid(column = 3, row = 21, sticky = "EW")
        self.entry.bind("<Return>", self.OnPressEnterLs4)
        y.set(u"Enter Leader Skill 2 Rcv Multiplier")
        self.lsEntryVariables4 = y

        # leader skill update label
        self.lsUpdateLabel = Tkinter.StringVar()
        lsUpdateLabel = Tkinter.Label(self, textvariable = self.lsUpdateLabel,
                            anchor = "w", fg = "white", bg = "blue")
        lsUpdateLabel.grid(column = 0, row = 22, columnspan = 4, sticky = "EW")

        # leader skill attack label
        self.lsAtkLabel = Tkinter.StringVar()
        lsAtkLabel = Tkinter.Label(self, textvariable = self.lsAtkLabel,
                        anchor = "w", fg = "white", bg = "blue")
        lsAtkLabel.grid(column = 0, row = 23, columnspan = 4, sticky = "EW")
        self.lsAtkLabel.set(self.getLsAtk())

        # leader skill recovery label
        self.lsRcvLabel = Tkinter.StringVar()
        lsRcvLabel = Tkinter.Label(self, textvariable = self.lsRcvLabel,
                        anchor = "w", fg = "white", bg = "blue")
        lsRcvLabel.grid(column = 0, row = 24, columnspan = 4, sticky = "EW")
        self.lsRcvLabel.set(self.getLsRcv())

        # do the calculation
        self.totalDamageLabel = Tkinter.StringVar()
        totalDamageLabel = Tkinter.Label(self, textvariable = self.totalDamageLabel,
                            anchor = "w", fg = "white", bg = "black")
        totalDamageLabel.grid(column = 0, row = 25, columnspan = 4, sticky = "EW")
        self.totalDamageLabel.set(self.getTotalDamage())

        button = Tkinter.Button(self, text=u"Update Damage Calculation",
                        command = self.OnButtonClick)
        button.grid(column = 0, row = 26, columnspan = 4, sticky = "EW")


        # enable resizing
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.resizable(True, False)
        self.update()
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)


    def OnPressEnterAttack(self, event, index):
        self.atkComboUpdateLabel.set("You updated " + self.types[index] + " attack.")
        self.typeDmg[index] = int(self.atkEntryVariables[index].get())
        # now update the damage label
        self.damageLabel.set(self.getTypeDmg())

    def OnPressEnterCombo(self, event, index):
        self.atkComboUpdateLabel.set("You updated " + self.types[index] + " combos.")
        # new combos for that type
        self.typeCombos[index] = [int(x) for x in self.comboEntryVariables[index].get().split()]
        # now update the combo label
        self.comboLabel.set(self.getCombos())

    def OnPressEnterRe1(self, event, index):
        self.reUpdateLabel.set("You updated " + self.types[index] + " rows.")
        self.typeRe[index][0] = int(self.reEntryVariables1[index].get())
        # now update the re label
        self.reLabel.set(self.getRe())

    def OnPressEnterRe2(self, event, index):
        self.reUpdateLabel.set("You updated " + self.types[index] + " RE awakenings.")
        self.typeRe[index][1] = int(self.reEntryVariables2[index].get())
        # now update the re label
        self.reLabel.set(self.getRe())

    def OnPressEnterLs1(self, event):
        self.lsUpdateLabel.set("You updated Leader Skill 1 Atk Multiplier.")
        self.ls1Atk = float(self.lsEntryVariables1.get())
        # now update the ls label
        self.lsAtkLabel.set(self.getLsAtk())

    def OnPressEnterLs2(self, event):
        self.lsUpdateLabel.set("You updated Leader Skill 2 Atk Multiplier.")
        self.ls2Atk = float(self.lsEntryVariables2.get())
        # now update the ls label
        self.lsAtkLabel.set(self.getLsAtk())

    def OnPressEnterLs3(self, event):
        self.lsUpdateLabel.set("You updated Leader Skill 1 Rcv Multiplier.")
        self.ls1Rcv = float(self.lsEntryVariables3.get())
        # now update the ls label
        self.lsRcvLabel.set(self.getLsRcv())

    def OnPressEnterLs4(self, event):
        self.lsUpdateLabel.set("You updated Leader Skill 2 Rcv Multiplier.")
        self.ls2Rcv = float(self.lsEntryVariables4.get())
        # now update the ls label
        self.lsRcvLabel.set(self.getLsRcv())

    def OnButtonClick(self):
        self.totalDamageLabel.set(self.getTotalDamage())
        
    # return a string that displays type damage
    def getTypeDmg(self):
        pieces = []
        for i, t in enumerate(self.types):
            pieces.append(t + ": " + str(self.typeDmg[i]))

        return '\t\t'.join(pieces)

    def getCombos(self):
        pieces = []
        for i, t in enumerate(self.types):
            pieces.append(t + ": " + str(self.typeCombos[i]))

        return '\t\t'.join(pieces)

    def getRe(self):
        pieces = []
        for i, t in enumerate(self.types):
            rows, awakenings = self.typeRe[i]
            pieces.append(t + ": " + str(rows) + " rows, " + str(awakenings) + " RE")

        return '\t\t'.join(pieces)

    def getLsAtk(self):
        pieces = []
        pieces.append("Leader Skill 1 Atk Multiplier: " + str(self.ls1Atk))
        pieces.append("Leader Skill 2 Atk Multiplier: " + str(self.ls2Atk))

        return '\t\t'.join(pieces)

    def getLsRcv(self):
        pieces = []
        pieces.append("Leader Skill 1 Rcv Multiplier: " + str(self.ls1Rcv))
        pieces.append("Leader Skill 2 Rcv Multiplier: " + str(self.ls2Rcv))

        return '\t\t'.join(pieces)

    def getTotalDamage(self):
        self.numCombos = sum([len(x) for x in self.typeCombos])
        self.comboMultiplier = 1.0 + (float(self.numCombos) - 1) / 4.0
        self.typeMultipliers = [sum([1.0 + (float(x) - 3) / 4.0 for x in y]) for y in self.typeCombos]

        typeDamage = []

        pieces = []
        for i, t in enumerate(self.types):
            reMultiplier = 1.0 + 0.1 * self.typeRe[i][0] * self.typeRe[i][1]
            dmg = self.typeDmg[i] * self.comboMultiplier * self.typeMultipliers[i] * reMultiplier * self.ls1Atk * self.ls2Atk
            typeDamage.append(dmg)
            pieces.append(t + " damage: " + str(dmg))

        pieces.append("total damage: " + str(sum(typeDamage)))
        return '\t\t'.join(pieces)


if __name__ == "__main__":
    app = padcalc_tk(None)
    app.title("Puzzle & Dragons Damage Calculator")
    app.mainloop()