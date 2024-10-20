from src.view.main.mainView import MainView

class MainViewController:
    def __init__(self):
        self.mainView = MainView()

        self.events_handler()

        self.mainView.loop()

    def events_handler(self):
        print("Events Handler")
        self.mainView.settingsView.inputDirView.browseButton.on_click = self.on_click_input_dir_browse_button
        self.mainView.settingsView.outputDirView.browseButton.on_click = self.on_click_output_dir_browse_button

    def on_click_input_dir_browse_button(self, event):
        print("Input Dir Browse Button Clicked")

    def on_click_output_dir_browse_button(self, event):
        print("Output Dir Browse Button Clicked")


