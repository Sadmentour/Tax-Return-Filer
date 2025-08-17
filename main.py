import ttkbootstrap as ttk
from ttkbootstrap import DoubleVar
from tkinter import messagebox, TclError
from widget_constants import *
import TaxReturn as tR
from conversions import monthly_to_yearly, \
                        yearly_to_monthly

tax_return = tR.TaxReturn()

def help_box():
    messagebox.showinfo(title="How to use", message=HELP_MESSAGE)

def refresh_constants():
    tax_return.financial_constants.init_constants()

def apply_values():
    wage_tax: float = 0
    pension_tax: float = 0
    rent_tax: float = 0
    
    try:
        wage_tax = monthly_to_yearly(wage_value_month.get())
        pension_tax = monthly_to_yearly(pension_value_month.get())
        rent_tax = monthly_to_yearly(rent_value_month.get())
    except TclError:
        messagebox.showerror(title="Only numbers", message="Your income must not contain anything"
                                                         "that isn't a number.")

    wage_year.config(text=f"€{wage_tax:,.2f}")
    pension_year.config(text=f"€{pension_tax:,.2f}")
    rent_year.config(text=f"€{rent_tax:,.2f}")
    total_gauge.config(text=f"€{sum([
        wage_tax,
        pension_tax,
        rent_tax
    ]):,.2f}")

def set_tax_gauges():
    wage_year_float = float(wage_year.cget("text").replace("€", "").replace(",", ""))
    pension_year_float = float(pension_year.cget("text").replace("€", "").replace(",", ""))
    rent_year_float = float(rent_year.cget("text").replace("€", "").replace(",", ""))

    wage_gauge.config(text=f"€{tax_return.calculate_income_tax(yearly_to_monthly(wage_year_float), "wage"):,.2f}")
    pension_gauge.config(text=f"€{tax_return.calculate_income_tax(yearly_to_monthly(pension_year_float), "wage"):,.2f}")
    rent_gauge.config(text=f"€{tax_return.calculate_income_tax(yearly_to_monthly(rent_year_float), "rent"):,.2f}")

    wage_gauge_float = float(wage_gauge.cget("text").replace("€", "").replace(",", ""))
    pension_gauge_float = float(pension_gauge.cget("text").replace("€", "").replace(",", ""))
    rent_gauge_float = float(rent_gauge.cget("text").replace("€", "").replace(",", ""))

    taxed_total_gauge.config(text=f"€{sum(
        [
            wage_gauge_float,
            pension_gauge_float,
            rent_gauge_float
        ]
    ):,.2f}")

window: WIN = ttk.Window(title="Tax Return Filer", themename="sandstone", resizable=(False, False))

wage_value_month: DoubleVar = DoubleVar()
pension_value_month: DoubleVar = DoubleVar()
rent_value_month: DoubleVar = DoubleVar()

wage_value_year: DoubleVar = DoubleVar()
pension_value_year: DoubleVar = DoubleVar()
rent_value_year: DoubleVar = DoubleVar()

menubar: MEN = ttk.Menu(window)
window.config(menu=menubar)

menus = {}
menus['Tools'] = ttk.Menu(menubar, type='menubar')
menus['Help'] = ttk.Menu(menubar, type='normal')

menus['Tools'].add_command(label="Load Fiscals", command=refresh_constants)
menus['Tools'].add_command(label="Enter Values", command=apply_values)
menus['Tools'].add_command(label="Calculate", command=set_tax_gauges)

# menus['Help'].add_command(label=)

menubar.add_cascade(label='Tools', menu=menus['Tools'])
menubar.add_cascade(label='Help', command=help_box)

main_frame: FRM = ttk.Frame(window)
main_frame.pack(anchor="nw")

#######################
# Yearmonth Widgets
#######################

yearmonth_labelframe: LBF = ttk.Labelframe(main_frame, text="Income")
yearmonth_labelframe.grid(row=0, rowspan=2, column=0, padx=4, pady=4, sticky="ns")

monthly_label: LBL = ttk.Label(yearmonth_labelframe, text="Monthly")
monthly_label.grid(row=0, column=0, padx=4, pady=8)

annual_label: LBL = ttk.Label(yearmonth_labelframe, text="Annual")
annual_label.grid(row=1, column=0, padx=4, pady=5, sticky="s")

#######################
# Wage Widgets
#######################

wage_labelframe: LBF = ttk.Labelframe(main_frame, text="Wage", labelanchor="nw")
wage_labelframe.grid(row=0, rowspan=2, column=1, padx=4, pady=4, sticky="ns")

wage_entry: ENT = ttk.Entry(wage_labelframe, textvariable=wage_value_month)
wage_entry.grid(row=0, column=0, padx=4, pady=4)

wage_year: LBL = ttk.Label(wage_labelframe, text=f"€{0:,.2f}")
wage_year.grid(row=1, column=0, padx=4, pady=4, sticky="w")
#######################
# Pension Widgets
#######################

pension_labelframe: LBF = ttk.Labelframe(main_frame, text="Pension", labelanchor="nw")
pension_labelframe.grid(row=0, rowspan=2, column=2, padx=4, pady=4, sticky="ns")

pension_entry: ENT = ttk.Entry(pension_labelframe, textvariable=pension_value_month)
pension_entry.grid(row=0, column=0, padx=4, pady=4)

pension_year: LBL = ttk.Label(pension_labelframe, text=f"€{0:,.2f}")
pension_year.grid(row=1, column=0, padx=4, pady=4, sticky="w")

#######################
# Rent Widgets
#######################

rent_labelframe: LBF = ttk.Labelframe(main_frame, text="Rent", labelanchor="nw")
rent_labelframe.grid(row=0, rowspan=2, column=3, padx=4, pady=4, sticky="ns")

rent_entry: ENT = ttk.Entry(rent_labelframe, textvariable=rent_value_month)
rent_entry.grid(row=0, column=0, padx=4, pady=4)

rent_year: LBL = ttk.Label(rent_labelframe, text=f"€{0:,.2f}")
rent_year.grid(row=1, column=0, padx=4, pady=4, sticky="w")

###########################################

wage_gauge_labelframe: LBF = ttk.Labelframe(main_frame, text="Taxed Wage")
wage_gauge_labelframe.grid(row=2, column=1, padx=4, sticky="we")
wage_gauge: LBL = ttk.Label(wage_gauge_labelframe, text=f"€{0:,.2f}")
wage_gauge.pack(padx=4, pady=4, anchor="w")

pension_gauge_labelframe: LBF = ttk.Labelframe(main_frame, text="Taxed Pension")
pension_gauge_labelframe.grid(row=2, column=2, padx=4, sticky="we")
pension_gauge: LBL = ttk.Label(pension_gauge_labelframe, text=f"€{0:,.2f}")
pension_gauge.pack(padx=4, pady=4, anchor="w")

rent_gauge_labelframe: LBF = ttk.Labelframe(main_frame, text="Taxed Rent")
rent_gauge_labelframe.grid(row=2, column=3, padx=4, sticky="we")
rent_gauge: LBL = ttk.Label(rent_gauge_labelframe, text=f"€{0:,.2f}")
rent_gauge.pack(padx=4, pady=4, anchor="w")

total_labelframe: LBF = ttk.Labelframe(main_frame, text="Total Annual Income")
total_labelframe.grid(row=3, column=1, padx=4, pady=4, sticky="we")
total_gauge: LBL = ttk.Label(total_labelframe, text=f"€{0:,.2f}")
total_gauge.pack(padx=4, pady=4, anchor="w")

taxed_total_labelframe: LBF = ttk.Labelframe(main_frame, text="Taxed Total")
taxed_total_labelframe.grid(row=3, column=3, padx=4, pady=4, sticky="we")
taxed_total_gauge: LBL = ttk.Label(taxed_total_labelframe, text=f"€{0:,.2f}")
taxed_total_gauge.pack(padx=4, pady=4, anchor="w")

window.mainloop()
