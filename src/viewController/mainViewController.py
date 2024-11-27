from src.view.main.mainView import MainView

from src.model.homeModel import HomeModel
from src.model.inspectionModel import InspectionModel
from src.model.settingsModel import SettingsModel

class MainViewController:
    def __init__(self):
        self.mainView = MainView()
        self.homeModel = HomeModel()
        self.inspectionModel = InspectionModel()
        self.settingsModel = SettingsModel()

        self.set_components_value()

        self.events_handler()

        self.mainView.loop()

    def events_handler(self):
        self.mainView.settingsView.inputDirBrowseView.button.on_click = self.on_click_input_dir_browse_button
        self.mainView.settingsView.outputDirBrowseView.button.on_click = self.on_click_output_dir_browse_button
        self.mainView.inspectionView.controlButtonsView.stopButton.on_click = self.on_click_stop_button
        self.mainView.inspectionView.controlButtonsView.startButton.on_click = self.on_click_start_button
        self.mainView.inspectionView.controlButtonsView.outputButton.on_click = self.on_click_output_button
        self.mainView.inspectionView.localizationView.progressView.countUpButton.on_click = self.on_click_count_up_button
        self.mainView.inspectionView.localizationView.progressView.countDownButton.on_click = self.on_click_count_down_button
        self.mainView.inspectionView.localizationView.progressView.okButton.on_click = self.on_click_ok_button
        self.mainView.inspectionView.localizationView.gestureDetector.on_pan_start = self.on_click_localization_view
        self.mainView.inspectionView.localizationView.gestureDetector.on_pan_update = self.on_drag_localization_view
        self.mainView.settingsView.inputDirBrowseView.textField.on_blur = self.on_finish_editing_input_dir_textField
        self.mainView.settingsView.outputDirBrowseView.textField.on_blur = self.on_finish_editing_input_dir_textField
        self.mainView.settingsView.subjectNameTextField.on_blur = self.on_finish_editing_input_dir_textField
        self.mainView.settingsView.experimentNameTextField.on_blur = self.on_finish_editing_input_dir_textField
        self.mainView.inspectionView.audio.on_seek_complete = self.on_seek_complete_audio

    def on_click_input_dir_browse_button(self, event):
        print("Input Dir Browse Button Clicked")

    def on_click_output_dir_browse_button(self, event):
        print("Output Dir Browse Button Clicked")

    def on_click_stop_button(self, event):
        print("Stop Button Clicked")
        self.finish_inspection()
        self.update_mainView()

    def on_click_start_button(self, event):
        print("Start Button Clicked")
        self.start_inspection()
        self.update_mainView()

    def on_click_output_button(self, event):
        print("Output Button Clicked")
        self.output_results_to_csv()        

    def on_click_count_up_button(self, event):
        print("Count Up Button Clicked")
        self.change_sound_count(1)
        self.update_mainView()

    def on_click_count_down_button(self, event):
        print("Count Down Button Clicked")
        self.change_sound_count(-1)
        self.update_mainView()

    def on_click_ok_button(self, event):
        print("OK Button Clicked")
        self.save_pointer_angle() 
        self.continue_inspection()
        self.update_mainView()

    def on_click_localization_view(self, event):
        mouseX, mouseY = event.local_x, event.local_y
        self.move_pointer(mouseX, mouseY)
        self.update_mainView()

    def on_drag_localization_view(self, event):
        mouseX, mouseY = event.local_x, event.local_y
        self.move_pointer(mouseX, mouseY)
        self.update_mainView()

    def on_finish_editing_input_dir_textField(self, event):
        print("Input Dir TextField Edited")
        value = self.get_input_dir()
        self.set_settings_input_dir(value)
        self.refresh_sound_count()

    def on_finish_editing_output_dir_textField(self, event):
        print("Output Dir TextField Edited")
        value = self.get_output_dir()
        self.set_settings_output_dir(value)

    def on_finish_editing_subject_name_textField(self, event):
        print("Subject Name TextField Edited")
        value = self.get_subject_name()
        self.set_settings_subject_name(value)   

    def on_finish_editing_experiment_name_textField(self, event):
        print("Experiment Name TextField Edited")
        value = self.get_experiment_name()
        self.set_settings_experiment_name(value)
    
    def on_seek_complete_audio(self, event):
        print("Audio Seek Completed")
        current_position = self.get_inspectionView_audio_current_position()
        if current_position == 0:
            self.on_finish_audio_play()

    def on_finish_audio_play(self):
        print("Audio Finished Playing")
        self.switch_progressView_okButton_availability(True)
        self.init_localizationView_pointer_position()   
        self.display_localizationView_pointer()
        self.update_mainView()  

    # private
    def get_angle(self):
        circle_center = self.get_localizationView_circle_center()
        pointer_center = self.get_localizationView_pointer_position()
        angle = self.calculate_angle(circle_center[0], circle_center[1], pointer_center[0], pointer_center[1])
        return self.change_angle_anchor(angle, 270)
    
    def set_components_value(self):
        self.set_input_dir(self.get_settings_input_dir())
        self.set_output_dir(self.get_settings_output_dir())
        self.set_subject_name(self.get_settings_subject_name())
        self.set_experiment_name(self.get_settings_experiment_name())
        self.set_localizationView_scale_distance(self.get_settings_scale_distance())
        self.refresh_sound_count()
    
    def refresh_sound_count(self):
        initCount = self.get_settings_init_sound_count()
        fileCount = len(self.get_sounds_file_names())
        soundCount = self.refresh_count(fileCount, initCount)
        self.set_progressView_count(soundCount)
    
    def change_sound_count(self, value:int):
        upperLimit = len(self.get_sounds_file_names())
        count = self.get_progressView_count()
        count = self.change_count(count, value, upperLimit)
        self.set_progressView_count(count)

    def move_pointer(self, mouseX:int, mouseY:int):
        circle_center = self.get_localizationView_circle_center()
        circle_radius = self.get_localizationView_circle_radius()
        x, y = self.calculate_intersection_point(circle_center[0], circle_center[1], circle_radius, mouseX, mouseY)
        self.move_localizationView_pointer(x, y)
    def save_pointer_angle(self):
        pointerAngle = self.get_angle()
        self.save_inspection_result(pointerAngle)

    def start_inspection(self):
        print("Inspection Started")
        if self.get_inspection_has_started(): return
        soundFileNames = self.get_sounds_file_names()
        self.set_inspection_has_started(True)
        self.switch_progressView_count_button_availability(False)
        self.remove_inspection_data()
        self.set_inspection_soundFileNames(soundFileNames)
        self.continue_inspection()

    def continue_inspection(self):
        print("Inspection Continued")
        count = self.get_progressView_count()
        if count == 0: 
            self.finish_inspection()
            return
        print("play sound")
        soundFileName = self.pop_inspection_sound_file_name() 
        self.dismiss_localizationView_pointer()
        self.switch_progressView_okButton_availability(False)
        self.set_inspectionView_audio_src(soundFileName)
        self.set_progressView_count(count-1)
        self.play_inspection_audio()
    
    def finish_inspection(self):
        print("Inspection Finished")
        self.refresh_sound_count()
        self.switch_progressView_okButton_availability(False)
        self.switch_progressView_count_button_availability(True)
        self.dismiss_localizationView_pointer()
        self.set_inspection_has_started(False)
    
    def output_results_to_csv(self):
        print("Output Results to CSV")
        outputDirPath = self.get_output_dir()
        subjectName = self.get_subject_name()
        experimentName = self.get_experiment_name()
        fileName = f"{subjectName}_{experimentName}"
        self.inspectionModel.output_results_to_csv(outputDirPath, fileName)

    # external
    ## homeModel
    def calculate_intersection_point(self, centerX:int, centerY:int, radius:int, x:int, y:int):
        return self.homeModel.calculate_intersection_point(centerX, centerY, radius, x, y)
    def calculate_angle(self, centerX:int, centerY:int, x:int, y:int):
        return self.homeModel.calculate_angle(centerX, centerY, x, y)
    def change_angle_anchor(self, angle:int, anchor:int):
        return self.homeModel.change_angle_anchor(angle, anchor)
    def get_sounds_file_names(self):     
        dirPath = self.get_input_dir()
        return self.homeModel.get_sounds_file_names(dirPath)
    def refresh_count(self, fileCount:int, initCount:int):
        return self.homeModel.refresh_count(fileCount, initCount)
    def change_count(self, count:int, value:int, upperLimit:int):   
        return self.homeModel.change_count(count, value, upperLimit)
    
    ## settingsModel
    def get_settings_input_dir(self): return self.settingsModel.get_input_dir_path()
    def get_settings_output_dir(self): return self.settingsModel.get_output_dir_path()
    def get_settings_subject_name(self): return self.settingsModel.get_subject_name()
    def get_settings_experiment_name(self): return self.settingsModel.get_experiment_name()
    def get_settings_scale_distance(self): return self.settingsModel.get_scale_distance()
    def get_settings_init_sound_count(self): return self.settingsModel.get_init_sound_count()

    def set_settings_input_dir(self, value:str): self.settingsModel.set_input_dir_path(value)
    def set_settings_output_dir(self, value:str): self.settingsModel.set_output_dir_path(value)
    def set_settings_subject_name(self, value:str): self.settingsModel.set_subject_name(value)
    def set_settings_experiment_name(self, value:str): self.settingsModel.set_experiment_name(value)

    ## inspectionModel
    def set_inspection_soundFileNames(self, soundFileNames:list): self.inspectionModel.set_soundFileNames(soundFileNames)
    def get_inspection_has_started(self): return self.inspectionModel.get_has_started()
    def set_inspection_has_started(self, value:bool): self.inspectionModel.set_has_started(value)
    def remove_inspection_data(self): self.inspectionModel.remove_data()
    def pop_inspection_sound_file_name(self): return self.inspectionModel.pop_sound_file_name()
    def save_inspection_result(self, answer:int): self.inspectionModel.save_result(answer)
    
    ## mainView
    def update_mainView(self):
        self.mainView.update()

    ### settingsView
    def get_settingsView(self):
        return self.mainView.settingsView
    
    def get_input_dir(self):
        view = self.get_settingsView()
        return view.get_input_dir()
    
    def get_output_dir(self):
        view = self.get_settingsView()
        return view.get_output_dir()
    
    def get_subject_name(self):
        view = self.get_settingsView()
        return view.get_subject_name()
    
    def get_experiment_name(self):
        view = self.get_settingsView()
        return view.get_experiment_name()
    
    def set_input_dir(self, value:str):
        view = self.get_settingsView()
        view.set_input_dir(value)

    def set_output_dir(self, value:str):

        view = self.get_settingsView()
        view.set_output_dir(value)

    def set_subject_name(self, value:str):
        view = self.get_settingsView()
        view.set_subject_name(value)

    def set_experiment_name(self, value:str):
        view = self.get_settingsView()
        view.set_experiment_name(value)
        
    ### inspectionView
    def get_inspectionView(self):
        return self.mainView.inspectionView
    def get_inspectionView_audio_current_position(self):
        view = self.get_inspectionView()
        return view.get_audio_current_position()
    
    def set_inspectionView_audio_src(self, src:str):
        view = self.get_inspectionView()
        view.set_audio_src(src)
    
    def play_inspection_audio(self):
        view = self.get_inspectionView()
        view.play_audio()

    #### localizationView
    def get_localizationView(self):
        return self.mainView.inspectionView.localizationView
    
    def get_localizationView_circle_radius(self):
        view = self.get_localizationView()
        return view.get_circle_radius()
    
    def get_localizationView_circle_center(self):
        view = self.get_localizationView()
        return view.get_circle_center()
    
    def get_localizationView_pointer_position(self):
        view = self.get_localizationView()
        return view.get_pointer_position()
    
    def set_localizationView_scale_distance(self, distance:int):
        view = self.get_localizationView()
        view.set_scale_distance(distance)
    
    def move_localizationView_pointer(self, x:int, y:int):
        view = self.get_localizationView()
        view.set_pointer_position(x, y)

    def display_localizationView_pointer(self):
        view = self.get_localizationView()
        view.display_pointer()    

    def dismiss_localizationView_pointer(self):
        view = self.get_localizationView()
        view.dismiss_pointer()

    def init_localizationView_pointer_position(self):
        view = self.get_localizationView()
        view.init_pointer_position()

    ##### progressView
    def get_progressView(self):
        view = self.get_localizationView()
        return view.progressView
    
    def get_progressView_count(self):
        view = self.get_progressView()
        return view.get_count()

    def set_progressView_count(self, count:int):
        view = self.get_progressView()
        view.set_count(count)

    def switch_progressView_okButton_availability(self, isAvailable:bool):
        view = self.get_progressView()
        view.switch_ok_button_availability(isAvailable)

    def switch_progressView_count_button_availability(self, isAvailable:bool):
        view = self.get_progressView()
        view.switch_count_button_availability(isAvailable)
