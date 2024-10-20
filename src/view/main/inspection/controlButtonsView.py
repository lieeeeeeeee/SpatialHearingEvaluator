import flet as ft

class ControlButtonsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.stopButton = None
        self.startButton = None
        self.outputButton = None
        self.create_components()

    def create_components(self):
        self.stopButton = ft.OutlinedButton("Stop")
        self.startButton = ft.OutlinedButton("Start")
        self.outputButton = ft.OutlinedButton("Output")

        self.stopButton.expand = True
        self.startButton.expand = True
        self.outputButton.expand = True

        self.content = ft.Row(
            controls=[
                self.stopButton,
                self.startButton,
                self.outputButton,
            ],
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )