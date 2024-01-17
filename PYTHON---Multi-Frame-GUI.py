import tkinter as tk

def raise_frame(frame):
    frame.tkraise()

def main_app():
    root = tk.Tk()
    root.title("Main Window")

    # Creating frames for each set of options
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)

    for frame in (frame1, frame2, frame3):
        frame.grid(row=0, column=0, sticky='news')

    # Options for frame 1
    tk.Label(frame1, text="Frame 1").grid()
    tk.Button(frame1, text="Option 1A").grid()
    tk.Button(frame1, text="Option 1B").grid()
    tk.Button(frame1, text="Option 1C").grid()

    # Options for frame 2
    tk.Label(frame2, text="Frame 2").grid()
    tk.Button(frame2, text="Option 2A").grid()
    tk.Button(frame2, text="Option 2B").grid()
    tk.Button(frame2, text="Option 2C").grid()

    # Options for frame 3
    tk.Label(frame3, text="Frame 3").grid()
    tk.Button(frame3, text="Option 3A").grid()
    tk.Button(frame3, text="Option 3B").grid()
    tk.Button(frame3, text="Option 3C").grid()

    # Buttons for the main window to raise each frame
    tk.Button(root, text="Open Frame 1", command=lambda: raise_frame(frame1)).grid(row=1, column=0)
    tk.Button(root, text="Open Frame 2", command=lambda: raise_frame(frame2)).grid(row=2, column=0)
    tk.Button(root, text="Open Frame 3", command=lambda: raise_frame(frame3)).grid(row=3, column=0)

    raise_frame(frame1)  # Show the first frame initially

    root.mainloop()

# Run the application
main_app()
