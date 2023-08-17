#/bin/python3

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI Calculator")
        
        self.result_var = tk.StringVar()
        
        self.create_ui()
    
    def create_ui(self):
        # Entry widget to display the current expression/result
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20))
        entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons for digits and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            # ('Clear', 5, 0),  
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
    
    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif value == 'Clear':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            if current_text == "Error":
                current_text = ""
            self.result_var.set(current_text + value)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
