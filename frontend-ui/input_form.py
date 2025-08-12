import ttkbootstrap as tbs
from widget_constants import *

INCOME_TAX: str = "income-tax"


class InputForm:
    def __init__(self, master: tbs.Window, input_type: str = "income-tax", income_prefix: str = "Monthly"):
        self.master: tbs.Window = master
        self.type: str = input_type
        self.income_prefix: str = income_prefix
        self.select_type()

    def select_type(self):
        if self.type == INCOME_TAX:
            self.init_income_tax_widgets()
        else:
            raise ValueError(f"Invalid <input_type> entry: \"{self.type}\".")

    def init_income_tax_widgets(self):
        self.containter_frame: FRM = tbs.Frame(self.master)

        self.pension_labelframe: LBF = tbs.Labelframe(self.containter_frame, text="Pension")
        self.rent_labelframe: LBF = tbs.Labelframe(self.containter_frame, text="Rent")

        self.pension_label: LBL = tbs.Label(self.pension_labelframe, text=f"{self.income_prefix} Pension Income")
        self.pension_entry: ENT = tbs.Entry(self.pension_labelframe)

        self.rent_label: LBL = tbs.Label(self.rent_labelframe, text=f"{self.income_prefix} Rent Income")
        self.rent_entry: ENT = tbs.Entry(self.rent_labelframe)

    def place_income_tax_widgets(self, grid_row: int, grid_column: int, grid_margin_xy: float, widget_margin_xy: float):
        self.containter_frame.grid(row=grid_row, column=grid_column, padx=grid_margin_xy, pady=grid_margin_xy)

        self.pension_labelframe.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.rent_labelframe.grid(row=0, column=1, padx=widget_margin_xy, pady=widget_margin_xy)

        self.pension_label.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.pension_entry.grid(row=1, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.rent_label.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.rent_entry.grid(row=1, column=0, padx=widget_margin_xy, pady=widget_margin_xy)


if __name__ == "__main__":
    print(f"input_form.py: {__name__}")
    w = tbs.Window()
    inp = InputForm(w)
    inp.place_income_tax_widgets(0, 0, 10, 1)
    w.mainloop()
