# # Age Calculator

## Project Description
This is a simple Python project that calculates a user's age based on their birth year. The program asks the user to input their birth year, then calculates their age by subtracting it from the current year. The final result is printed to the screen.

## How to Run
1. Make sure you have Python 3 installed on your system.  
2. Open your terminal or command prompt.  
3. Navigate to the directory where the `age_calculator.py` file is located.  
4. Run the following command:
   ```bash
   python age_calculator.py
   ```
5. When prompted, enter your birth year (e.g., `2000`), and the program will return your age.

## Example Usage
```bash
python age_calculator.py
Enter your birth year: 1990
Your age is: 35 years old
```

## Technical Notes
- The script uses Python's built-in `datetime` module to get the current year automatically.
- The user input is converted from string to integer using the `int()` function.
- The age is calculated by subtracting the birth year from the current year.
- If the user enters non-numeric input, an error may occur — input validation can be added in future versions.
