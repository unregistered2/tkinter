import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=5)

first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(
    user_info_frame,
    values=[
        "",
        "Mr.",
        "Ms.",
        "Dr.",
    ],
)
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=0, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(
    user_info_frame,
    values=[
        "Africa",
        "Antarctica",
        "Asia",
        "Europe",
        "North America",
        "Oceania",
        "South America",
    ],
)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1, sticky="news", padx=20, pady=20)

registered_label = tk.Label(courses_frame, text="Registration Status")
registered_check = tk.Checkbutton(courses_frame, text="Currently Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="# of Completed Courses")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=0)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_frame, text="# of Semesters")
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=0)
numsemesters_spinbox.grid(row=1, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=5)

terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.")
terms_check.grid(row=0, column=0)

button = tk.Button(frame, text="Enter Data")
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()
