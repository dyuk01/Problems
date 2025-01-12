unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Write your code here!
class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time
    
    def label(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.time)

bomb1 = Bomb(unlock_code, wire_color, seconds)
bomb1.label()
