import tkinter as tk

class WindowSizeApp:
    def __init__(self, root):
        # Aspect ratio options
        self.selected_aspect_ratio = tk.StringVar()
        self.aspect_ratios = ["16:9", "4:3", "1:1"]
        self.selected_aspect_ratio.set(self.aspect_ratios[0])
        
        # Title
        self.root = root
        self.root.title("Window Size Visualizer")

        # Fixed Initial Width at start
        initial_width = 800
        initial_height = 400
        self.root.geometry(f"{initial_width}x{initial_height}")

        # UI Labels
        self.title_label = tk.Label(root, text="Window Size Visualizer", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)
        
        self.size_display_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.size_display_label.pack(pady=5)

        self.how_to_use_label = tk.Label(root, text="How to Use", font=("Helvetica", 12, "underline"), fg="blue", cursor="hand2")
        self.how_to_use_label.pack(pady=5)
        self.how_to_use_label.bind("<Button-1>", self.open_instructions)

        self.aspect_ratio_setter_label = tk.Label(root, text="Aspect Ratio Setter", font=("Helvetica", 16, "bold"))
        self.aspect_ratio_setter_label.pack(pady=10)
        
        # OptionMenu for Aspect Ratio changing
        self.aspect_ratio_option_menu = tk.OptionMenu(root, self.selected_aspect_ratio, *self.aspect_ratios, command=self.resize_to_aspect_ratio)
        self.aspect_ratio_option_menu.config(font=("Helvetica", 12))
        self.aspect_ratio_option_menu.pack(pady=10)
        
        self.selected_aspect_ratio.set(self.aspect_ratios[0])

        # Updating of displayed window size
        self.root.bind("<Configure>", self.update_size)
        self.update_size()
        
        # Centering of UI while window is resized
        self.center_elements()

    def center_elements(self):
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")
        self.how_to_use_label.place(relx=0.5, rely=0.4, anchor="center")
        self.size_display_label.place(relx=0.5, rely=0.5, anchor="center")
        self.aspect_ratio_setter_label.place(relx=0.5, rely=0.6, anchor="center")
        self.aspect_ratio_option_menu.place(relx=0.5, rely=0.7, anchor="center")    
        
    # Displaying of new window size func
    def update_size(self, event=None):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        self.size_display_label.config(text=f"{width} x {height}")

    # Instructions displaying
    def open_instructions(self, event=None):
        instructions = """Drag any corner or edge of the program's window until you reach your desired window size for visualizing. \n\n(Optional) Use the Aspect Ratio Setter dropdown menu to change the current window size to that aspect ratio."""
        tk.messagebox.OK
        tk.messagebox.showinfo("How to Use", instructions)

    # Resizing to chosen aspect ratio    
    def resize_to_aspect_ratio(self, *args):
        selected_ratio = self.selected_aspect_ratio.get()
        width, height = map(int, selected_ratio.split(":"))
        current_width = self.root.winfo_width()
        new_height = int((height / width) * current_width)

        self.root.geometry(f"{current_width}x{new_height}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowSizeApp(root)
    root.mainloop()