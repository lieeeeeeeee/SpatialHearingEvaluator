from src.view.main.mainView import MainView

class MainViewController:
    def __init__(self):
        self.mainView = MainView()

        self.events_handler()

        self.mainView.loop()

    def events_handler(self):
        print("Events Handler")
        self.mainView.settingsView.inputDirBrowseView.button.on_click = self.on_click_input_dir_browse_button
        self.mainView.settingsView.outputDirBrowseView.button.on_click = self.on_click_output_dir_browse_button
        self.mainView.inspectionView.controlButtonsView.stopButton.on_click = self.on_click_stop_button
        self.mainView.inspectionView.controlButtonsView.startButton.on_click = self.on_click_start_button
        self.mainView.inspectionView.controlButtonsView.outputButton.on_click = self.on_click_output_button

    def on_click_input_dir_browse_button(self, event):
        print("Input Dir Browse Button Clicked")

    def on_click_output_dir_browse_button(self, event):
        print("Output Dir Browse Button Clicked")

    def on_click_stop_button(self, event):
        print("Stop Button Clicked")

    def on_click_start_button(self, event):
        print("Start Button Clicked")

    def on_click_output_button(self, event):
        print("Output Button Clicked")


