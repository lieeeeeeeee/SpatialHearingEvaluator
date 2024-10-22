import flet as ft
import flet.canvas as cv
import math

from src.view.main.inspection.localization.progressView import ProgressView

class LocalizationView(ft.Container):
    def __init__(self):
        super().__init__()
        self.container = None
        self.canvas = None
        self.circle = None
        self.pointer = None
        self.gestureDetector = None
        self.progressView = None
        self.width = 0
        self.height = 0
        self.scaleDistance = 0
        self.create_components()

    def create_components(self):
        self.container = ft.Stack()
        self.canvas = cv.Canvas()
        self.circle = cv.Circle()
        self.pointer = cv.Circle()
        self.gestureDetector = ft.GestureDetector()
        self.progressView = ProgressView()

        self.canvas.shapes = [self.circle, self.pointer]

        self.circle.paint = ft.Paint( 
            stroke_width=2,
            style=ft.PaintingStyle.STROKE,
            color=ft.colors.BLUE,
        )

        self.pointer.paint = ft.Paint(
            style=ft.PaintingStyle.FILL,
            color=ft.colors.RED,
        )

        self.gestureDetector.drag_interval = 10
        
        self.container.controls = [
            ft.Container(
                content=self.canvas,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=self.progressView,
                alignment=ft.alignment.center,
            ),
            self.gestureDetector,
        ]

        self.content = self.container


    # private
    def change_angel(self, angel:int=0, anchor:int=0):
        return (angel - anchor) % 360

    def build_scale(self, angle:int=0):
        lineLength = 10
        textSize = 12
        # line
        x = self.width/2 + (self.circle.radius+lineLength/2) * math.cos(math.radians(angle))
        y = self.height/2 + (self.circle.radius+lineLength/2) * math.sin(math.radians(angle))
        x2 = self.width/2 + (self.circle.radius-lineLength/2) * math.cos(math.radians(angle))
        y2 = self.height/2 + (self.circle.radius-lineLength/2) * math.sin(math.radians(angle))
        line = cv.Line(x1=x, y1=y, x2=x2, y2=y2, paint=ft.Paint(stroke_width=2, color=ft.colors.BLUE))
        # text
        x = self.width/2 + (self.circle.radius+lineLength/2+textSize) * math.cos(math.radians(angle))
        y = self.height/2 + (self.circle.radius+lineLength/2+textSize) * math.sin(math.radians(angle))
        changedAngle = self.change_angel(angle, 270)
        text = cv.Text(x=x, y=y, text=str(changedAngle), text_align=ft.TextAlign.RIGHT, alignment=ft.alignment.center, style=ft.TextStyle(size=textSize))

        self.canvas.shapes.append(line)
        self.canvas.shapes.append(text)

    def build_scales(self):
        if self.scaleDistance == 0: return
        for i in range(270, 630, self.scaleDistance):
            self.build_scale(i)

    # public
    def get_circle_radius(self) -> int: return self.circle.radius
    def get_circle_center(self) -> tuple: return (self.circle.x, self.circle.y)
    def get_pointer_position(self) -> tuple: return (self.pointer.x, self.pointer.y)
    def set_pointer_position(self, x:int=0, y:int=0): self.pointer.x, self.pointer.y = x, y
    def set_scale_distance(self, distance:int=0): self.scaleDistance = distance
    
    def display_pointer(self, x:int=0, y:int=0):
        self.pointer.radius = 10
        
    def dismiss_pointer(self):
        self.pointer.radius = 0

    def init_pointer_position(self):
        self.pointer.x = self.width/2
        self.pointer.y = 0

    def adjust_components_size(self, parentWidth, parentHeight, ratioW=1, ratioH=1):
        self.width = parentWidth*ratioW
        self.height = parentHeight*ratioH
        self.progressView.adjust_component_size(self.width, self.height, 0.25, 0.25)

        self.canvas.width = self.width
        self.canvas.height = self.height

        self.circle.radius = min(self.width, self.height)/2
        self.circle.x = self.width/2
        self.circle.y = self.height/2

        self.dismiss_pointer()
        self.init_pointer_position()

        self.build_scales()

        self.container.width = self.width
        self.container.height = self.height


