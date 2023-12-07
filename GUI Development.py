import tkinter as tk

# Create a basic GUI window
window = tk.Tk()
window.title('My GUI')
window.geometry('300x200')

# Add a label to the window
label = tk.Label(window, text='Hello, World!')
label.pack()

# Add a button to the window
button = tk.Button(window, text='Click me!')
button.pack()

# Start the GUI event loop
window.mainloop()
