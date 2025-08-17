def monthly_to_yearly(income: float):
    MONTHS_IN_A_YEAR: int = 12
    return income * MONTHS_IN_A_YEAR

def yearly_to_monthly(income: float):
    MONTHS_IN_A_YEAR: int = 12
    return income / MONTHS_IN_A_YEAR

def make_precent(number: float, precent: float = 100.0, digit_resolution: int = 6):
    """
    Takes a number from 0 to 100 and
    divides it by a number to make it
    a precentage coefficient

    *(Default is 100)*
    """
    if number != 0:
        return round(number / precent, digit_resolution) if precent != 0 else None
    return None

def currency_string(amount: float, currency_symbol: str, digits: int = 2):
    return f"{currency_symbol}{amount:,.{digits}f}"

"""
if __name__ == "__main__":
    c1 = currency_string(1002.4335, "$")
    print(c1)
"""
