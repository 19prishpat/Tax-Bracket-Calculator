# Tax Bracket Calculator

## Overview
This Python project calculates the federal tax a user needs to pay based on their income. The program determines the user's tax bracket and calculates the total federal tax accordingly.

## Functions

### `find_tax_bracket(salary)`
- **Purpose**: Determines the tax bracket based on the user's salary.
- **Args**: 
  - `salary` (int): The user's salary.
- **Returns**: 
  - An integer representing the tax bracket (1 to 5).

### `check_b(income, limit, min, rate, bracket)`
- **Purpose**: Calculates the tax for a specific tax bracket.
- **Args**:
  - `income` (float): The user's total income.
  - `limit` (float): The upper limit of the tax bracket.
  - `min` (float): The lower limit of the tax bracket.
  - `rate` (float): The tax rate for the bracket.
  - `bracket` (int): The tax bracket number.
- **Returns**: 
  - The amount of tax for the given bracket.

### `calculate_tax()`
- **Purpose**: Main function that calculates the total federal tax based on the user's income.
- **Args**: 
  - None (input is taken directly from the user).
- **Returns**: 
  - None (prints the tax amount to be paid).

## How It Works
1. The user is prompted to input their income.
2. The program calculates which tax bracket the user belongs to using the `find_tax_bracket()` function.
3. The tax is calculated incrementally by applying different rates for each tax bracket, based on the user’s income.
4. The total tax is displayed at the end.


