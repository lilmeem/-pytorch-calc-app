"""
torch_calculator.py
A simple calculator app with a GUI using Tkinter and PyTorch tensors.
"""

import tkinter as tk
from tkinter import messagebox
import torch


class TorchCalculator:
    def __init__(self, master):
        self.master = master
        master.title("PyTorch Calculator")

        # Input fields
        self.label1 = tk.Label(master, text="Number 1:")
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        self.label2 = tk.Label(master, text="Number 2:")
        self.label2.grid(row=1, column=0, padx=5, pady=5)

        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # Result display
        self.result_label = tk.Label(master, text="Result: ")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Buttons
        self.add_button = tk.Button(master, text="Add", command=self.add)
        self.add_button.grid(row=3, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(master, text="Subtract", command=self.subtract)
        self.subtract_button.grid(row=3, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(master, text="Multiply", command=self.multiply)
        self.multiply_button.grid(row=4, column=0, padx=5, pady=5)

        self.divide_button = tk.Button(master, text="Divide", command=self.divide)
        self.divide_button.grid(row=4, column=1, padx=5, pady=5)

    def get_inputs(self):
        """Retrieve inputs as PyTorch tensors."""
        try:
            num1 = torch.tensor(float(self.entry1.get()))
            num2 = torch.tensor(float(self.entry2.get()))
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = torch.add(num1, num2)
            self.result_label.config(text=f"Result: {result.item()}")

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = torch.sub(num1, num2)
            self.result_label.config(text=f"Result: {result.item()}")

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            result = torch.mul(num1, num2)
            self.result_label.config(text=f"Result: {result.item()}")

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Math error", "Cannot divide by zero.")
                return
            result = torch.div(num1, num2)
            self.result_label.config(text=f"Result: {result.item()}")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = TorchCalculator(root)
    root.mainloop()
