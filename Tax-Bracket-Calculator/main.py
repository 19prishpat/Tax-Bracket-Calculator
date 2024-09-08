
def find_tax_bracket(salary):
    """
    Calculates the tax bracket that you are in.


    Args:
        salary (int): Salary that the user has


    Returns:
        int: the bracket number that the user is in
    """
    if salary < 0:
        return -1
    elif salary <= 53359:
        return 1
    elif salary <= 106717:
        return 2
    elif salary <= 165430:
        return 3
    elif salary <= 235675:
        return 4
    else:
        return 5

def check_b(income, limit, min, rate, bracket):
    """"""
    if income - limit > 0 and bracket != 5:
        return (limit - min) * rate
    else:
        print(f"Fill in tax bracket {bracket}:", income-min)
        if limit == -1:
            print("Remaining space: infinite")
        else:
            print("Remaining space:", limit - income)
        return (income-min) * rate




def calculate_tax():
    """
    Caculates the Fedral tax you need to pay based on your income.
    Args: None
    Returns: None
    """
    income = float(input("What is your income?: "))
    tax_bracket = find_tax_bracket(income)
    print("you are in tax bracket", tax_bracket)
    tot = 0.0


    # Check if the user is in bracket one or above
    if tax_bracket >= 1:
        tot += check_b(income, 53359, 0, 0.15, 1)


    # Check if the user is in bracket two or above
    if tax_bracket >= 2:
        tot += check_b(income, 106717, 53359, 0.205, 2)


    # Check if the user is in bracket three or above
    if tax_bracket >= 3:
        tot += check_b(income, 165430, 106717, 0.26, 3)


    # Check if the user is in bracket four or above
    if tax_bracket >= 4:
        tot += check_b(income, 235675, 165430, 0.29, 4)


    # Check if the user is in the fifth bracket
    if tax_bracket == 5:
        tot += check_b(income, -1, 235675, 0.33, 5)


    print(F"you have to pay ${tot} dollars")

calculate_tax()











