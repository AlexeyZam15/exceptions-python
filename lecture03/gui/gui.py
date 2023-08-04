from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from random import randint

from lecture03.gui.savedexception import SavedException
from lecture03.gui.saveservice import SaveService
import traceback

Window.size = (300, 100)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Сохранятор"


class Gui(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text="Сохранятор")
        self.save_service = SaveService()

    def btn_pressed(self, *args):
        try:
            self.save_service.save()
            self.label.text = "Saved successfully"
        # except IOError as e:
        #     self.label.text = "Saved failed"
        except SavedException as e:
            self.label.text = f"Saved failed at {e.start_date}"
            traceback.print_exc()

    def build(self):
        box = BoxLayout(orientation="vertical")
        btn = Button(text="Save")
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)

        return box


if __name__ == "__main__":
    Gui().run()
