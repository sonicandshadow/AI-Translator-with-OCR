#获得屏幕区域与截图的实现
import pyautogui
import tkinter as tk
from PIL import ImageGrab
class SelectArea:
    def __init__(self, root):
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.geometry(f'{width}x{height}')
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<ButtonPress-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Create a rectangle to show selection area
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        # Update the coordinates of the rectangle
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        # Get final coordinates
        end_x, end_y = event.x, event.y
        self.root.quit() # Close the Tkinter window

        # Return the selected area
        self.selected_area = (self.start_x, self.start_y, end_x, end_y)


def get_screen_zone():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-alpha', 0.25)
    TRANSCOLOUR = 'gray'
    root.configure(background='gray')
    selector = SelectArea(root)
    root.mainloop()
    root.destroy()
    return selector.selected_area
    # print(selector.selected_area)
    # screenshot = ImageGrab.grab(selector.selected_area)
    # screenshot.save("image.png")


def get_screenshot(selected_zone):
    screenshot = ImageGrab.grab(selected_zone)
    screenshot.save("image.png")