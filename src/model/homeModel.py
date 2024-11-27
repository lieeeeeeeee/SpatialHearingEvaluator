import math
import os

class HomeModel:
    def __init__(self):
        self.soundCount = 0

    # public
    def calculate_intersection_point(self, centerX, centerY, radius, x, y):
        dx, dy = x - centerX, y - centerY
        distance = math.sqrt(dx**2 + dy**2)
        unitX, unitY = dx/distance, dy/distance
        return centerX + unitX*radius, centerY + unitY*radius
    
    def calculate_angle(self, centerX, centerY, x, y):
        dx, dy = x - centerX, y - centerY
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        angle_deg = (angle_deg + 360) % 360
        return angle_deg
    
    def refresh_count(self, fileCount, initCount):
        if self.soundCount == 0: self.soundCount = initCount
        count = fileCount if fileCount < self.soundCount else self.soundCount
        return count
    
    def change_count(self, count, value, upperLimit):
        c = count + value
        lowerLimit = 0
        if c < lowerLimit: c = lowerLimit
        if upperLimit < c: c = upperLimit
        self.soundCount = c
        return c
    
    def change_angle_anchor(self, angle, anchor):
        return (angle - anchor) % 360
    
    def get_sounds_file_names(self, dirPath):
        soundFileNames = []
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                if file.endswith(".wav"):
                    soundFileNames.append(os.path.join(root, file))
        return soundFileNames