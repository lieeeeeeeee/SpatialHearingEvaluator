import flet as ft

from src.view.main.inspection.localization.localizationView import LocalizationView
from src.view.main.inspection.controlButtonsView import ControlButtonsView

class InspectionView(ft.Container):
    def __init__(self):
        super().__init__()
        self.container = None
        self.localizationView = None
        self.controlButtonsView = None
        self.audio = None
        self.width = 0
        self.height = 0
        self.create_components()

    def create_components(self):
        self.container = ft.Column()
        self.localizationView = LocalizationView()
        self.controlButtonsView = ControlButtonsView()
        self.audio = ft.Audio()

        self.container.controls = [self.localizationView, self.controlButtonsView, self.audio]
        self.container.alignment = ft.MainAxisAlignment.CENTER

        self.audio.src = "materials/sounds/sample_sound.wav"

        self.content = self.container

    def adjust_components_size(self, parentWidth, parentHeight):
        verticalPadding = parentHeight*0.05
        horizontalPadding = parentWidth*0.05
        spacing = parentHeight*0.05

        self.margin = ft.margin.only(top=verticalPadding, left=horizontalPadding, right=horizontalPadding)
        
        self.width = (parentWidth - 2*horizontalPadding)/2
        self.height = parentHeight - 2*verticalPadding - spacing*(len(self.container.controls)-1)

        self.localizationView.adjust_components_size(self.width, self.height, ratioH=0.8)
        self.controlButtonsView.adjust_components_size(self.width, self.height, ratioH=0.2)

        self.container.width = self.width
        self.container.height = self.height

        self.container.spacing = spacing


    # public
    def set_audio_src(self, src:str):
        self.audio.release()
        self.audio.src = src

    def get_audio_src(self) -> str: return self.audio.src
    def get_audio_current_position(self) -> float: return self.audio.get_current_position()
    
    def play_audio(self):
        self.audio.play()
