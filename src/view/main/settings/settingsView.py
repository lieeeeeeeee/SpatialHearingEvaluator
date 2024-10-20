import flet as ft

from src.view.main.settings.browseView import BrowseView

class SettingsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.inputDirBrowseView = None
        self.outputDirBrowseView = None
        self.subjectNameTextField = None
        self.experimentNameTextField = None

        self.create_components()

    def create_components(self):
        self.inputDirBrowseView = BrowseView("Input Directory")
        self.outputDirBrowseView = BrowseView("Output Directory")
        self.subjectNameTextField = ft.TextField()
        self.experimentNameTextField = ft.TextField()
        self.subjectNameTextField.label = "Subject Name"
        self.experimentNameTextField.label = "Experiment Name"

        self.content = ft.Column(
            controls=[
                self.inputDirBrowseView,
                self.outputDirBrowseView,
                self.subjectNameTextField,
                self.experimentNameTextField,
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        )

        self.padding = ft.padding.symmetric(vertical=20, horizontal=40)
        self.expand = True

    # public
    def get_input_dir(self):
        return self.inputDirBrowseView.textField.value
    
    def get_output_dir(self):
        return self.outputDirBrowseView.textField.value
    
    def get_subject_name(self):
        return self.subjectNameTextField.value
    
    def get_experiment_name(self):
        return self.experimentNameTextField.value