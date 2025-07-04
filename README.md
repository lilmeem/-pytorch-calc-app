# PyTorch Calculator with GUI

This project is a simple calculator application built in Python using:

**Tkinter** for the graphical user interface (GUI)  
**PyTorch** tensors to perform the arithmetic operations

While using PyTorch for basic calculator functionality is not necessary from a performance standpoint, this project demonstrates how to integrate PyTorch into a Python GUI application. It also serves as an educational example of how tensor operations can replace native Python math for experimentation or learning purposes.

---

## Features

- Addition, subtraction, multiplication, and division of two numbers
- Input validation with error messages
- Results displayed in real time
- Simple, clean interface built with Tkinter
- PyTorch tensor operations under the hood (`torch.add`, `torch.mul`, etc.)

---

## Why Use PyTorch for a Calculator?

This project is primarily intended as a **learning tool** and portfolio example rather than as a production calculator. Benefits include:

- **Learning PyTorch API** in a safe, simple context
- Demonstrating integration between a deep learning library and a GUI
- Creating a foundation for more advanced tensor-based features in the future

---

## Potential Extensions and Ideas

If you’d like to make this project more unique or powerful, here are some ideas:

- **Vector and Matrix Operations**
  - Allow users to input lists of numbers and see tensor operations applied.
- **Neural Network Demo Mode**
  - Use a small neural network to process inputs and display outputs.
- **GPU Support Display**
  - Detect whether CUDA is available and show which device PyTorch is using.
- **Tensor Visualization**
  - Show histograms or other visualizations of input and output tensors.
- **Batch Processing**
  - Support applying operations to multiple pairs of numbers at once.

---

## Installation

Make sure you have Python installed. Then install PyTorch:

```bash
pip install torch
