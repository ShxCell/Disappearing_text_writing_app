import tkinter as tk
from tkinter import ttk


class DissText(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("Disappearing Text App")
        parent.configure(bg="#faf7c8")
        parent.option_add('*Background', '#faf7c8')
        self.words = 75
        self.count = 10
        self.timer = []

        # Make title
        self.title = tk.Label(text="Don't Stop WRITING!")
        self.title.config(font=("arial", 18, "bold"))
        self.title.pack(pady=10)

        # make subtitle
        self.subtitle = tk.Label(text="Writing all you have. If you stuck, all progress will be lost")
        self.subtitle.config(font=("arial", 11))
        self.subtitle.pack(pady=5)

        # make option
        self.option_label = tk.Label(text="Select how many words:")
        self.option_label.pack()
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar(parent)
        self.selected_option.set(self.words)  # Set default value
        self.selected_option.trace("w", self.on_option_select)

        # Create an option menu
        self.options = [75, 150, 200, 300]
        self.option_menu = tk.OptionMenu(parent, self.selected_option, *self.options)
        self.option_menu.configure(highlightthickness=0, activeforeground="black", activebackground="skyblue")
        self.option_menu.pack()

        # make textbox
        self.user_text = tk.Text(height=12, width=40, font=("arial", 11), wrap=tk.WORD)
        self.user_text.configure(bg="white")
        self.user_text.focus()
        self.user_text.pack(expand=True)
        self.user_text.bind("<KeyRelease>", self.on_key_release)
        self.user_text.bind("<Any-KeyPress>", self.callback)

        # count words remaining
        self.count_word = tk.Label(text=f"Remaining words:{self.words}")
        self.count_word.config(font=("arial", 11), fg="blue")
        self.count_word.pack()

        # make stop warning
        self.stop = tk.Label()
        self.stop.config(font=("arial", 12))
        self.stop.pack()

    def count_down(self, count):
        if count > 0:
            time = self.parent.after(1000, self.count_down, count - 1)
            self.timer.append(time)
            self.word_count()
            if self.words <= 0:
                self.user_text.config(state=tk.DISABLED, bg="light green")
                self.stop.config(text="Great! You have passed idea block!", fg="green")
                for time in self.timer:
                    self.parent.after_cancel(time)

        else:
            self.user_text.delete("1.0", tk.END)
            self.user_text.configure(state=tk.DISABLED, bg="pink")
            self.stop.config(text="Oh no, you stuck! Your progress was lost!", fg="red")

    def word_count(self):
        selected_number = int(self.selected_option.get())
        input_words = self.user_text.get("1.0", tk.END).split(" ")
        self.words = selected_number + 1 - len(input_words)
        if self.words < 0:
            self.words = 0
        self.count_word.config(text=f"Remaining words:{self.words}")

    def on_key_release(self, event):
        self.count_down(self.count)

    def adjust_text_height(self, event):
        # calculate number of lines
        num_lines = int(self.user_text.index('end-1c').split('.')[0])
        # Set the height of the Text widget to the number of lines
        self.user_text.config(height=num_lines)

    def on_option_select(self, *args):
        self.word_count()

    def callback(self, event):
        if True:
            for time in self.timer:
                self.parent.after_cancel(time)


if __name__ == "__main__":
    root = tk.Tk()
    DissText(root).pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    root.mainloop()
