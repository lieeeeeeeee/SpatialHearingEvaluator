import flet as ft

from src.view.main.settings.browseView import BrowseView

class SettingsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.create_components()

    def create_components(self):
        self.content = ft.Text("Settings")
        self.expand = True
        self.bgcolor = ft.colors.BLUE