import flet as ft
import flet.canvas as cv
import math

class ProgressView(ft.Container):
    def __init__(self):
        super().__init__()
        self.container = None
        self.canvas = None
        self.circle = None
        self.countLabel = None
        self.okButton = None
        self.width = 0
        self.height = 0
        self.create_components()
        
    def create_components(self):
        self.container = ft.Stack()
        self.canvas = cv.Canvas()
        self.circle = cv.Circle()
        self.countLabel = ft.Text()
        self.okButton = ft.OutlinedButton()

        self.canvas.shapes = [self.circle]
        
        self.circle.paint = ft.Paint(
            stroke_width=2,
            style=ft.PaintingStyle.STROKE,
            color=ft.colors.BLUE,
        )

        self.container.controls = [
            ft.Container(
                content=self.canvas,
                alignment=ft.alignment.center,
            ),
            ft.Column(
                controls=[
                    ft.Container(
                        content=self.countLabel,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=self.okButton,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]

        self.countLabel.value = "0"
        
        self.okButton.text = "OK"
        self.okButton.disabled = True
        
        self.content = self.container
    
    # public
    def set_count(self, count:int=0):
        self.countLabel.value = str(count)  

    def get_count(self) -> int:
        return int(self.countLabel.value)
    
    def switch_ok_button_availability(self, isAvailable):
        self.okButton.disabled = not isAvailable
    
    def adjust_component_size(self, parentWidth, parentHeight, ratioW=1, ratioH=1):
        self.width = parentWidth*ratioW
        self.height = parentHeight*ratioH

        self.canvas.width = self.width
        self.canvas.height = self.height

        self.circle.radius = self.height/2
        self.circle.x = self.width/2
        self.circle.y = self.height/2

        self.container.width = self.width
        self.container.height = self.height

        self.countLabel.size = self.height/3.5



        