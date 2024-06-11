import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import locale


platform = toga.platform.current_platform
if platform != "android" and platform != "ios":
    import playsound
    from pathlib import Path
else:
    from android.media import MediaPlayer
    from os.path import dirname, join


class SimpleThanks(toga.App):
    def startup(self):
        file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            )

        else:
            lang = locale.getlocale()
            lang, _ = lang
        main_box = toga.Box()

        # widgets
        thxtext = toga.Label(
            text=tr(csv_file=file, target_key="THANKYOU", langcode=lang),
            style=Pack(padding=10, flex=1),
        )
        birthdaybtn = toga.Button(
            text=tr(csv_file=file, target_key="BIRTHDAY", langcode=lang),
            on_press=self.pressed_birthdaybtn,
            style=Pack(padding=10, flex=1),
        )
        mothersdaybtn = toga.Button(
            text=tr(csv_file=file, target_key="MOTHERSDAY", langcode=lang),
            on_press=self.pressed_mothersdaybtn,
            style=Pack(padding=10, flex=1),
        )
        fathersdaybtn = toga.Button(
            text=tr(csv_file=file, target_key="FATHERSDAY", langcode=lang),
            on_press=self.pressed_fathersdaybtn,
            style=Pack(padding=10, flex=1),
        )

        # add
        main_box.add(thxtext)
        main_box.add(birthdaybtn)
        main_box.add(mothersdaybtn)
        main_box.add(fathersdaybtn)

        # style
        main_box.style.direction = "column"

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def pressed_birthdaybtn(self, widget):
        if platform != "android" and platform != "ios":
            self.resources_folder = Path(__file__).joinpath("../resources").resolve()
            self.birthday_filepath = self.resources_folder.joinpath(
                "happy-birthday-whistled.wav"
            )
            print(self.birthday_filepath)
            playsound.playsound(sound=self.birthday_filepath)
        else:
            player = MediaPlayer()
            sound = join(dirname(__file__), "resources/happy-birthday-whistled.wav")
            player.setDataSource(sound)
            player.prepare()
            player.start()

    def pressed_mothersdaybtn(self, widget):
        self.main_window.info_dialog(
            title="Happy Mothersday", message="Happy Mothersday"
        )

    def pressed_fathersdaybtn(self, widget):
        self.main_window.info_dialog(
            title="Happy Fathersday", message="Happy Fathersday"
        )


def main():
    return SimpleThanks()
