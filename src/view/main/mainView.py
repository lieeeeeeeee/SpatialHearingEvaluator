import flet as ft

from src.view.main.inspection.inspectionView import InspectionView
from src.view.main.settings.settingsView import SettingsView


class MainView:
    def __init__(self):
        self.page: ft.Page = None
        self.inspectionView: InspectionView = None
        self.settingsView: SettingsView = None
        ft.app(target=self.build)

    def build(self, page: ft.Page):
        self.page = page
        self.inspectionView = InspectionView()
        self.settingsView = SettingsView()

        page.add(
            ft.Row(
                controls=[
                    self.inspectionView,
                    self.settingsView,
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                expand=True,
            )
        )

    def update(self):
        self.page.update()