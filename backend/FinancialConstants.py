import json

class FinancialConstants:
    def __init__(self):
        self.pension_brackets: dict = {}
        self.rent_brackets: dict = {}
        self.pension_brackets, self.rent_brackets = self.get_tax_brackets()

    def get_constants(self):
        pass

    def get_tax_brackets(self, file: str = "financialConstants.json"):
        pension_brackets: dict = {}
        rent_brackets: dict = {}
        with open(file, "r") as constants:
            tax_constants: dict = json.load(constants)
        self.pension_brackets = self.parse_brackets_from_json("pension_data", tax_constants)
        self.rent_brackets = self.parse_brackets_from_json("rent_data", tax_constants)

        return self.parse_bracket_values(self.pension_brackets), self.parse_bracket_values(self.pension_brackets)

    @staticmethod
    def parse_brackets_from_json(data_field: str, constants_object: dict):
        brackets: dict = {}
        for bracket in constants_object[data_field]["brackets"].items():
            brackets.update({bracket[0]: bracket[1]})
        return brackets

    def calculate_tax(self, monthly_income, tax_brackets, stamp_duty):
        final_result: float = 0.0
        """
        Tax formula:

        """
        annual_income = self.monthly_to_yearly(monthly_income)
        final_result = ...

    def parse_bracket_values(self, tax_brackets: dict):
        bracket_dict: dict = {}
        for bracket_index, bracket_content in tax_brackets.items():

            bracket_dict.update({bracket_index: bracket_content})
        return bracket_dict

    @staticmethod
    def monthly_to_yearly(income: float):
        MONTHS_IN_A_YEAR: int = 12
        return income * MONTHS_IN_A_YEAR


if __name__ == "__main__":
    c1 = FinancialConstants()
    var1, var2 = c1.get_tax_brackets()
    # for i in c1.parse_bracket_values(var1):
    #     print(i)
    print(c1.parse_bracket_values(var1))
