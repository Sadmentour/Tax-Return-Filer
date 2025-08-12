import ttkbootstrap as tbs
from data.global_constants import *

INCOME_TAX: str = "income-tax"


class InputForm:
    def __init__(self, master: tbs.Window, input_type: str = "income-tax", income_prefix: str = "Monthly"):
        self.master: tbs.Window = master
        self.type: str = input_type
        self.income_prefix: str = income_prefix

    def select_type(self):
        if self.type == INCOME_TAX:
            pass
        else:
            raise ValueError(f"Invalid <input_type> entry: \"{self.type}\".")

    def init_income_tax_widgets(self):
        self.containter_frame: FRM = tbs.Frame(self.master)

        self.pension_label: LBL = tbs.Label(self.containter_frame, text=f"{self.income_prefix} Pension Income")
        self.pension_entry: ENT = tbs.Entry(self.containter_frame)

        self.rent_label: LBL = tbs.Label(self.containter_frame, text=f"{self.income_prefix} Rent Income")
        self.rent_entry: ENT = tbs.Entry(self.containter_frame)

        self.submit_button: BTN = tbs.Button(self.containter_frame)


if __name__ == "__main__":
    w = tbs.Window()
    e = tbs.Entry(w, show="Hello, world!")
    e.pack()
    w.mainloop()
