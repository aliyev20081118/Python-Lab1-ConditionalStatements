# Python Programming - Laboratory Assignment 1
**Course:** Introduction to Python Programming 
**Institution:** Karabakh University
**Student:** Ibrahim Aliyev 
**Group:** KOM26 
**Instructor:** Shamil Humbatov


This repository contains my work for **Laboratory Assignment 1** in the *Introduction to Python Programming* course. The goal of this assignment is to practice using conditional statements (`if`, `elif`, `else`) and solve simple real-world problems in Python.

---

## 📂 Task Descriptions

This project includes three main Python applications:

### 1. Body Mass Index (BMI) Calculator
* **What it does:** Calculates the user's BMI based on their weight and height.
* **How it works:**
  * Asks the user to enter weight (in kg) and height (in meters).
  * Calculates BMI using the formula: `BMI = weight / (height * height)`.
  * Checks the BMI value and prints the result: *Underweight*, *Normal Weight*, *Overweight*, or *Obese*.
  * Asks if the user wants to try again using a `while` loop.

### 2. Chinese Zodiac Calculator
* **What it does:** Finds the user's Chinese Zodiac sign based on their birth year.
* **How it works:**
  * Asks the user for their birth year.
  * Uses the remainder operator (`year % 12`) to calculate the index.
  * Displays the corresponding zodiac animal (Rat, Ox, Tiger, Dragon, etc.) from a Python list.

### 3. Birthday Guessing Game
* **What it does:** Guesses the user's birthday (day of the month) without asking directly for the number.
* **How it works:**
  * Shows 5 different sets of numbers to the user.
  * Asks if their birthday is in each set (`1` for Yes, `0` for No).
  * Adds up the starting numbers of the sets (`1, 2, 4, 8, 16`) where the user answered "Yes" to find the exact day.

---

## 🚀 How to Run the Code

Make sure you have Python installed, then run the script using:

```bash
python main.py