import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import datetime

root = tk.Tk()
root.title("Journal App")
root.eval("tk::PlaceWindow . center")


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def update_text(*args):
    text_widget.delete(1.0, tk.END)  # Clear the existing text in the ScrolledText widget
    text_widget.insert(tk.END, string_var.get())


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    tk.Label(frame1,
             text="Enter your name here",
             bg="white",
             fg="black",
             font=("TkHeadingFont", 15)
             ).pack(pady=20)

    global name
    name = tk.StringVar()

    tk.Entry(frame1,
             textvariable=name,
             width=15,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack()

    tk.Label(frame1,
             text="Enter today's date: ",
             bg="white",
             fg="black",
             font=("TkHeadingFont", 15)
             ).pack()

    global date
    date = tk.StringVar()

    tk.Entry(frame1,
             textvariable=date,
             width=15,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack()

    tk.Label(frame1,
             text="Rate your day on a scale of 1-10",
             bg="white",
             fg="black",
             font=("TkHeadingFont", 15)
             ).pack()

    global rating
    rating = tk.StringVar()

    tk.Entry(frame1,
             textvariable=rating,
             width=15,
             font=('calibre', 20, 'normal'),
             justify="center"
             ).pack()

    tk.Button(frame1,
              text="Enter",
              font=("TkHeadingFont", 14),
              bg="black",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame2()
              ).pack(pady=20)


def save_entry():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    f = open(f"{name.get()}'s journal - {date.get()}.txt", 'a')
    f.write(f"{name.get()}\n")
    f.write(f"Date: {date.get()}\n")
    f.write(f"Time: {formatted_time}\n")
    f.write(f"Today's Rating: {rating.get()}\n")
    f.write(text_entry.get('1.0', 'end'))
    file_path = os.path.abspath(f"{name.get(), datetime.datetime.now()}.txt")
    tk.Label(frame2,
             text=f"Your journal has been created at {file_path}",
             bg="white",
             fg="black",
             font=("TkHeadingFont", 15)
             ).pack()


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    tk.Label(frame2,
             text="Describe your day",
             bg="white",
             fg="black",
             font=("TkHeadingFont", 15)
             ).pack(pady=10)

    # Create a frame to hold the Text widget and scrollbar
    text_frame = tk.Frame(frame2)
    text_frame.pack(padx=10, pady=10, fill='both', expand=True)

    global text_entry
    text_entry = tk.Text(text_frame, height=10, width=50, wrap="word", font=("Arial", 12))
    text_entry.pack(side='left', fill='both', expand=True)

    # Add a vertical scrollbar
    scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=text_entry.yview)
    scrollbar.pack(side='right', fill='y')
    text_entry.configure(yscrollcommand=scrollbar.set)

    # Add a Save button below the text entry
    save_button = tk.Button(frame2, text='Save', command=save_entry)
    save_button.pack(pady=5)

    # Add a Quit button below the Save button
    quit_button = tk.Button(frame2, text='Quit', command=frame2.quit)
    quit_button.pack(pady=5)


frame1 = tk.Frame(root, width=600, height=600, bg="white")
frame2 = tk.Frame(root, width=600, height=600, bg="white")


for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()
root.mainloop()
