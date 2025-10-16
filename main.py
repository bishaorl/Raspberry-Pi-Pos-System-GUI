import matplotlib
matplotlib.use('Agg')

from tkinter import *
from utils.settings import Settings
from utils.frame import frameSettings

class POS(Settings, frameSettings):
    def __init__(self, root):
        self.root = root
        self.load_configs()
        
        self.create_vaiables()
        self.set_all_button_fonts(('Arial', 24, 'normal'))
        self.set_all_label_fonts(('Arial', 20, 'normal'))
        self.set_all_frames()

if __name__ == '__main__':
    root = Tk()
    app = POS(root)
    root.mainloop()
    