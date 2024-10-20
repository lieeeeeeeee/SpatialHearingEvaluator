import flet as ft

class BrowseView(ft.Container):
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.textField = None
        self.button = None
        self.create_components()

    def create_components(self):
        self.textField = ft.TextField()
        self.button = ft.IconButton()
        spacing = 20
        self.textField.label = self.label
        self.textField.expand = True
        self.button.icon = ft.icons.FOLDER

        self.content = ft.Row(
            controls=[
                self.textField,
                self.button,
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=spacing,
            expand=True,
        )
