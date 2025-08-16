import ttkbootstrap as tbs
from widget_constants import *
from utils.conversions import currency_string

class OutputFields:
    def __init__(self, master: tbs.Window, output_type: str = SELECTABLE_LABELS, currency_symbol: str = "€"):
        self.master: tbs.Window = master
        self.type: str = output_type
        self.has_initialized: bool = False
        self.currency_symbol = currency_symbol
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
        if self.type == SELECTABLE_LABELS:
            self.init_selectable_labels_widgets()
        else:
            raise ValueError(f"Invalid <output_type> entry: \"{self.type}\".")
        self.has_initialized = True

    def forget_all_widgets(self):
        """
        Update by adding destroy() for every
        top-level (parent frame, etc...) of each initialization
        type
        """
        self.containter_frame.destroy()

    def init_selectable_labels_widgets(self):
        self.containter_frame: FRM = tbs.Frame(self.master)

        self.yearly_labelframe: LBF = tbs.Labelframe(self.containter_frame, text="Yearly", labelanchor="n", width=60)

        self.wage_labelframe: LBF = tbs.Labelframe(self.yearly_labelframe, text="Wage", labelanchor="s", border=0)
        self.wage_pension_separator: SEP = tbs.Separator(self.yearly_labelframe, orient="vertical")
        self.pension_labelframe: LBF = tbs.Labelframe(self.yearly_labelframe, text="Pension", labelanchor="s", border=0)
        self.pension_rent_separator: SEP = tbs.Separator(self.yearly_labelframe, orient="vertical")
        self.rent_labelframe: LBF = tbs.Labelframe(self.yearly_labelframe, text="Rent", labelanchor="s", border=0)

        self.wage_label: LBL = tbs.Label(self.wage_labelframe, text=currency_string(1000000000.25, self.currency_symbol), width=16, anchor="center")
        self.pension_label: LBL = tbs.Label(self.pension_labelframe, text=currency_string(1000000000.25, self.currency_symbol), width=17, anchor="center")
        self.rent_label: LBL = tbs.Label(self.rent_labelframe, text=currency_string(1000000000.25, self.currency_symbol), width=16, anchor="center")


    def place_selectable_labels_widgets(self, grid_margin_xy: float, widget_margin_xy: float):
        self.containter_frame.pack(padx=grid_margin_xy, pady=grid_margin_xy, expand="y")

        self.yearly_labelframe.grid(row=0, column=0, padx=widget_margin_xy, pady=widget_margin_xy)

        self.wage_labelframe.grid(row=0, column=0, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.wage_pension_separator.grid(row=0, column=1, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.pension_labelframe.grid(row=0, column=2, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.pension_rent_separator.grid(row=0, column=3, padx=widget_margin_xy+1, pady=widget_margin_xy)
        self.rent_labelframe.grid(row=0, column=4, padx=widget_margin_xy+1, pady=widget_margin_xy)

        self.wage_label.grid(row=0, column=0, padx=widget_margin_xy, pady=5)
        self.pension_label.grid(row=0, column=0, padx=widget_margin_xy, pady=5)
        self.rent_label.grid(row=0, column=0, padx=widget_margin_xy, pady=5)



if __name__ == "__main__":
    print(f"input_form.py: {__name__}")
    w = tbs.Window(themename="superhero")
    outp = OutputFields(w)
    outp.place_framed_entries_widgets(0, 0, 2, 1)
    w.mainloop()
