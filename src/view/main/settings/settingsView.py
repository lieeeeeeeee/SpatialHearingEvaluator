import flet as ft

from src.view.main.settings.browseView import BrowseView

class SettingsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.inputDirView = BrowseView("Input Directory")
        self.outputDirView = BrowseView("Output Directory")
        self.create_components()

    def create_components(self):
        self.content = ft.Column(
            controls=[
                self.inputDirView,
                self.outputDirView,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )

        self.padding = ft.padding.symmetric(vertical=10)
        self.expand = True