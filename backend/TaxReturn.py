from utils.conversions import *

class TaxReturn:
    def __init__(self):
        self.income: float = 0.0
        self.income_increase: float = 0.0
        self.income_details: dict = {}
    
    def calculate_tax(self, monthly_income, tax_brackets, stamp_duty):
        final_result: float = 0.0
        """
        Tax formula:
        """
        annual_income = monthly_to_yearly(monthly_income)
        final_result = ...