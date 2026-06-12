# Insurance Management System

A Python-based console application designed to streamline the management of insurance policies and client data. This project served as a comprehensive final exam milestone, demonstrating practical knowledge of Object-Oriented Programming (OOP) and software design best practices.

## 🚀 Features
* **Client & Policy Management:** Full CRUD capabilities to create, retrieve, update, and manage insurance records.
* **Data Validation:** Built-in mechanisms to ensure user inputs (names, phone numbers, policy details) are formatted correctly before processing.
* **Interactive CLI:** An intuitive, user-friendly command-line interface for seamless navigation.

## 🛠️ Software Engineering Principles Applied

### Object-Oriented Programming (OOP)
* Implemented clean data models utilizing classes, encapsulation, and clear object relationships (e.g., linking specific insurance policies directly to client objects).

### Single Responsibility Principle (SRP)
The system is divided into independent layers to maximize code maintainability and scalability:
* **Models:** Pure data structures representing clients and insurance policies.
* **Business Logic / Repository:** Handles data storage, filtering, searching, and backend operations.
* **App / UI Layer:** Manages the console loop, user inputs, and visual output formatting.

### Don't Repeat Yourself (DRY)
* Input validation rules and formatting utilities are centralized into reusable helper functions, eliminating code duplication across the application.

## 📦 Tech Stack
* **Language:** Python 3
* **Core Concepts:** Object-Oriented Programming, Data Collections, Input Parsing

## 🔧 How to Run
1. Clone the repository:
```bash
   git clone [https://github.com/Petr2411/insurance-management-system.git](https://github.com/Petr2411/insurance-management-system.git)

Run apllication
python main.py
