import flet as ft

from src.view.main.inspection.localization.progressView import ProgressView

class LocalizationView(ft.Container):
    def __init__(self):
        super().__init__()
        self.create_components()

    def create_components(self):
        self.content = ft.Text("Localization")
        self.expand = True
        self.bgcolor = ft.colors.RED
        