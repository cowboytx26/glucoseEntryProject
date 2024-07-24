import tkinter
from tkinter import *
from tkcalendar import Calendar

class GlucoseEntry(Frame):

    def __init__(self, master=None):
        #self.masterFrame = Frame.__init__(self, master=None, bg='light blue')
        super().__init__(master)
        #self.masterFrame = Frame(self, bg='light blue')
        #self.masterFrame.pack(fill=BOTH, expand=1)
        self.image = PhotoImage(file="diabetes.png")
        self.imageResize = self.image.subsample(5,5)
        self.imageLabel = Label(image=self.imageResize, bg="white")
        self.imageLabel.pack(fill="both")
        self.glucoseEntryFrame = Frame(bg='light blue', padx=155)
        self.glucoseEntryFrame.pack()
        self.glucoseDateFrame = Frame(bg='light blue',padx=157)
        self.glucoseDateFrame.pack()
        self.glucoseStatusFrame = Frame(bg='light blue',padx=145, width=60)
        self.glucoseStatusFrame.pack()
        self.glucoseButtonFrame = Frame(bg='light blue', padx=175, relief=RAISED, borderwidth=1)
        self.glucoseButtonFrame.pack()
        self.glucoseEntryLabel = Label(self.glucoseEntryFrame, fg='black', bg='light blue', text="Enter Glucose Value:")
        self.glucoseEntryLabel.pack(side="left", padx=7)
        self.glucoseEntryInput = Entry(self.glucoseEntryFrame, width=5)
        self.glucoseEntryInput.pack(side="right")
        self.glucoseDateLabel = Label(self.glucoseDateFrame, fg='black', bg='light blue', text="Glucose date:")
        self.glucoseDateLabel.pack(side="left")
        self.glucoseDateInputLbl = Label(self.glucoseDateFrame,bg="yellow", fg="black", width=14)
        self.glucoseDateInputLbl.pack(side="right")
        self.glucoseDateInputLbl["text"] = ""
        self.glucoseStatusLabel = Label(self.glucoseStatusFrame, fg='black', bg='light blue', text="Application Status Good", width=105)
        self.glucoseStatusLabel.pack()
        self.glucoseNewBtn = Button(self.glucoseButtonFrame, text="New Glucose Entry", command=self.newEntry,state=NORMAL)
        self.glucoseWindowBtn = Button(self.glucoseButtonFrame, text="Select Date", command=self.openWindow,state=NORMAL, width=20)
        self.glucoseSaveBtn = Button(self.glucoseButtonFrame, text="Save Glucose Entry", command=self.saveEntry,state=NORMAL)
        self.glucoseExitBtn = Button(self.glucoseButtonFrame, text="Exit Application", command=self.exitApp, state=NORMAL, width=20)
        self.glucoseNewBtn.pack()
        self.glucoseWindowBtn.pack()
        self.glucoseSaveBtn.pack()
        self.glucoseExitBtn.pack()

    def newEntry(self):
        self.glucoseEntryInput.delete(0, tkinter.END)
        self.glucoseDateInputLbl["text"] = ""
        self.glucoseStatusLabel["text"] = "Values cleared"

    def openWindow(self):
        self.newWin = Toplevel(self.master, background='light blue')
        self.newWin.geometry("500x500")
        self.newWin.title("Enter date")
        self.cal = Calendar(self.newWin, width=30, font="Arial 20", selectmode='day', locale='en_US',
                            showweeknumbers=False, background='dark blue', foreground='green', normalforeground='white',
                            weekendforeground='white', othermonthforeground='yellow', othermonthweforeground='yellow',
                            headersforeground='green', selectforeground='red', date_pattern='mm/dd/y')
        self.cal.pack()
        self.chooseDateBtn = Button(self.newWin, text="Select Date", command=self.selectDate)
        self.chooseDateBtn.pack()

    def selectDate(self):
        self.glucoseDateInputLbl["text"] = str(self.cal.get_date())
        self.newWin.destroy()

    def saveEntry(self):
        self.valuesOK = True
        if self.glucoseDateInputLbl["text"] == "":
            self.glucoseStatusLabel["text"] = "Enter date by clicking Select Date!"
            self.valuesOK = False
        if self.glucoseEntryInput.get() == "":
            self.glucoseStatusLabel["text"] = "Please enter a glucose value!"
            self.valuesOK = False
        if self.valuesOK:
            file = open('glucoseEntry.txt', 'a')
            file.write(self.glucoseDateInputLbl["text"])
            file.write(",")
            file.write(self.glucoseEntryInput.get())
            file.write("\n")
            file.close()
            self.glucoseStatusLabel["text"] = "Values saved"

    def exitApp(self):
        exit(0)

def main():
    root = Tk()
    app = GlucoseEntry(root)
    root.wm_title("Glucose Tracker")
    root.geometry("500x365")
    root.mainloop()


if __name__ == "__main__":
    main()