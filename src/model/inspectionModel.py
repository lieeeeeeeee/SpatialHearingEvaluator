import os
import sys
import random

class InspectionModel:
    SOUND_DATA_DIR_PATH  = "materials/sounds/stereo/"
    OUTPUT_DIR_PATH = "materials/sounds/output/"

    def __init__(self):
        self.hasStarted = False
        self.soundFileNames = []
        self.results = []
        self.popedSoundFileName = None

    
    
    def get_angle_from_sound_file_name(self, soundFileName: str):
        return int(soundFileName.split("_")[-1].split(".")[0])
    
    def sort_results(self):
        self.results.sort(key=lambda x: x[0])
        return self.results
    
    # public
    def set_soundFileNames(self, soundFileNames: list):
        self.soundFileNames = soundFileNames
        random.shuffle(self.soundFileNames)
        
    def get_has_started(self): return self.hasStarted
    def set_has_started(self, hasStarted: bool): self.hasStarted = hasStarted

    def pop_sound_file_name(self):
        self.popedSoundFileName = self.soundFileNames.pop(0)
        return self.popedSoundFileName
    
    def save_result(self, answer: int):
        solution = self.get_angle_from_sound_file_name(self.popedSoundFileName)
        self.results.append((solution, answer))

    def remove_data(self):
        self.soundFileNames = []
        self.results = []
        self.popedSoundFileName = None

    def output_results_to_csv(self):
        path = self.OUTPUT_DIR_PATH + "results.csv"
        results = self.sort_results()
        # もし同じファイル名が存在する場合は名前の後ろに数字をつける
        if os.path.exists(path):
            i = 1
            while True:
                path = self.OUTPUT_DIR_PATH + f"results_{i}.csv"
                if not os.path.exists(path): break
                i += 1

        with open(path, "w") as f:
            f.write("solution,answer\n")
            for a in results:
                f.write(f"{a[0]},{a[1]}\n")