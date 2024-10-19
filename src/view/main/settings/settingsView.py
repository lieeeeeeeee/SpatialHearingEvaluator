import flet as ft

from src.view.main.settings.browseView import BrowseView

class SettingsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.inputDirView = BrowseView()
        self.outputDirView = BrowseView()
        self.create_components()

    def create_components(self):
        self.content = ft.Column(
            controls=[
                self.inputDirView,
                self.outputDirView,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
        )
        self.expand = True
        self.bgcolor = ft.colors.BLUE