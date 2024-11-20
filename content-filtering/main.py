import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
import numpy as np
from numpy.linalg import norm

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

root = ck.CTk()
root.geometry("400x300")

count = 0

timeframe1_var = tk.BooleanVar(value=False)
timeframe2_var = tk.BooleanVar(value=False)
timeframe3_var = tk.BooleanVar(value=False)
timeframe4_var = tk.BooleanVar(value=False)
timeframe5_var = tk.BooleanVar(value=False)
timeframe6_var = tk.BooleanVar(value=False)
grades1_var = tk.BooleanVar(value=False)
grades2_var = tk.BooleanVar(value=False)
grades3_var = tk.BooleanVar(value=False)
grades4_var = tk.BooleanVar(value=False)
grades5_var = tk.BooleanVar(value=False)
grades6_var = tk.BooleanVar(value=False)
problem1_var = tk.BooleanVar(value=False)
problem2_var = tk.BooleanVar(value=False)
problem3_var = tk.BooleanVar(value=False)
problem4_var = tk.BooleanVar(value=False)
problem5_var = tk.BooleanVar(value=False)
problem6_var = tk.BooleanVar(value=False)

user_inputs = [
    ['Dummy1', True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    ['Dummy2', False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True],
    ['Dummy3', True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True],
    ['Dummy4', False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False],
    ['Dummy5', True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False],
    ['Dummy6', False, True, True, False, False, True, True, False, False, True, True, False, False, True, True, False, False, True],
    ['Dummy7', True, True, True, False, False, False, True, True, True, False, False, False, True, True, True, False, False, False],
    ['Dummy8', False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, True, True, True],
    ['Dummy9', True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    ['Dummy10', False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
]

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

    print_user_data()
    reset_variables()

    # if count == 4:
    new_frame = ck.CTkFrame(master=root)
    new_frame.pack(pady=10, padx=10, fill="both", expand=True)
    label = ck.CTkLabel(master=new_frame, text="Search for a bouldering partner!")
    label.pack(pady=12, padx=10)
    global entry2
    entry2 = ck.CTkEntry(master=new_frame, placeholder_text="Input Name")
    entry2.pack(pady=12, padx=10)
    button1 = ck.CTkButton(master=new_frame, text="Find a Partner", hover_color="green", command=find_partner)
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

def print_user_data():
    print("Currently saved users: ")
    for user_data in user_inputs:
        print(f"{user_data[0]}: {user_data}")
    
def reset_variables():
    entry1.delete(0, tk.END)
    timeframe1_var.set(False)
    timeframe2_var.set(False)
    timeframe3_var.set(False)
    timeframe4_var.set(False)
    timeframe5_var.set(False)
    timeframe6_var.set(False)
    grades1_var.set(False)
    grades2_var.set(False)
    grades3_var.set(False)
    grades4_var.set(False)
    grades5_var.set(False)
    grades6_var.set(False)
    problem1_var.set(False)
    problem2_var.set(False)
    problem3_var.set(False)
    problem4_var.set(False)
    problem5_var.set(False)
    problem6_var.set(False)

def calculate_cosine_similarity(user_name):
    # Convert user data to vectors
    user_vectors = []
    target_vector = None
    for user_data in user_inputs:
        vector = [1 if val else 0 for val in user_data[1:]]
        user_vectors.append(vector)
        if user_data[0] == user_name:
            target_vector = vector
    
    if target_vector is None:
        print(f"No data found for user: {user_name}")
        return
    
    # Calculate cosine similarity between the target user and other users
    user_vectors = np.array(user_vectors)
    target_vector = np.array(target_vector)
    num_users = len(user_vectors)
    similarity_scores = []

    for i in range(num_users):
        if user_inputs[i][0] != user_name:
            similarity = np.dot(target_vector, user_vectors[i]) / (np.linalg.norm(target_vector) * np.linalg.norm(user_vectors[i]))
            similarity_scores.append((user_inputs[i][0], similarity))

    # Sort by similarity score in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    print(f"Cosine Similarity Scores for {user_name}:")
    for name, score in similarity_scores:
        print(f"{name}: {score}")

def find_partner():
    name = entry2.get()
    calculate_cosine_similarity(name)


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