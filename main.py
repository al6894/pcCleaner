import tkinter as tk
import subprocess
import os

def run_batch():
    # Path to the batch file
    batch_file = r"C:\Users\al334\Documents\VSCode\pcCleaner\test.bat"
    # Run the batch file
    subprocess.run(batch_file, shell=True)

# Create the main window
root = tk.Tk()
root.title("Delete %temp% Contents")

# Set window size
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Click to delete contents")
label.pack(pady=10)

# Add a button to run the batch file
button = tk.Button(root, text="Delete", command=run_batch, bg="red", fg="white")
button.pack(pady=20)

# Start the GUI loop
root.mainloop()