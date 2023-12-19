import tkinter as tk

class WindowSizeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Size App")

        # Label to display window size
        self.size_label = tk.Label(root, text="")
        self.size_label.pack(pady=10)

        # Bind the Configure event to update size dynamically
        self.root.bind("<Configure>", self.update_size)

        # Bind the Shift key press event to resize with a fixed ratio
        self.root.bind("<Shift-Key>", self.resize_with_ratio)

        # Set initial size
        self.update_size()

        # Get and display the maximum screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.size_label.config(text=f"Max Screen Size: {screen_width} x {screen_height}")

    def update_size(self, event=None):
        # Get the current window size
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Display the window size in the label
        self.size_label.config(text=f"Window Size: {width} x {height}")

    def resize_with_ratio(self, event):
        # Resize the window with a fixed ratio when Shift key is pressed
        current_width = self.root.winfo_width()
        current_height = self.root.winfo_height()

        # Set the desired ratio (you can modify this as needed)
        ratio = 0.8  # For example, resize to 80% of the current size

        new_width = int(current_width * ratio)
        new_height = int(current_height * ratio)

        # Resize the window
        self.root.geometry(f"{new_width}x{new_height}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowSizeApp(root)
    root.mainloop()

