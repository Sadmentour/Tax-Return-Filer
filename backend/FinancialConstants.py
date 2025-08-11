from utils.conversions import monthly_to_yearly
import json

class FinancialConstants:
    def __init__(self, file: str = "backend/financialConstants.json"):
        self.pension_brackets: dict = {}
        self.pension_brackets_length: int = 0
        self.pension_stamp_duty: float = 0
        self.rent_brackets: dict = {}
        self.rent_brackets_length: int = 0
        self.constants: dict = {}
        with open(file, "r") as constants:
            self.constants: dict = json.load(constants)
        self.pension_brackets, self.rent_brackets = self.get_tax_brackets(self.constants)

    def init_constants(self):
        self.get_tax_brackets(self.constants)

        self.pension_stamp_duty = self.get_stamp_duty("pension_data", self.constants)
        self.rent_stamp_duty = self.get_stamp_duty("rent_data", self.constants)

    def get_tax_brackets(self, constants: dict):
        pension_brackets: dict = {}
        rent_brackets: dict = {}

        self.pension_brackets_length = constants["pension_data"]["brackets_length"]
        self.rent_brackets_length = constants["rent_data"]["brackets_length"]

        self.pension_brackets = self.parse_brackets_from_json("pension_data", constants)
        self.rent_brackets = self.parse_brackets_from_json("rent_data", constants)

        return self.convert_bracket_values_to_dict(self.pension_brackets), self.convert_bracket_values_to_dict(self.rent_brackets)

    def get_stamp_duty(self, data_field: str, constants_object: dict):
        stamp_duty: float = constants_object[data_field]["stamp_duty"]
        if stamp_duty == 0:
            return None
        return stamp_duty

    @staticmethod
    def parse_brackets_from_json(data_field: str, constants_object: dict):
        brackets: dict = {}
        for bracket in constants_object[data_field]["brackets"].items():
            brackets.update({bracket[0]: bracket[1]})
        return brackets

    def convert_bracket_values_to_dict(self, tax_brackets: dict):
        bracket_dict: dict = {}
        for bracket_index, bracket_content in tax_brackets.items():

            bracket_dict.update({bracket_index: bracket_content})
        return bracket_dict


if __name__ == "__main__":
    c1 = FinancialConstants()

    def print_dict_conversion(for_=False):
        var1, var2 = c1.get_tax_brackets(c1.constants)
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


    c1.init_constants()
    print(c1.pension_stamp_duty)
    print(c1.rent_stamp_duty)
    print(c1.pension_brackets_length)
    print(c1.pension_brackets)
    print(c1.rent_brackets_length)
    print(c1.rent_brackets)
