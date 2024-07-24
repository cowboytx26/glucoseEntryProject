"""
Author:  Brian Wiatrek
Date written: 07/24/24
Assignment:   Final Project
Short Desc:   This python program will allow a diabetic user to input his/her glucose reading along with a date.  These
              values will be stored in a file so that the user can provide the values to the doctor for purposes of
              monitoring the disease
"""
import tkinter
from tkinter import *
from tkcalendar import Calendar

class GlucoseEntry(Frame):
    """
    Short Desc: This object is responsible for displaying the primary application window which allows for the entry
                of a glucose value - which must be a positive integer, and the date of the glucose value.  The user
                keys in the glucose value into an entry field which only allows a positive integer or an empty string.
                The glucose date must be selected with the tkcalendar widget.  This ensures that only a date is input.
                The calendar widget opens when the user presses the select date button which opens the tkcalendar widget
                in a second window.  When user hits the select date button on the second window, the date is saved in
                the date entry labal (which is not actually an entry field), and then the second window is closed.  When
                the user hits the Save Glucose Entry button, the values are written to the file if the values pass a
                second validation test to ensure that they were actually keyed in.  The application can be exited by
                pressing the exit button.
    """

    def __init__(self, master=None):
        super().__init__(master)
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
        #reg is the validation method for the Glucose Value Entry.  Any values input should be either an empty string
        #or a positive integer
        reg = self.master.register(self.callback)
        self.glucoseEntryInput.config(validate="key", validatecommand=(reg, '%P'))
        self.glucoseDateLabel = Label(self.glucoseDateFrame, fg='black', bg='light blue', text="Glucose date:")
        self.glucoseDateLabel.pack(side="left")
        self.glucoseDateInputLbl = Label(self.glucoseDateFrame,bg="yellow", fg="black", width=14)
        self.glucoseDateInputLbl.pack(side="right")
        self.glucoseDateInputLbl["text"] = ""
        self.glucoseStatusLabel = Label(self.glucoseStatusFrame, fg='black', bg='light blue',
                                        text="Application Status Good", width=105)
        self.glucoseStatusLabel.pack()
        self.glucoseWindowBtn = Button(self.glucoseButtonFrame, text="Select Date", command=self.openWindow,
                                       state=NORMAL, width=20)
        self.glucoseSaveBtn = Button(self.glucoseButtonFrame, text="Save Glucose Entry", command=self.saveEntry,
                                     state=NORMAL)
        self.glucoseExitBtn = Button(self.glucoseButtonFrame, text="Exit Application", command=self.exitApp,
                                     state=NORMAL, width=20)
        self.glucoseWindowBtn.pack()
        self.glucoseSaveBtn.pack()
        self.glucoseExitBtn.pack()

    def openWindow(self):
        """
        This method opens a second window so that the user can select a date that corresponds to the date of the
        glucose measurement.  By utilizing the tkcalendar widget, the program ensures that the user only selects a
        valid date.
        """
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
        """
        This method is used to update the glucoseDateInputLbl field with the date of the glucose measurement, and then
        close the second window with the tkcalendar widget.
        """
        self.glucoseDateInputLbl["text"] = str(self.cal.get_date())
        self.newWin.destroy()

    def saveEntry(self):
        """
        This method is responsible for saving the values entered by the user to a file.  This method first ensures that
        the user actually entered values in the application before saving them to the file.  The method also
        sends an error status to the status bar in the event that the values could not be saved to the file.  After the
        values are saved to the file successfully, the app clears the entry fields so that the user can input the next
        set of values if applicable.
        """
        self.valuesOK = True
        if self.glucoseDateInputLbl["text"] == "":
            self.glucoseStatusLabel["text"] = "Enter date by clicking Select Date!"
            self.valuesOK = False
        if self.glucoseEntryInput.get() == "":
            self.glucoseStatusLabel["text"] = "Please enter a glucose value!"
            self.valuesOK = False
        if self.valuesOK:
            try:
                file = open('glucoseEntry.txt', 'a')
                file.write(self.glucoseDateInputLbl["text"])
                file.write(",")
                file.write(self.glucoseEntryInput.get())
                file.write("\n")
                file.close()
                self.glucoseStatusLabel["text"] = "Values saved"
                self.glucoseEntryInput.delete(0, tkinter.END)
                self.glucoseDateInputLbl["text"] = ""
            except IOError:
                self.glucoseStatusLabel["text"] = "Unable to save values"

    def callback(self, input):
        """
        This method validates the input values in the glucose measurement entry field.  The method allows the user to
        key in a positive integer or the empty string.  The empty string is allowed so that the user can clear the field
        in case a mistake was made.  The empty string cannot be saved, however.
        """
        validInput = False
        try:
            validInt = int(input)
            if validInt > 0:
                validInput = True
        except ValueError:
            if input == "":
                return True
            else:
                self.glucoseStatusLabel["text"] = str(input) + "Please enter a positive integer"
                return False
        if validInput:
            return True


    def exitApp(self):
        """
        This method allows the user to exit the application.
        """
        exit(0)

def main():
    root = Tk()
    app = GlucoseEntry(root)
    root.wm_title("Glucose Tracker")
    root.geometry("500x275")
    root.mainloop()


if __name__ == "__main__":
    main()