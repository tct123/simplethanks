"""
A simple thank you
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


plattform = toga.platform.current_platform

if plattform != "android" and plattform != "ios":
    import playsound
    from pathlib import Path
else:
    from android.media import MediaPlayer
    from os.path import dirname, join


class SimpleThanks(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """        
        main_box = toga.Box()

        # widgets
        thxtext = toga.Label(text="Thank you, ...", style=Pack(padding=10, flex=1))
        birthdaybtn = toga.Button(
            text="Birthday",
            on_press=self.pressed_birthdaybtn,
            style=Pack(padding=10, flex=1),
        )
        mothersdaybtn = toga.Button(
            text="Mothers Day",
            on_press=self.pressed_mothersdaybtn,
            style=Pack(padding=10, flex=1),
        )
        fathersdaybtn = toga.Button(
            text="Fathers day",
            on_press=self.pressed_fathersdaybtn,
            style=Pack(padding=10, flex=1),
        )

        # add
        main_box.add(thxtext)
        main_box.add(birthdaybtn)
        main_box.add(mothersdaybtn)
        main_box.add(fathersdaybtn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def pressed_birthdaybtn(self, widget):
        if plattform != "android" and plattform != "ios":
            self.resources_folder = Path(__file__).joinpath("../resources").resolve()
            self.birthday_filepath = self.resources_folder.joinpath("happy-birthday-whistled.wav")
            print(self.birthday_filepath)
            playsound.playsound(sound=self.birthday_filepath)
        else:
            player = MediaPlayer()
            sound =join(dirname(__file__), "resources/happy-birthday-whistled.wav")
            player.setDataSource(sound)
            player.prepare()
            player.start()

    def pressed_mothersdaybtn(self, widget):
        self.main_window.info_dialog(title="Happy Mothersday",message="Happy Mothersday")

    def pressed_fathersdaybtn(self, widget):
        self.main_window.info_dialog(title="Happy Fathersday",message="Happy Fathersday")


def main():
    return SimpleThanks()
