import ttkbootstrap as ttk
from ttkbootstrap import DoubleVar
from tkinter import messagebox, TclError
from widget_constants import *
import TaxReturn as tR
from conversions import monthly_to_yearly

tax_return = tR.TaxReturn()

wage_tax: float = 0
pension_tax: float = 0
rent_tax: float = 0

HELP_MESSAGE = "To input into the program, insert the numeric " \
               "value of your income(s) on the three textboxes " \
               "accordingly. When this is done, click 'Enter Values' " \
               "in the 'Tools' menu to complete the process."

def help_box():
    messagebox.showinfo(title="How to use", message=HELP_MESSAGE)

def refresh_constants():
    tax_return.financial_constants.init_constants()

def apply_values():
    global wage_tax
    global pension_tax
    global rent_tax
    
    try:
        wage_tax = monthly_to_yearly(wage_value.get())
        pension_tax = monthly_to_yearly(pension_value.get())
        rent_tax = monthly_to_yearly(rent_value.get())
    except TclError:
        messagebox.showerror(title="Only numbers", message="Your income must not contain anything"
                                                         "that isn't a number.")

    wage_gauge.config(text=f"€{wage_tax:,.2f}")
    pension_gauge.config(text=f"€{pension_tax:,.2f}")
    rent_gauge.config(text=f"€{rent_tax:,.2f}")

window: WIN = ttk.Window(title="Tax Return Filer", themename="darkly")

wage_value: DoubleVar = DoubleVar()
pension_value: DoubleVar = DoubleVar()
rent_value: DoubleVar = DoubleVar()

menubar: MEN = ttk.Menu(window)
window.config(menu=menubar)

menus = {}
menus['Tools'] = ttk.Menu(menubar, type='menubar')
menus['Help'] = ttk.Menu(menubar, type='normal')

menus['Tools'].add_command(label="Enter Values", command=apply_values)
menus['Tools'].add_command(label="Load Fiscals", command=refresh_constants)

# menus['Help'].add_command(label=)

menubar.add_cascade(label='Tools', menu=menus['Tools'])
menubar.add_cascade(label='Help', command=help_box)

entry_form_frame: FRM = ttk.Frame(window)
entry_form_frame.pack()

yearmonth_labelframe: LBF = ttk.Labelframe(entry_form_frame, text="Income")
yearmonth_labelframe.grid(row=0, rowspan=2, column=0, padx=4, pady=4, sticky="ns")

monthly_label: LBL = ttk.Label(yearmonth_labelframe, text="Monthly")
monthly_label.grid(row=0, column=0, padx=4, pady=8)

annual_label: LBL = ttk.Label(yearmonth_labelframe, text="Annual")
annual_label.grid(row=1, column=0, padx=4, pady=5, sticky="s")

#######################
# Wage Widgets
#######################

wage_labelframe: LBF = ttk.Labelframe(entry_form_frame, text="Wage", labelanchor="nw")
wage_labelframe.grid(row=0, rowspan=2, column=1, padx=4, pady=4, sticky="ns")

wage_entry: ENT = ttk.Entry(wage_labelframe, textvariable=wage_value)
wage_entry.grid(row=0, column=0, padx=4, pady=4)

wage_gauge: LBL = ttk.Label(wage_labelframe, text=f"€{0:,.2f}")
wage_gauge.grid(row=1, column=0, padx=4, pady=4, sticky="w")

#######################
# Pension Widgets
#######################

pension_labelframe: LBF = ttk.Labelframe(entry_form_frame, text="Pension", labelanchor="nw")
pension_labelframe.grid(row=0, rowspan=2, column=2, padx=4, pady=4, sticky="ns")

pension_entry: ENT = ttk.Entry(pension_labelframe, textvariable=pension_value)
pension_entry.grid(row=0, column=0, padx=4, pady=4)

pension_gauge: LBL = ttk.Label(pension_labelframe, text=f"€{0:,.2f}")
pension_gauge.grid(row=1, column=0, padx=4, pady=4, sticky="w")

#######################
# Rent Widgets
#######################

rent_labelframe: LBF = ttk.Labelframe(entry_form_frame, text="Rent", labelanchor="nw")
rent_labelframe.grid(row=0, rowspan=2, column=3, padx=4, pady=4, sticky="ns")

rent_entry: ENT = ttk.Entry(rent_labelframe, textvariable=rent_value)
rent_entry.grid(row=0, column=0, padx=4, pady=4)

rent_gauge: LBL = ttk.Label(rent_labelframe, text=f"€{0:,.2f}")
rent_gauge.grid(row=1, column=0, padx=4, pady=4, sticky="w")

###########################################


window.mainloop()

"""
###########################################
# CODE LIMBO: where functions hibernate...
###########################################

def apply_values():
    global wage_tax
    global pension_tax
    global rent_tax
    
    try:
        wage_tax = tax_return.calculate_income_tax(wage_value.get(), "wage")
        pension_tax = tax_return.calculate_income_tax(pension_value.get(), "wage")
        rent_tax = tax_return.calculate_income_tax(rent_value.get(), "rent")
    except TclError:
        messagebox.showerror(title="Only numbers", message="Your income must not contain anything"
                                                         "that isn't a number.")

    wage_gauge.config(text=f"€{wage_tax:,.2f}")
    pension_gauge.config(text=f"€{pension_tax:,.2f}")
    rent_gauge.config(text=f"€{rent_tax:,.2f}")
"""
