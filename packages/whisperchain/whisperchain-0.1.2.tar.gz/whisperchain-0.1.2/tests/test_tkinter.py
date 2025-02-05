import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window dimensions (width and height)
window_width = screen_width
window_height = screen_height

# Calculate the position to center the window
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the geometry of the window and remove borders
root.geometry(f"{window_width}x{window_height}")
root.overrideredirect(True)  # Makes the window borderless

# Set a custom icon
try:
    icon = Image.open("assets/mic.png").convert("RGBA")
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(True, photo)
    
    # Configure transparency for macOS
    root.attributes("-alpha", 0.3)
    
    # Create canvas with transparent background
    canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0, bg="white")
    canvas.pack(expand=True, fill="both")
    
    # Display the image on canvas
    canvas.create_image(window_width//2, window_height//2, anchor="center", image=photo)
    canvas.image = photo  # Keep a reference to prevent garbage collection
except Exception as e:
    print(f"Icon could not be set: {e}")

# Run the application
root.mainloop()
