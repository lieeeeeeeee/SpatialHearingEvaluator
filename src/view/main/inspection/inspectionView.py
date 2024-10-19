import flet as ft

from src.view.main.inspection.localization.localizationView import LocalizationView
from src.view.main.inspection.controlButtonsView import ControlButtonsView

class InspectionView(ft.Container):
    def __init__(self):
        super().__init__()
        self.localizationView = LocalizationView()
        self.controlButtonsView = ControlButtonsView()
        self.create_components()

    def create_components(self):
        self.content = ft.Column(
            controls=[
                self.localizationView,
                self.controlButtonsView,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
        )
        self.expand = True
        self.bgcolor = ft.colors.GREEN