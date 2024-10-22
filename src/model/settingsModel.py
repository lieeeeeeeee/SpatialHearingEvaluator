import json

class SettingsModel:
    JSON_FILE_NAME = "settings.json"
    JSON_FILE_PATH_DIR = "materials/"
    JSON_FILE_PATH = JSON_FILE_PATH_DIR + JSON_FILE_NAME
    

    def __init__(self):
        self.initSettings = {
            "inputDirPath": "materials/sounds/input/",
            "outputDirPath": "materials/sounds/output/",
            "subjectName": "subject name",  
            "experimentName": "experiment",
            "scaleDistance": 30,
        }
        self.settings = None
        self.load()

    def get_input_dir_path(self): return self.settings["inputDirPath"]
    def get_output_dir_path(self): return self.settings["outputDirPath"]
    def get_subject_name(self): return self.settings["subjectName"]
    def get_experiment_name(self): return self.settings["experimentName"]
    def get_scale_distance(self): return self.settings["scaleDistance"]

    def set_input_dir_path(self, inputDirPath): 
        self.settings["inputDirPath"] = inputDirPath
        self.save()

    def set_output_dir_path(self, outputDirPath): 
        self.settings["outputDirPath"] = outputDirPath
        self.save()

    def set_subject_name(self, subjectName): 
        self.settings["subjectName"] = subjectName
        self.save()

    def set_experiment_name(self, experimentName): 
        self.settings["experimentName"] = experimentName
        self.save()
    

    def save(self):
        print("save")
        with open(self.JSON_FILE_PATH, "w") as f:
            json.dump(self.settings, f, indent=4)

    def load(self):
        try:
            with open(self.JSON_FILE_PATH, "r") as f:
                self.settings = json.load(f)
        except Exception as e:
            print(e)
            self.settings = self.initSettings
            self.save()