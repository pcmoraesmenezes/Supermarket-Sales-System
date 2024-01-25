# Supermarket Sales System

This Python project is an example of an object-oriented design for a supermarket sales system. It covers various concepts of object-oriented programming (OOP), including classes, inheritance, encapsulation, and polymorphism. The system models the interactions between a supermarket, cash registers, sales, and payment methods.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Object-Oriented Concepts](#object-oriented-concepts)
  
## Features

- **Products and Catalog:** Define and manage product descriptions with a product catalog.
- **Sales and Payments:** Create sales, add items, and process payments using various payment methods.
- **Cash Registers:** Simulate multiple cash registers with their sales and catalogs.
- **Calculators:** Implement calculators for both simple and compound interest to calculate payment amounts.
- **Exception Handling:** Handle exceptions, such as nonexistent product descriptions.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/pcmoraesmenezes/Supermarket-Sales-System.git
   ```

2. Run the `main.py` script:

   ```bash
   python supermaket_with_tkinter.py
   ```

3. Explore the simulated supermarket interactions and payments in the console.

## Project Structure

The project is structured into several Python files:

- `supermaket` - Contains the main code, including the supermarket, cash registers, sales, and payment methods.

- `supermaket_with_tkinter` - Contains the main code with a graphical user interface (GUI) built with Tkinter.

## Object-Oriented Concepts

- **Classes and Objects:** Each major entity in the system is represented by a class, and instances of these classes are created during the supermarket interactions.
- **Inheritance:** Payment methods (CardPayment, CheckPayment, CashPayment) inherit from the base Payment class.
- **Encapsulation:** Attributes and methods within classes are encapsulated, providing a clear interface for interactions.
- **Polymorphism:** Different payment methods share a common interface (Payment class), allowing them to be used interchangeably.
