import flet as ft

class BrowseView(ft.Container):
    def __init__(self, label):
        super().__init__()
        self.textField = ft.TextField()
        self.browseButton = ft.IconButton()
        self.label = label
        self.create_components()

    def create_components(self):
        spacing = 20
        self.textField.label = self.label
        self.browseButton.icon = ft.icons.FOLDER

        self.content = ft.Row(
            controls=[
                self.textField,
                self.browseButton,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=spacing,
            expand=True,
        )
        self.padding = spacing