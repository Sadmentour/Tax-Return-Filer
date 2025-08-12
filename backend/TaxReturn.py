from FinancialConstants import FinancialConstants as fc
from utils.conversions import *
from math import floor

class TaxReturn:
    def __init__(self):
        self.income: float = 0.0
        self.income_increase: float = 0.0
        self.income_details: dict = {}
        self.financial_constants: fc = fc() # Explicitly set the 'file' parameter if file isn't found
                                            # File Name: "financialConstants.json"
        self.financial_constants.init_constants

    def calculate_income_tax(self, monthly_income: float, income_type: str):
        """
        Calculates the tax based on taxing brackets and the stamp duty precent

        For now, income types only include
        'pension' and 'rent'
        """
        bracket: int = 1
        taxed_precent: float = 0.0
        stamp_duty: float = 0.0
        year_payment_whole: float = 0.0
        annual_income = monthly_to_yearly(monthly_income)
        precent_temp = self.choose_bracket(income=annual_income,
            bracket_dict=eval(f"self.financial_constants.{income_type}_brackets"),
            brackets_length=eval(f"self.financial_constants.{income_type}_brackets_length")
        )

        taxed_precent = precent_temp
        stamp_duty = self.calculate_stamp(f"{income_type}_data", self.financial_constants.constants)
        taxed_precent = make_precent(taxed_precent)
        print(self.financial_constants.constants["pension_data"]["stamp_duty"])

        if stamp_duty:
            stamp_duty = make_precent(stamp_duty)
            year_payment_whole = (annual_income * taxed_precent) + (annual_income * stamp_duty)
        year_payment_whole = (annual_income * taxed_precent)
        return round(year_payment_whole, ndigits=3)
        
    @staticmethod
    def choose_bracket(income: float, bracket_dict: dict, brackets_length: int) -> float:
        for n in range(brackets_length):
            n = str(n + 1)
            bracket = bracket_dict[n]

            if       income == 0:                          raise ValueError("Income cannot be zero.")
            elif bracket[1] == "Infinity":                 return bracket[2]
            elif bracket[0] <= floor(income) < bracket[1]: return bracket[2]
            
    def calculate_stamp(self, constants_field: str, constants_dict: dict):
        stamp: float = constants_dict[constants_field]["stamp_duty"]
        return stamp if stamp != 0 else None

if __name__ == "__main__":
    tr = TaxReturn()
    payment = tr.calculate_income_tax(5_607_33, "pension")
    print(f"${payment:,.2f}")