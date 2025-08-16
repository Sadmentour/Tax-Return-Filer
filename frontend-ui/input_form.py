import ttkbootstrap as tbs
from widget_constants import *

class InputForm:
    def __init__(self, master: tbs.Window, input_type: str = FRAMED_ENTRIES, income_prefix: str = "Monthly"):
        self.master: tbs.Window = master
        self.type: str = input_type
        self.income_prefix: str = income_prefix
        self.has_initialized: bool = False
        self.select_type()

    def select_type(self):
        """
        Every time this method is changed or appended,
        the following methods might need updating:

        * forget_all_widgets()

        Update them according to docstrings
        """
        if self.has_initialized:
            self.forget_all_widgets()
        if self.type == FRAMED_ENTRIES:
            self.init_framed_entries_widgets()
        else:
            raise ValueError(f"Invalid <input_type> entry: \"{self.type}\".")
        self.has_initialized = True

    def forget_all_widgets(self):
        """
        Update by adding destroy() for every
        top-level (parent frame, etc...) of each initialization
        type
        """
        self.containter_frame.destroy()

    def init_framed_entries_widgets(self):
        self.containter_frame: FRM = tbs.Frame(self.master)

        self.monthly_labelframe: LBF = tbs.Labelframe(self.containter_frame, text="Monthly", labelanchor="n")

        self.wage_labelframe: LBF = tbs.Labelframe(self.monthly_labelframe, text="Wage", labelanchor="s", border=0)
        self.pension_labelframe: LBF = tbs.Labelframe(self.monthly_labelframe, text="Pension", labelanchor="s", border=0)
        self.rent_labelframe: LBF = tbs.Labelframe(self.monthly_labelframe, text="Rent", labelanchor="s", border=0)

        self.wage_entry: LBF = tbs.Entry(self.wage_labelframe, width=15)
        self.pension_entry: ENT = tbs.Entry(self.pension_labelframe, width=15)
        self.rent_entry: ENT = tbs.Entry(self.rent_labelframe, width=15)

    def place_framed_entries_widgets(self, widget_margin_xy: float):
        self.containter_frame.pack(padx=5, anchor="center", expand=True)

        self.monthly_labelframe.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)

        self.wage_labelframe.grid(row=0, column=0, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.pension_labelframe.grid(row=0, column=1, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.rent_labelframe.grid(row=0, column=2, padx=widget_margin_xy+1, pady=widget_margin_xy)

        self.wage_entry.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.pension_entry.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)
        self.rent_entry.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)


if __name__ == "__main__":
    print(f"input_form.py: {__name__}")
    w = tbs.Window(themename="superhero")
    inp = InputForm(w)
    inp.place_framed_entries_widgets(0, 0, 2, 1)
    w.mainloop()
