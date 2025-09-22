import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from mylocale import TR
import locale
import asyncio
import mypysound as mp
import myupdater as upd
import webbrowser


platform = toga.platform.current_platform


class SimpleThanks(toga.App):
    def startup(self):
        self.mypath = self.paths.app.absolute()
        self.tr_file = f"{self.mypath}/resources/localisation.csv"
        print(self.tr_file)
        upd.writeversion(filepath=self.mypath, version=self.version)
        self.update_url = upd.updater(
            repo="https://github.com/tct123/simplethanks",
            repo_path=f"releases/tag",
            file_url="https://raw.githubusercontent.com/tct123/simplethanks/refs/heads/main/src/simplethanks/VERSION",
        )
        if platform == "android":
            self.lang = str(
                self._impl.native.getResources().getConfiguration().getLocales().get(0)
            ).split("_")[0]
            # self.formal_name = (
            #    tr.tr( target_key="FORMALNAME", langcode=self.lang),
            # )

        else:
            self.lang = locale.getlocale()[0].split("_")[0]
        # self._description = tr.tr(
        #     target_key="DESCRIBTION", langcode=self.lang
        # )
        main_box = toga.Box()
        # print(self.BACKGROUND)
        # widgets
        tr = TR(langcode=self.lang, csv_file=self.tr_file)
        thxtext = toga.Label(
            text=tr.tr(target_key="THANKYOU", langcode=self.lang),
            style=Pack(margin=10, flex=1),
        )
        birthdaybtn = toga.Button(
            text=tr.tr(target_key="BIRTHDAY", langcode=self.lang),
            on_press=self.pressed_birthdaybtn,
            style=Pack(margin=10, flex=1),
        )
        mothersdaybtn = toga.Button(
            text=tr.tr(target_key="MOTHERSDAY", langcode=self.lang),
            on_press=self.pressed_mothersdaybtn,
            style=Pack(margin=10, flex=1),
        )
        fathersdaybtn = toga.Button(
            text=tr.tr(target_key="FATHERSDAY", langcode=self.lang),
            on_press=self.pressed_fathersdaybtn,
            style=Pack(margin=10, flex=1),
        )
        websitebtn = toga.Button(
            text="Website",
            on_press=self.pressed_visitwebsitebtn,
            style=Pack(margin=10, flex=1),
        )
        updatebtn = toga.Button(
            text="Check for updates",
            on_press=self.pressed_updatebtn,
            style=Pack(margin=10, flex=1),
        )

        # add
        main_box.add(thxtext)
        main_box.add(birthdaybtn)
        main_box.add(mothersdaybtn)
        main_box.add(fathersdaybtn)
        main_box.add(websitebtn)
        main_box.add(updatebtn)
        # style
        main_box.style.direction = "column"

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def pressed_birthdaybtn(self, widget):
        file = f"{self.paths.app.absolute()}/resources/happy-birthday-whistled.wav"
        mp.play(file=file)

    def pressed_mothersdaybtn(self, widget):
        motherdialog = toga.InfoDialog(
            title=tr.tr(target_key="HAPPYMOTHERSDAY", langcode=self.lang),
            message=tr.tr(target_key="HAPPYMOTHERSDAY", langcode=self.lang),
        )
        mothertask = asyncio.create_task(self.main_window.dialog(motherdialog))
        # mothertask.add_done_callback(self.dialog_dismissed)

    def pressed_fathersdaybtn(self, widget):
        fatherdialog = toga.InfoDialog(
            title=tr.tr(target_key="HAPPYFATHERSDAY", langcode=self.lang),
            message=tr.tr(target_key="HAPPYFATHERSDAY", langcode=self.lang),
        )
        fathertask = asyncio.create_task(self.main_window.dialog(fatherdialog))
        # fathertask.add_done_callback(self.dialog_dismissed)

    def pressed_visitwebsitebtn(self, widget):
        if platform not in ["android", "ios"]:
            self.visit_homepage()
        else:
            platformdialog = toga.InfoDialog(
                title=tr.tr(
                    target_key="SUPPORTEDPLATFORM",
                    langcode=self.lang,
                ),
                message=tr.tr(
                    target_key="SUPPORTEDPLATFORM",
                    langcode=self.lang,
                ),
            )
            platformtask = asyncio.create_task(self.main_window.dialog(platformdialog))

    def pressed_updatebtn(self, widget):
        webbrowser.open(url=self.update_url)


def main():
    return SimpleThanks()
