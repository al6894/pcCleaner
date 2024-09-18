import tkinter as tk
import subprocess
import os

def run_batch():
    # Path to the batch file
    batch_file = r"C:\Users\al334\Documents\VSCode\pcCleaner\test.bat"
    subprocess.run(batch_file, shell=True)

# Create the main window
root = tk.Tk()
root.title("pcCleaner")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x and y to center the window
window_width = 400
window_height = 300
position_x = int(screen_width/2 - window_width/2)
position_y = int(screen_height/2 - window_height/2)

# Set the dimensions and position of the window
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

label = tk.Label(root, text="Click to delete contents")
label.pack(pady=10)

# Add a button to run the batch file
button = tk.Button(root, text="Delete", command=run_batch, bg="red", fg="white")
button.pack(pady=20)

# Start the GUI loop
root.mainloop()