import json

class FinancialConstants:
    def __init__(self):
        self.pension_brackets: dict = {}
        self.pension_brackets_length: int = 0
        self.rent_brackets: dict = {}
        self.rent_brackets_length: int = 0
        self.pension_brackets, self.rent_brackets = self.get_tax_brackets()

    def get_constants(self):
        pass

    def get_tax_brackets(self, file: str = "backend/financialConstants.json"):
        pension_brackets: dict = {}
        rent_brackets: dict = {}
        with open(file, "r") as constants:
            tax_constants: dict = json.load(constants)

        self.pension_brackets_length = tax_constants["pension_data"]["brackets_length"]
        self.rent_brackets_length = tax_constants["rent_data"]["brackets_length"]

        self.pension_brackets = self.parse_brackets_from_json("pension_data", tax_constants)
        self.rent_brackets = self.parse_brackets_from_json("rent_data", tax_constants)

        return self.convert_bracket_values_to_dict(self.pension_brackets), self.convert_bracket_values_to_dict(self.rent_brackets)

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

    def convert_bracket_values_to_dict(self, tax_brackets: dict):
        bracket_dict: dict = {}
        for bracket_index, bracket_content in tax_brackets.items():

            bracket_dict.update({bracket_index: bracket_content})
        return bracket_dict


if __name__ == "__main__":
    c1 = FinancialConstants()

    def print_dict_conversion(for_=False):
        var1, var2 = c1.get_tax_brackets()
        if for_ is False:
            print(c1.convert_bracket_values_to_dict(var1))
            print(c1.convert_bracket_values_to_dict(var2))
            return None
        for i, j in var1.items():
            print(f"{i}: {j}")
        print("---------------------------")
        for i, j in var2.items():
            print(f"{i}: {j}")

    def print_brackets_length():
        print(f"Pension: {c1.pension_brackets_length}")
        print(f"Rent: {c1.rent_brackets_length}")

    print_dict_conversion(for_=True)
    print_brackets_length()
