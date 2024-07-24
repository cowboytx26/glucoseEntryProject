import tkinter
from tkinter import *

def newEntry(self):
    self.glucoseEntryInput.delete(0, tkinter.END)
    self.glucoseDateInput.delete(0, tkinter.END)
    self.glucoseStatusLabel["text"] = "Values cleared"

def saveEntry(self):
    file = open('glucoseEntry.txt', 'a')
    file.write(self.glucoseDateInput.get())
    file.write(",")
    file.write(self.glucoseEntryInput.get())
    file.write("\n")
    file.close()
    self.glucoseStatusLabel["text"] = "Values saved"

def main():
    root = Tk()
    #app = GlucoseEntry(root)
    root.wm_title("Glucose Tracker")
    root.geometry("500x300")
    masterFrame = Frame(master=None, bg='light blue')
    #master = master
    masterFrame.pack(fill=BOTH, expand=1)
    glucoseEntryFrame = Frame(masterFrame, bg='light blue', padx=155)
    glucoseEntryFrame.pack()
    glucoseDateFrame = Frame(masterFrame, bg='light blue',padx=100)
    glucoseDateFrame.pack()
    glucoseStatusFrame = Frame(masterFrame, bg='light blue',padx=175)
    glucoseStatusFrame.pack()
    glucoseEntryLabel = Label(glucoseEntryFrame, fg='black', bg='light blue', text="Enter Glucose Value:")
    #glucoseEntryLabel.grid(row=0,column=0)
    glucoseEntryLabel.pack(side='left', padx=7)
    glucoseEntryInput = Entry(glucoseEntryFrame, width=5)
    #glucoseEntryInput.grid(row=0,column=1)
    glucoseEntryInput.pack(side='right')
    glucoseDateLabel = Label(glucoseDateFrame, fg='black', bg='light blue', text="Enter the date:")
    glucoseDateLabel.pack(side="left")
    glucoseDateInput = Entry(glucoseDateFrame,width=9)
    glucoseDateInput.pack(side="right")
    glucoseStatusLabel = Label(glucoseStatusFrame, fg='black', bg='light blue', text="Application Status Good")
    glucoseStatusLabel.pack()
    glucoseNewBtn = Button(masterFrame, text="New Glucose Entry", command=None,state=NORMAL)
    glucoseSaveBtn = Button(masterFrame, text="Save Glucose Entry", command=None,state=NORMAL)
    glucoseNewBtn.pack()
    glucoseSaveBtn.pack()
    root.mainloop()


if __name__ == "__main__":
    main()