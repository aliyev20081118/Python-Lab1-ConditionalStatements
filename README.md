# Python Programming - Laboratory Assignment 1

**Course:** Introduction to Python Programming

**Institution:** Karabakh University

**Faculty:**  Mathematics & IT

**Student:** İbrahim Əliyev

**Group:** KOM26

**Instructor:** Shamil Humbatov

## 📌 Overview

This repository contains the solution for **Laboratory Assignment 1** in the *Introduction to Python Programming* course. The focus of this assignment is on using conditional statements (`if`, `elif`, `else`), logical operators, modulo operations, and basic repetition loops (`while`) to build simple interactive command-line applications.

## 📂 Project Structure & Program Descriptions

The project consists of three main Python scripts:

### 1. Body Mass Index (BMI) Calculator (`BMI Calculator.py`)

* **Objective:** Calculates the user's BMI based on weight and height, then categorizes the health status.

* **How it works:**

  * Prompts the user for weight (in kilograms) and height (in meters).

  * Computes BMI using the formula:

    $$
   BMI=weight/height**2
    $$

  * Determines the BMI category:

    * **Underweight:** $< 18.5$

    * **Normal Weight:** $18.5 \le BMI < 25.0$

    * **Overweight:** $25.0 \le BMI < 30.0$

    * **Obese:** $\ge 30.0$

  * Includes a loop (`while a == 'y'`) allowing the user to perform multiple calculations.

### 2. Chinese Zodiac Calculator (`Chinese Zodiac Calculator.py`)

* **Objective:** Identifies the user's Chinese Zodiac sign based on their birth year.

* **How it works:**

  * Asks the user to enter a valid birth year between 1900 and 2026.

  * Calculates the remainder of the birth year divided by 12 (`year % 12`).

  * Maps the remainder index to the corresponding zodiac animal:

    * `0`: Monkey, `1`: Rooster, `2`: Dog, `3`: Pig, `4`: Rat, `5`: Ox, `6`: Tiger, `7`: Rabbit, `8`: Dragon, `9`: Snake, `10`: Horse, `11`: Sheep.

  * Prompts the user to re-run the calculation if desired.

### 3. Birthday Guessing Game (`Birthday Guessing Game.py`)

* **Objective:** Guesses the exact day of the month a user was born without directly asking for the number.

* **How it works:**

  * Displays 5 sets of numbers representing binary powers ($2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16$).

  * Prompts the user to enter `1` (Yes) or `0` (No) for each set based on whether their birth day is present in that set.

  * Adds up the base values ($1, 2, 4, 8, 16$) of each set where the user responds with `1`.

  * Outputs the calculated birth day and offers a replay option.

## 🚀 How to Run the Scripts

Ensure you have Python installed on your system. Run any of the individual files in your terminal:

```
python "BMI Calculator.py"
python "Chinese Zodiac Calculator.py"
python "Birthday Guessing Game.py"

```

## 🛠 Features & Concepts Demonstrated

* **Control Flow:** `if`, `elif`, `else` conditional logic.

* **Data Structures:** Python `list` index lookup.

* **Loops:** Interactive `while` loops for repeating program executions.

* **User Input & Formatting:** String formatting (`f-strings`) and data casting (`int()`, `float()`).