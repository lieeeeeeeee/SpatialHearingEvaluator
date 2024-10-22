import flet as ft

from src.view.main.inspection.inspectionView import InspectionView
from src.view.main.settings.settingsView import SettingsView


class MainView:
    def __init__(self):
        self.page: ft.Page = None
        self.container = None
        self.inspectionView: InspectionView = None
        self.settingsView: SettingsView = None
        self.content = None
        self.width = 0
        self.height = 0

        self.build()

    def build(self):
        self.container = ft.Row()
        self.inspectionView = InspectionView()
        self.settingsView = SettingsView()

        self.container.controls = [self.settingsView, self.inspectionView]
        self.container.alignment = ft.MainAxisAlignment.END
        self.container.expand = True

        self.content = self.container
        
    def adjust_components_size(self, windowWidth, windowHeight):
        self.width = windowWidth
        self.height = windowHeight
        self.inspectionView.adjust_components_size(self.width, self.height)
        self.settingsView.adjust_components_size(self.width, self.height)
        self.container.width = self.width
        self.container.height = self.height

    def loop(self):
        ft.app(target=self.initAdd)

    def initAdd(self, page: ft.Page):
        self.page = page

        self.initUpdate()
        page.add(self.content)
        
    def initUpdate(self):
        self.adjust_components_size(self.page.window.width, self.page.window.height)

    def update(self):
        self.page.update()