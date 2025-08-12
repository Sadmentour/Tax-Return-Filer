import ttkbootstrap as tbs

class Window(tbs.Window):
    def __init__(
        self, title="Tax Return Filer",
        themename="sandstone",
        iconphoto='',
        size=None,
        position=None,
        minsize=None,
        maxsize=None,
        resizable=None,
        hdpi=True,
        scaling=None,
        transient=None,
        overrideredirect=False,
        alpha=1,
        **kwargs
    ):
        super().__init__(
            title,
            themename,
            iconphoto,
            size,
            position,
            minsize,
            maxsize,
            resizable,
            hdpi,
            scaling,
            transient,
            overrideredirect,
            alpha,
            **kwargs
        )

    def create_widget_objects(self):
        pass

    def place_widgets(self):
        pass

    def unplace_widgets(self):
        pass
