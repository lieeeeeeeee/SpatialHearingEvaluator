import flet as ft

class ControlButtonsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.container = None
        self.stopButton = None
        self.startButton = None
        self.outputButton = None
        self.width = 0
        self.height = 0
        self.create_components()

    def create_components(self):
        self.container = ft.Row()
        self.stopButton = ft.OutlinedButton("Stop")
        self.startButton = ft.OutlinedButton("Start")
        self.outputButton = ft.OutlinedButton("Output")

        # self.stopButton.expand = True
        # self.startButton.expand = True
        # self.outputButton.expand = True

        self.container.controls = [
            self.stopButton,
            self.startButton,
            self.outputButton,
        ]
        self.container.alignment = ft.MainAxisAlignment.SPACE_AROUND

        self.expand = True
        self.content = self.container

    def adjust_components_size(self, parentWidth, parentHeight, ratioW=1, ratioH=1):
        self.width = parentWidth*ratioW
        self.height = parentHeight*ratioH
        self.container.width = self.width
        self.container.height = self.height

        self.stopButton.height = parentHeight / 20
        self.startButton.height = parentHeight / 13
        self.outputButton.height = parentHeight / 20

        self.stopButton.width = self.width / 5
        self.startButton.width = self.width / 5
        self.outputButton.width = self.width / 5
