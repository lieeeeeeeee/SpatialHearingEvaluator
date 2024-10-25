import os
import sys
import random
import re

class InspectionModel:
    def __init__(self):
        self.hasStarted = False
        self.soundFileNames = []
        self.results = []
        self.popedSoundFileName = None
    
    def sort_results(self):
        self.results.sort(key=lambda x: x[0])
        return self.results
    def extract_angle_from_sound_file_name(self, soundFileName: str):
        pattern = r'\d{3}'
        matches = re.findall(pattern, soundFileName)
        return int(matches[-1]) if matches else None
    
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
        solution = self.extract_angle_from_sound_file_name(self.popedSoundFileName)
        if solution == None: solution = -1
        self.results.append((solution, answer))

    def remove_data(self):
        self.soundFileNames = []
        self.results = []
        self.popedSoundFileName = None

    def output_results_to_csv(self, outputDirPath: str, fileName: str):
        if fileName == "_": fileName = "result"

        path = outputDirPath + fileName 
        results = self.sort_results()
        # もし同じファイル名が存在する場合は名前の後ろに数字をつける
        if os.path.exists(path):
            i = 1
            while True:
                path = outputDirPath + fileName + f"_{i}"
                if not os.path.exists(path): break
                i += 1

        path = path + ".csv"

        with open(path, "w") as f:
            f.write("solution,answer\n")
            for a in results:
                f.write(f"{a[0]},{a[1]}\n")