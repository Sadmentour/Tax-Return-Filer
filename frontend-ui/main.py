import ttkbootstrap as tbs
from input_form import *
from output import *
from widget_constants import *

WMIN_GEOMETRY = ("374", "160")
WMAX_GEOMETRY = ("395", "200")

window = tbs.Window(
    title="Tax Return Filer",
    themename="darkly",
    minsize=WMIN_GEOMETRY,
    maxsize=WMAX_GEOMETRY
    
)
window.geometry("395x148")

input_form = InputForm(window, FRAMED_ENTRIES, "Monthly")
output_fields = OutputFields(window, SELECTABLE_LABELS)

input_form.place_framed_entries_widgets(2)
output_fields.place_selectable_labels_widgets(5, 2)

window.mainloop()
