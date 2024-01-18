import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import random

class ChristmasGiftApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Christmas Gift App")

        self.label = QLabel("Enter Family Members' Names (comma-separated):", self)
        self.names_entry = QLineEdit(self)
        self.generate_button = QPushButton("Generate Gift Pairings", self)
        self.refresh_button = QPushButton("Refresh Pairings", self)
        self.reset_button = QPushButton("Reset", self)
        self.pairings_text = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.names_entry)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.pairings_text)

        self.setLayout(layout)

        self.generate_button.clicked.connect(self.generate_gift_pairings)
        self.refresh_button.clicked.connect(self.refresh_pairings)
        self.reset_button.clicked.connect(self.reset)

    def generate_gift_pairings(self):
        family_members = self.names_entry.text().split(',')
        family_members = [name.strip() for name in family_members if name.strip()]

        if len(family_members) < 2:
            QMessageBox.warning(self, "Input Error", "Please enter at least two family members.")
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
        self.pairings_text.setPlainText(pairings_text)

    def refresh_pairings(self):
        self.generate_gift_pairings()

    def reset(self):
        self.names_entry.clear()
        self.pairings_text.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChristmasGiftApp()
    window.show()
    sys.exit(app.exec_())
