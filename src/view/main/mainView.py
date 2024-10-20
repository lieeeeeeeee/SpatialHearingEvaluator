import flet as ft

from src.view.main.inspection.inspectionView import InspectionView
from src.view.main.settings.settingsView import SettingsView


class MainView:
    def __init__(self):
        self.page: ft.Page = None
        self.inspectionView: InspectionView = None
        self.settingsView: SettingsView = None
        self.content = None

        self.build()

    def build(self):
        self.inspectionView = InspectionView()
        self.settingsView = SettingsView()
        self.content = ft.Row(
            controls=[
                self.settingsView,
                self.inspectionView,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
        )

    def loop(self):
        ft.app(target=self.initAdd)

    def initAdd(self, page: ft.Page):
        self.page = page
        page.add(self.content)
        
    def update(self):
        self.page.update()