import tkinter as tk
from tkinter import messagebox
import random

# Praise & critique lists
praise = [
    "Nice dirt pile you've got there.",
    "That's a fine heap of soil!",
    "Impressive mound, friend.",
    "The envy of all gardeners.",
    "Truly majestic dirt.",
]

critique = [
    "This dirt pile is lacking in volume.",
    "I expected more from such a prominent gardener.",
    "This mound could use some serious work.",
    "Not the best dirt I've seen.",
    "I've seen better piles at the compost heap.",
]

# App logic
class DirtCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dirt Checker")
        self.amount = None
        self.has_started = False

        # Entry for dirt amount
        self.label = tk.Label(root, text="How much dirt is in the pile?")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit", command=self.check_amount)
        self.button.pack(pady=5)

    def check_amount(self):
        try:
            amount = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        self.amount = amount

        if not self.has_started:  # First check
            if self.amount > 22:
                messagebox.showinfo("Result", "You have passed the check. Proceeding...")
                self.label.config(text="Has the dirt amount changed? (yes=type 1 / no=type 0)")
                self.entry.delete(0, tk.END)
                self.has_started = True
            else:
                messagebox.showwarning("Result", "Not enough dirt to start! Grow a bigger pile.")
                self.root.quit()
        else:  # After start
            if self.amount == 1:  # yes
                self.label.config(text="How much dirt is in the pile now?")
                self.button.config(command=self.update_amount)
                self.entry.delete(0, tk.END)
            elif self.amount == 0:  # no
                messagebox.showinfo("Result", "Awesome. You still have enough dirt!")
            else:
                messagebox.showerror("Error", "Please type 1 for yes or 0 for no.")

    def update_amount(self):
        try:
            self.amount = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        while self.amount < 22:
            messagebox.showwarning("Critique", random.choice(critique))
            self.entry.delete(0, tk.END)
            return  # Wait for user to type again

        messagebox.showinfo("Praise", random.choice(praise))
        self.label.config(text="Has the dirt amount changed? (yes=type 1 / no=type 0)")
        self.entry.delete(0, tk.END)
        self.button.config(command=self.check_amount)

# Create window
root = tk.Tk()
app = DirtCheckerApp(root)
root.mainloop()
