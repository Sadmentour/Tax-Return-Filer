import json

class FinancialConstants:
    """Explicitly set the 'file' parameter File Name: 'financialConstants.json'"""
    def __init__(self, file: str = "jsons/financialConstants.json"):
        self.file: str = file
        self.wage_brackets: dict = {}
        self.wage_brackets_length: int = 0
        self.wage_stamp_duty: float = 0
        self.rent_brackets: dict = {}
        self.rent_brackets_length: int = 0
        self.rent_stamp_duty: float = 0
        self.constants: dict = {}
        self.init_constants()
        # self.wage_brackets, self.rent_brackets = self.get_tax_brackets(self.constants)

    def init_constants(self):
        with open(self.file, "r") as constants:
            self.constants: dict = json.load(constants)
        self.get_tax_brackets(self.constants)

        self.wage_stamp_duty = self.get_stamp_duty("wage_data", self.constants)
        self.rent_stamp_duty = self.get_stamp_duty("rent_data", self.constants)

    def get_tax_brackets(self, constants: dict):
        self.wage_brackets_length = constants["wage_data"]["brackets_length"]
        self.rent_brackets_length = constants["rent_data"]["brackets_length"]

        self.wage_brackets = self.parse_brackets_from_json("wage_data", constants)
        self.rent_brackets = self.parse_brackets_from_json("rent_data", constants)

        return self.convert_bracket_values_to_dict(self.wage_brackets), self.convert_bracket_values_to_dict(self.rent_brackets)

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
