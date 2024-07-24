from breezypythongui.breezypythongui import *

class GlucoseEntry(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, width=500, height=300, title="Glucose Tracker")
        self.setBackground('light blue')
        self.glucoseEntryLabel = self.addLabel(text="Enter Glucose Value:", row=0, column=0)
        self.glucoseEntryInput = self.addFloatField(value=0.0, row=0, column=1, width=8, precision=1, state=NORMAL)
        self.glucoseDateLabel = self.addLabel(text="Enter the date of the Glucose Reading", row=1,column=0)
        self.glucoseDateInput = self.addTextField(text='', row=1,column=1,width=12)
        self.glucoseNewBtn = self.addButton(text="New Glucose Entry", row=2,column=0,command=self.newEntry,state=NORMAL)
        self.glucoseSaveBtn = self.addButton(text="Save Glucose Entry", row=2, column=1,command=self.saveEntry,state=NORMAL)
        self.appStatusLabel = self.addLabel(text="",row=3,column=0)

    def newEntry(self):
        self.glucoseEntryInput.setValue(0.0)
        self.glucoseDateInput.setText("")
        self.appStatusLabel["text"] = "Values cleared"

    def saveEntry(self):
        file = open('glucoseEntry.txt', 'a')
        file.write(self.glucoseDateInput.getValue())
        file.write(",")
        file.write(self.glucoseEntryInput.getValue())
        file.write("\n")
        file.close()
        self.appStatusLabel["text"] = "Values saved"



def main():
    GlucoseEntry().mainloop()


if __name__ == "__main__":
    main()