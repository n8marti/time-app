import sys
from datetime import datetime
from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk


class App:
    def __init__(self):
        self.title_text = "Get the time"
        self.ask_time_text = "Get current time?"

    def ask_time(self):
        """Placeholder for API implemented by CLI/GUI subclass"""
        raise NotImplementedError

    def get_time(self):
        """Placeholder for API implemented by CLI/GUI subclass"""
        raise NotImplementedError

    def run(self):
        """Placeholder for API implemented by CLI/GUI subclass"""
        raise NotImplementedError

    def _get_time(self):
        """UI-agnostic method for retrieving the current time."""
        return datetime.now().time().strftime('%I:%M:%S %p')


class CLI(App):
    def __init__(self):
        super().__init__()
        print(self.title_text)
    
    def ask_time(self):
        """Implementation of asking the user if they want to get the current time"""
        answer = input(f"{self.ask_time_text} [Y/n]: ")
        if answer == '' or answer.lower() == 'y':
            return True
        return False

    def get_time(self):
        """Implementation of displaying the current time"""
        print(self._get_time())

    def run(self):
        """Run app in a loop to mimic GUI flow."""
        try:
            while True:
                if self.ask_time():
                    self.get_time()
        except KeyboardInterrupt:
            print()
            sys.exit()

class GUI(App):
    def __init__(self):
        super().__init__()
        # Define widgets.
        self.root = Tk()
        self.root.title(self.title_text)
        self.label = ttk.Label(self.root, text=self.ask_time_text)
        self.button = ttk.Button(self.root, text="OK", command=self.get_time)
        self.time_var = StringVar()
        self.time = ttk.Label(self.root, textvariable=self.time_var)
        # Arrange widgets in root window.
        for w in self.root.winfo_children():
            w.pack()
    
    def ask_time(self):
        """Implementation not needed since it's incorporated into the GUI window"""
        pass

    def get_time(self):
        self.time_var.set(self._get_time())

    def run(self):
        """Run the app."""
        self.root.mainloop()


class IncompleteUI(App):
    pass


if __name__ == '__main__':
    # Determine UI type from command line.
    if len(sys.argv) > 1:
        if 'cli' in sys.argv:
            app = CLI()
        else:
            app = IncompleteUI()
    else:
        app = GUI()

    # Run app.
    app.run()
