import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Password Generator")

        self.name_label = tk.Label(root, text="Name:", width=20, height=1)
        self.name_label.pack()

        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.pack()

        self.length_label = tk.Label(root, text="Enter Password Length:", width=20, height=1)
        self.length_label.pack()

        self.length_entry = tk.Entry(root, width=20)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Your Password", command=self.generate_password, width=20)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="", width=20, height=1)
        self.password_label.pack()

    def generate_password(self):
        name = self.name_entry.get()
        password_length = int(self.length_entry.get())
        if password_length <= 0:
            self.password_label.config(text="Length Is Invalid Try Again !")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        random_part = ''.join(random.choice(characters) for _ in range(password_length - len(name)))
        generated_password = name + random_part
        self.password_label.config(text=generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
