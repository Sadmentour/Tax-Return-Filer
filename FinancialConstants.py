import json

class FinancialConstants:
    def __init__(self):
        self.pension_brackets: list[float] = []
        self.rent_brackets: list[float] = []

    def get_constants(self):
        pass

    def get_tax_brackets(self, file: str = "financialConstants.json"):
        pension_brackets: list = []
        rent_brackets: list = []
        with open(file, "r") as brackets:
            tax_brackets: dict = json.load(brackets)
        self.pension_brackets = self.parse_brackets_from_json("pension_data", tax_brackets)
        self.rent_brackets = self.parse_brackets_from_json("rent_data", tax_brackets)
        return self.pension_brackets, self.rent_brackets

    @staticmethod
    def parse_brackets_from_json(data_field: str, constants_object: dict):
        brackets: list = []
        for bracket in constants_object[data_field]["brackets"].items():
            brackets.append(bracket)
        return brackets


if __name__ == "__main__":
    c1 = FinancialConstants()
    var1, var2 = c1.get_tax_brackets()
    for i, l in var1, var2:
        for j, k in i, l:
            print(j)
