import flet as ft

from src.view.main.inspection.localization.localizationView import LocalizationView
from src.view.main.inspection.controlButtonsView import ControlButtonsView

class InspectionView(ft.Container):
    def __init__(self):
        super().__init__()
        self.create_components()

    def create_components(self):
        self.content = ft.Text("Inspection")
        self.expand = True
        self.bgcolor = ft.colors.GREEN