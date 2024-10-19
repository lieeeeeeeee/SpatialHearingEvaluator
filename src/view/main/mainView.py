import flet as ft

from src.view.main.inspection.inspectionView import InspectionView
from src.view.main.settings.settingsView import SettingsView


class MainView:
    def __init__(self):
        self.page = None
        self.contentView = None
        ft.app(target=self.build)

    def build(self, page: ft.Page):
        self.page = page
        self.contentView = InspectionView()
        self.settingsView = SettingsView()

        page.add(
            ft.Row(
                controls=[ft.Text("Main View")],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                expand=True,
            )
        )

    def update(self):
        self.page.update()