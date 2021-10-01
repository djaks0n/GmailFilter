import gmail_filter as filter
from tkinter import *
from tkinter import ttk

class FilterGUI:

    def __init__(self):

        root = Tk()
        root.title("Email Filter")
        root.configure(bg="light gray")
        self.root = root

        Label(root, text="Spam Emails:", bg="light gray").grid(row=1, column=1)
        ttk.Separator(root).grid(row=2, column=1, sticky="ew")

        display = Frame(root, width=600, height=400, bg="light gray")
        display.grid(row=3, column=1)
        self.display = display

        panel = Frame(root, width=600, height=200)
        panel.grid(row=4, column=1)
        self.panel = panel

        spam_input = Entry(panel, width=70)
        spam_input.grid(row=1, column=1)
        self.spam_input = spam_input

        Button(panel, text="Add Email to spam", width=23, bg="gray", command=self.take_input).grid(row=1, column=2)
        Button(panel, text="Filter my inbox", width=60, bg="#bd952a", command=self.main).grid(row=2, column=1)
        Button(panel, text="Clear given Emails", bg="#b02727", fg="white", width=23, command=self.wipe_file).grid(row=2, column=2)
        Button(root, text="NUKE! (not recommended)", bg="red", fg="white", width=84, command=self.nuke).grid(row=5, column=1)


    def update_display(self):

        with open("emails.txt", "r") as emails:

            y_pos = 0

            for line in emails.readlines():
                
                text = Label(self.display, text=line, fg="black", bg="light gray")
                text.place(x=0, y=y_pos)

                y_pos += 20


    def take_input(self):

        if self.spam_input.get() != "":

            text = self.spam_input.get().strip()

            with open("emails.txt", "a") as emails:
                emails.write(text + "\n")

            with open("emails.txt", "r") as emails:   

                length = len(emails.readlines())

                if length > 20:
                
                    overflow = length - 20
                    
                    self.display.destroy()
                    display = Frame(self.root, width=600, height=400 + (overflow * 20), bg="light gray")
                    display.grid(row=3, column=1)

                    self.display = display
                
            self.spam_input.delete(0, "end")
            self.update_display()


    def wipe_file(self):
        
        with open("emails.txt", "w") as emails:
            pass

        self.display.destroy()

        display = Frame(self.root, width=600, height=400, bg="light gray")
        display.grid(row=3, column=1)
        self.display = display


    def nuke(self):

        self.root.destroy()
        filter.nukeFunc()


    def main(self):

        spam_emails = []
        with open("emails.txt", "r") as emails:

            for line in emails.readlines():
                spam_emails.append(f"<{line[:-1]}>")

        my_filter = filter.Filter(spam_emails)

        self.root.destroy()
        my_filter.mainFunc()


if __name__ == "__main__":

    filter.connectFunc()

    app = FilterGUI()
    app.update_display()
    app.root.mainloop()
