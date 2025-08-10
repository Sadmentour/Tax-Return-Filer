import json

class FinancialConstants:
    def __init__(self):
        self.pension_bracket_length: int = 0
        self.rent_bracket_length: int = 0
        self.pension_brackets: list[float] = []
        self.rent_brackets: list[float] = []

    def get_constants(self):
        pass

    def get_tax_brackets(self, file: str = "brackets.json"):
        with open(file, "r") as brackets:
            tax_brackets: dict = json.load(brackets)
            self.pension_brackets = tax_brackets["pension_brackets"]
            self.rent_brackets = tax_brackets["rent_brackets"]
