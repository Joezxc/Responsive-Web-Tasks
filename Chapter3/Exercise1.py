import tkinter as tk

# Create a function that greet the users
def greet_user():
    user_name = entry.get()
    greeting_label.config(text=f"Hello, {user_name}! Welcome to the Greeting App.")

# Declare a root.title that has a greeting app
root = tk.Tk()
root.title("Greeting App")

# Create a function that greet the users
def create_frames():
    # Here is the InputFrame
    input_frame = tk.Frame(root)
    input_frame.pack()

    entry_label = tk.Label(input_frame, text="Enter your name: ")
    entry_label.pack(side="left")

    global entry
    entry = tk.Entry(input_frame)
    entry.pack(side="left")

    greet_button = tk.Button(input_frame, text="Greet", command=greet_user)
    greet_button.pack(side="left")

    # Here is the DisplayFrame
    global greeting_label
    display_frame = tk.Frame(root)
    display_frame.pack()

    greeting_label = tk.Label(display_frame, text="Enter your name and click 'Greet' to get a welcome message!")
    greeting_label.pack()

create_frames()

root.mainloop()