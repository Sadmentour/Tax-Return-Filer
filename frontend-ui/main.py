import ttkbootstrap as tbs
from input_form import *
from output import *
from widget_constants import *

window = tbs.Window(
    title="Tax Return Filer",
    themename="darkly",
)

input_form = InputForm(window, FRAMED_ENTRIES, "Monthly")
output_fields = OutputFields(window, SELECTABLE_LABELS)

input_form.place_framed_entries_widgets(0, 0, 5, 2)
output_fields.place_selectable_labels_widgets(1, 0, 5, 2)

window.mainloop()
