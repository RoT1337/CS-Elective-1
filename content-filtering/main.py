import customtkinter as ck
import tkinter as tk
from tkinter import messagebox

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

root = ck.CTk()
root.geometry("400x300")

count = 0

timeframe1_var = tk.BooleanVar()
timeframe2_var = tk.BooleanVar()
timeframe3_var = tk.BooleanVar()
timeframe4_var = tk.BooleanVar()
timeframe5_var = tk.BooleanVar()
timeframe6_var = tk.BooleanVar()
grades1_var = tk.BooleanVar()
grades2_var = tk.BooleanVar()
grades3_var = tk.BooleanVar()
grades4_var = tk.BooleanVar()
grades5_var = tk.BooleanVar()
grades6_var = tk.BooleanVar()
problem1_var = tk.BooleanVar()
problem2_var = tk.BooleanVar()
problem3_var = tk.BooleanVar()
problem4_var = tk.BooleanVar()
problem5_var = tk.BooleanVar()
problem6_var = tk.BooleanVar()

user_inputs = []

def save_user_inputs():
    name = entry1.get()

    user_data = [
        name,
        timeframe1_var.get(),
        timeframe2_var.get(),
        timeframe3_var.get(),
        timeframe4_var.get(),
        timeframe5_var.get(),
        timeframe6_var.get(),
        grades1_var.get(),
        grades2_var.get(),
        grades3_var.get(),
        grades4_var.get(),
        grades5_var.get(),
        grades6_var.get(),
        problem1_var.get(),
        problem2_var.get(),
        problem3_var.get(),
        problem4_var.get(),
        problem5_var.get(),
        problem6_var.get()
    ]
    user_inputs.append(user_data)


def open_timeframe_window():
    global timeframe_window
    root.withdraw()
    timeframe_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = timeframe_window.winfo_screenwidth()
    screen_height = timeframe_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    timeframe_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    timeframe_window.title("Select Times")

    label = ck.CTkLabel(master=timeframe_window, text="Check the boxes of the times you are in the bouldering gym")
    label.pack(pady=12, padx=10)

    timeframe1 = ck.CTkCheckBox(master=timeframe_window, text="10:00 A.M. - 12:00 P.M.", variable=timeframe1_var)
    timeframe1.pack(pady=12, padx=10)

    timeframe2 = ck.CTkCheckBox(master=timeframe_window, text="12:00 P.M. - 2:00 P.M.", variable=timeframe2_var)
    timeframe2.pack(pady=12, padx=10)

    timeframe3 = ck.CTkCheckBox(master=timeframe_window, text="2:00 P.M. - 4:00 P.M.", variable=timeframe3_var)
    timeframe3.pack(pady=12, padx=10)

    timeframe4 = ck.CTkCheckBox(master=timeframe_window, text="4:00 P.M. - 6:00 P.M.", variable=timeframe4_var)
    timeframe4.pack(pady=12, padx=10)

    timeframe5 = ck.CTkCheckBox(master=timeframe_window, text="6:00 P.M. - 8:00 P.M.", variable=timeframe5_var)
    timeframe5.pack(pady=12, padx=10)

    timeframe6 = ck.CTkCheckBox(master=timeframe_window, text="8:00 P.M. - 10:00 P.M.", variable=timeframe6_var)
    timeframe6.pack(pady=12, padx=10)

    timeframe_button = ck.CTkButton(master=timeframe_window, text="Continue", command=open_grades_window)
    timeframe_button.pack(pady=12, padx=10)

def open_grades_window():
    global grades_window
    timeframe_window.destroy()
    grades_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = grades_window.winfo_screenwidth()
    screen_height = grades_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    grades_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    grades_window.title("Select Grades")

    label = ck.CTkLabel(master=grades_window, text="Check the boxes of your preferred climbing grades:")
    label.pack(pady=12, padx=10)

    grades1 = ck.CTkCheckBox(master=grades_window, text="V0-V1", variable=grades1_var)
    grades1.pack(pady=12, padx=10)

    grades2 = ck.CTkCheckBox(master=grades_window, text="V1-V2", variable=grades2_var)
    grades2.pack(pady=12, padx=10)

    grades3 = ck.CTkCheckBox(master=grades_window, text="V2-V3", variable=grades3_var)
    grades3.pack(pady=12, padx=10)

    grades4 = ck.CTkCheckBox(master=grades_window, text="V3-V4", variable=grades4_var)
    grades4.pack(pady=12, padx=10)

    grades5 = ck.CTkCheckBox(master=grades_window, text="V4-V5", variable=grades5_var)
    grades5.pack(pady=12, padx=10)

    grades6 = ck.CTkCheckBox(master=grades_window, text="V6 and beyond", variable=grades6_var)
    grades6.pack(pady=12, padx=10)

    grades_button = ck.CTkButton(master=grades_window, text="Continue", command=open_problems_window)
    grades_button.pack(pady=12, padx=10)

def open_problems_window():
    global problems_window
    grades_window.destroy()
    problems_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = problems_window.winfo_screenwidth()
    screen_height = problems_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    problems_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    problems_window.title("Select Problems")

    label = ck.CTkLabel(master=problems_window, text="Check the boxes of your preferred boulder problems:")
    label.pack(pady=12, padx=10)

    problem1 = ck.CTkCheckBox(master=problems_window, text="Overhangs", variable=problem1_var)
    problem1.pack(pady=12, padx=10)

    problem2 = ck.CTkCheckBox(master=problems_window, text="Slabs", variable=problem2_var)
    problem2.pack(pady=12, padx=10)

    problem3 = ck.CTkCheckBox(master=problems_window, text="Verticals", variable=problem3_var)
    problem3.pack(pady=12, padx=10)

    problem4 = ck.CTkCheckBox(master=problems_window, text="Arete", variable=problem4_var)
    problem4.pack(pady=12, padx=10)

    problem5 = ck.CTkCheckBox(master=problems_window, text="Dynamic / Dyno", variable=problem5_var)
    problem5.pack(pady=12, padx=10)

    problem6 = ck.CTkCheckBox(master=problems_window, text="Crimps", variable=problem6_var)
    problem6.pack(pady=12, padx=10)

    problems_button = ck.CTkButton(master=problems_window, text="Submit", command=finish)
    problems_button.pack(pady=12, padx=10)

def finish():
    global count
    problems_window.destroy()
    root.deiconify()
    count += 1

    save_user_inputs()
    messagebox.showinfo("Info", "User data saved")

    name = entry1.get()
    print_user_data(name)

    if count == 2:
        new_frame = ck.CTkFrame(master=root)
        new_frame.pack(pady=10, padx=10, fill="both", expand=True)
        label = ck.CTkLabel(master=new_frame, text="Search for a bouldering partner!")
        label.pack(pady=12, padx=10)
        entry2 = ck.CTkEntry(master=new_frame, placeholder_text="Input Name")
        entry2.pack(pady=12, padx=10)
        button1 = ck.CTkButton(master=new_frame, text="Find a Partner", hover_color="green")
        button1.pack(pady=12, padx=10)
        root.geometry("400x450")

def btn_continue():
    name = entry1.get()
    if name:
        open_timeframe_window()
    else:
        messagebox.showerror("Error", "Name cannot be empty")

def btn_exit():
    root.destroy()

def print_user_data(name):
    for user_data in user_inputs:
        if user_data[0] == name:
            print(f"Data for {name}: {user_data}")
            return
    print(f"No data found for user: {name}")

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

frame = ck.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

root.title("Bouldering Partner Finder")

entry1 = ck.CTkEntry(master=frame, placeholder_text="Input Your Name Here")
entry1.pack(pady=12, padx=10)

button = ck.CTkButton(master=frame, text="Continue", command=btn_continue)
button.pack(pady=12, padx=10)

exit_button = ck.CTkButton(master=frame, text="Exit", command=btn_exit, hover_color="red")
exit_button.pack(pady=12, padx=10)

root.mainloop()