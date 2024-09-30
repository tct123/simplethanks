import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale.TR import tr
import locale
import asyncio


platform = toga.platform.current_platform

if platform != "android" and platform != "ios":
    import playsound
    from pathlib import Path
else:
    from android.media import MediaPlayer
    from os.path import dirname, join


class SimpleThanks(toga.App):
    def startup(self):
        self.file = f"{self.paths.app.absolute()}/resources/localisation.csv"
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
            # self.formal_name = (
            #    tr(csv_file=self.file, target_key="FORMALNAME", langcode=self.lang),
            # )

        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        # self._description = tr(
        #    csv_file=self.file, target_key="DESCRIBTION", langcode=self.lang
        # )
        main_box = toga.Box()

        # widgets
        thxtext = toga.Label(
            text=tr(csv_file=self.file, target_key="THANKYOU", langcode=self.lang),
            style=Pack(padding=10, flex=1),
        )
        birthdaybtn = toga.Button(
            text=tr(csv_file=self.file, target_key="BIRTHDAY", langcode=self.lang),
            on_press=self.pressed_birthdaybtn,
            style=Pack(padding=10, flex=1),
        )
        mothersdaybtn = toga.Button(
            text=tr(csv_file=self.file, target_key="MOTHERSDAY", langcode=self.lang),
            on_press=self.pressed_mothersdaybtn,
            style=Pack(padding=10, flex=1),
        )
        fathersdaybtn = toga.Button(
            text=tr(csv_file=self.file, target_key="FATHERSDAY", langcode=self.lang),
            on_press=self.pressed_fathersdaybtn,
            style=Pack(padding=10, flex=1),
        )
        websitebtn = toga.Button(
            text="Website",
            on_press=self.pressed_visitwebsitebtn,
            style=Pack(padding=10, flex=1),
        )

        # add
        main_box.add(thxtext)
        main_box.add(birthdaybtn)
        main_box.add(mothersdaybtn)
        main_box.add(fathersdaybtn)
        main_box.add(websitebtn)

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
        motherdialog = toga.InfoDialog(
            title=tr(
                csv_file=self.file, target_key="HAPPYMOTHERSDAY", langcode=self.lang
            ),
            message=tr(
                csv_file=self.file, target_key="HAPPYMOTHERSDAY", langcode=self.lang
            ),
        )
        mothertask = asyncio.create_task(self.main_window.dialog(motherdialog))
        # mothertask.add_done_callback(self.dialog_dismissed)

    def pressed_fathersdaybtn(self, widget):
        fatherdialog = toga.InfoDialog(
            title=tr(
                csv_file=self.file, target_key="HAPPYFATHERSDAY", langcode=self.lang
            ),
            message=tr(
                csv_file=self.file, target_key="HAPPYFATHERSDAY", langcode=self.lang
            ),
        )
        fathertask = asyncio.create_task(self.main_window.dialog(fatherdialog))
        # fathertask.add_done_callback(self.dialog_dismissed)

    def pressed_visitwebsitebtn(self, widget):
        self.visit_homepage()


def main():
    return SimpleThanks()
