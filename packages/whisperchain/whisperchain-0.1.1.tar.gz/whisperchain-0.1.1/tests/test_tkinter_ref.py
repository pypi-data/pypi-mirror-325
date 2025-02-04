import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()

# Set the window dimensions (width and height)
window_width = 1024
window_height = 1024

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the geometry of the window and remove borders
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.overrideredirect(True)  # Makes the window borderless

# Set a custom icon
try:
    icon = Image.open("assets/mic.png")
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(True, photo)

    # Configure transparency
    # root.attributes("-alpha", 0.0)  # Make window fully transparent
    # root.config(bg="systemTransparent")  # For macOS

    # Create label with image instead of text
    label = tk.Label(root, image=photo, bg="white")
    label.image = photo  # Keep a reference to prevent garbage collection
    label.pack(expand=True, fill="both")

    # root.attributes("-alpha", 1.0)
except Exception as e:
    print(f"Icon could not be set: {e}")

# Run the application
root.mainloop()
