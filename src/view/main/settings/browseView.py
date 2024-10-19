import flet as ft

class BrowseView(ft.Container):
    def __init__(self):
        
        super().__init__()
        self.create_components()

    def create_components(self):
        self.content = ft.Text("Browse")
        self.expand = True
        self.bgcolor = ft.colors.PURPLE