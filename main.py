# THIS IS A TUTORIAL PROJECT FROM https://youtu.be/l8Imtec4ReQ?si=R_qphKMilqJa9qBM

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    pass


"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Button1")
        b2 = Button(text="Button2")
        self.orientation = "vertical"
        # the order of writing is important
        self.add_widget(b1)
        self.add_widget(b2)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
