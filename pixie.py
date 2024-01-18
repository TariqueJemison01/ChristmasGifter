import tkinter as tk
from tkinter import messagebox
import random

class ChristmasGiftApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Christmas Gift App")

        self.label = tk.Label(root, text="Enter Family Members' Names (comma-separated):", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.names_entry = tk.Entry(root, width=40)
        self.names_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Gift Pairings", command=self.generate_gift_pairings)
        self.generate_button.pack(pady=10)

        self.refresh_button = tk.Button(root, text="Refresh Pairings", command=self.refresh_pairings)
        self.refresh_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

        self.pairings_text = tk.Text(root, height=10, width=40)
        self.pairings_text.pack(pady=10)

    def generate_gift_pairings(self):
        family_members = self.names_entry.get().split(',')
        family_members = [name.strip() for name in family_members if name.strip()]

        if len(family_members) < 2:
            messagebox.showwarning("Input Error", "Please enter at least two family members.")
            return

        gift_pairs = self.generate_gift_pairs(family_members)
        self.display_gift_pairings(gift_pairs)

    def generate_gift_pairs(self, people):
        pairs = []
        remaining_recipients = list(people)

        for person in people:
            recipient = random.choice(remaining_recipients)
            while recipient == person:
                recipient = random.choice(remaining_recipients)

            pairs.append((person, recipient))
            remaining_recipients.remove(recipient)

        return pairs

    def display_gift_pairings(self, pairs):
        pairings_text = "\n".join([f"{pair[0]} buys a gift for {pair[1]}" for pair in pairs])
        self.pairings_text.delete(1.0, tk.END)
        self.pairings_text.insert(tk.END, pairings_text)

    def refresh_pairings(self):
        self.generate_gift_pairings()

    def reset(self):
        self.names_entry.delete(0, tk.END)
        self.pairings_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChristmasGiftApp(root)
    root.mainloop()
