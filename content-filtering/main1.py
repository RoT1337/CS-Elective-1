import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
import numpy as np
from numpy.linalg import norm

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

root = ck.CTk()
root.geometry("400x300")

# count = 0

user_inputs = []

paladin_level_var = tk.StringVar()
warrior_level_var = tk.StringVar()
dark_knight_level_var = tk.StringVar()
gunbreaker_level_var = tk.StringVar()
ninja_level_var = tk.StringVar()
viper_level_var = tk.StringVar()
bard_level_var = tk.StringVar()
machinist_level_var = tk.StringVar()
dancer_level_var = tk.StringVar()
black_mage_level_var = tk.StringVar()
summoner_level_var = tk.StringVar()
red_mage_level_var = tk.StringVar()
white_mage_level_var = tk.StringVar()
scholar_level_var = tk.StringVar()
astrologian_level_var = tk.StringVar()
sage_level_var = tk.StringVar()

def validate_number_input(event):
    entry = event.widget
    value = entry.get()
    if not value.isdigit() and value != "":
        entry.delete(0, tk.END)
        entry.insert(0, ''.join(filter(str.isdigit, value)))

def open_tank_window():
    global tank_window
    root.withdraw()
    tank_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = tank_window.winfo_screenwidth()
    screen_height = tank_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    tank_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    tank_window.title("Tank Levels")

    label = ck.CTkLabel(master=tank_window, text="Input your Warrior of Light's Tank Levels")
    label.pack(pady=12, padx=10)

    paladin_level = ck.CTkEntry(master=tank_window, textvariable=paladin_level_var, placeholder_text="Paladin Level")
    paladin_level.pack(pady=12, padx=10)
    paladin_level.bind("<KeyRelease>", validate_number_input)

    warrior_level = ck.CTkEntry(master=tank_window, textvariable=warrior_level_var, placeholder_text="Warrior Level")
    warrior_level.pack(pady=12, padx=10)
    warrior_level.bind("<KeyRelease>", validate_number_input)

    dark_knight_level = ck.CTkEntry(master=tank_window, textvariable=dark_knight_level_var, placeholder_text="Dark Knight Level")
    dark_knight_level.pack(pady=12, padx=10)
    dark_knight_level.bind("<KeyRelease>", validate_number_input)

    gunbreaker_level = ck.CTkEntry(master=tank_window, textvariable=gunbreaker_level_var, placeholder_text="Gunbreaker Level")
    gunbreaker_level.pack(pady=12, padx=10)
    gunbreaker_level.bind("<KeyRelease>", validate_number_input)

    tank_button = ck.CTkButton(master=tank_window, text="Continue", command=open_meleedps_window)
    tank_button.pack(pady=12, padx=10)

def open_meleedps_window():
    global meleedps_window
    tank_window.destroy()
    meleedps_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = meleedps_window.winfo_screenwidth()
    screen_height = meleedps_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    meleedps_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    meleedps_window.title("Melee DPS Levels")

    label = ck.CTkLabel(master=meleedps_window, text="Input your Warrior of Light's Melee DPS Levels")
    label.pack(pady=12, padx=10)

    ninja_level = ck.CTkEntry(master=meleedps_window, textvariable=ninja_level_var, placeholder_text="Ninja Level")
    ninja_level.pack(pady=12, padx=10)
    ninja_level.bind("<KeyRelease>", validate_number_input)

    viper_level = ck.CTkEntry(master=meleedps_window, textvariable=viper_level_var, placeholder_text="Viper Level")
    viper_level.pack(pady=12, padx=10)
    viper_level.bind("<KeyRelease>", validate_number_input)

    meleedps_button = ck.CTkButton(master=meleedps_window, text="Submit", command=open_physrange_dps)
    meleedps_button.pack(pady=12, padx=10)

def open_physrange_dps():
    global physrange_window
    meleedps_window.destroy()
    physrange_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = physrange_window.winfo_screenwidth()
    screen_height = physrange_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    physrange_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    physrange_window.title("Physical Ranged DPS Levels")

    label = ck.CTkLabel(master=physrange_window, text="Input your Warrior of Light's Physical Ranged DPS Levels")
    label.pack(pady=12, padx=10)

    bard_level = ck.CTkEntry(master=physrange_window, textvariable=bard_level_var, placeholder_text="Bard Level")
    bard_level.pack(pady=12, padx=10)
    bard_level.bind("<KeyRelease>", validate_number_input)

    machinist_level = ck.CTkEntry(master=physrange_window, textvariable=machinist_level_var, placeholder_text="Machinist Level")
    machinist_level.pack(pady=12, padx=10)
    machinist_level.bind("<KeyRelease>", validate_number_input)

    dancer_level = ck.CTkEntry(master=physrange_window, textvariable=dancer_level_var, placeholder_text="Dancer Level")
    dancer_level.pack(pady=12, padx=10)
    dancer_level.bind("<KeyRelease>", validate_number_input)

    physrange_button = ck.CTkButton(master=physrange_window, text="Submit", command=open_magirange_dps)
    physrange_button.pack(pady=12, padx=10)

def open_magirange_dps():
    global magirange_window
    physrange_window.destroy()
    magirange_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = magirange_window.winfo_screenwidth()
    screen_height = magirange_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    magirange_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    magirange_window.title("Magical Ranged DPS Levels")

    label = ck.CTkLabel(master=magirange_window, text="Input your Warrior of Light's Magical Ranged DPS Levels")
    label.pack(pady=12, padx=10)

    black_mage_level = ck.CTkEntry(master=magirange_window, textvariable=black_mage_level_var, placeholder_text="Black Mage Level")
    black_mage_level.pack(pady=12, padx=10)
    black_mage_level.bind("<KeyRelease>", validate_number_input)

    summoner_level = ck.CTkEntry(master=magirange_window, textvariable=summoner_level_var, placeholder_text="Summoner Level")
    summoner_level.pack(pady=12, padx=10)
    summoner_level.bind("<KeyRelease>", validate_number_input)

    red_mage_level = ck.CTkEntry(master=magirange_window, textvariable=red_mage_level_var, placeholder_text="Red Mage Level")
    red_mage_level.pack(pady=12, padx=10)
    red_mage_level.bind("<KeyRelease>", validate_number_input)

    magirange_button = ck.CTkButton(master=magirange_window, text="Submit", command=open_healer_window)
    magirange_button.pack(pady=12, padx=10)

def open_healer_window():
    global healer_window
    magirange_window.destroy()
    healer_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 400
    screen_width = healer_window.winfo_screenwidth()
    screen_height = healer_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    healer_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    healer_window.title("Healer Levels")

    label = ck.CTkLabel(master=healer_window, text="Input your Warrior of Light's Healer Levels")
    label.pack(pady=12, padx=10)

    white_mage_level = ck.CTkEntry(master=healer_window, textvariable=white_mage_level_var, placeholder_text="White Mage Level")
    white_mage_level.pack(pady=12, padx=10)
    white_mage_level.bind("<KeyRelease>", validate_number_input)

    scholar_level = ck.CTkEntry(master=healer_window, textvariable=scholar_level_var, placeholder_text="Scholar Level")
    scholar_level.pack(pady=12, padx=10)
    scholar_level.bind("<KeyRelease>", validate_number_input)

    astrologian_level = ck.CTkEntry(master=healer_window, textvariable=astrologian_level_var, placeholder_text="Astrologian Level")
    astrologian_level.pack(pady=12, padx=10)
    astrologian_level.bind("<KeyRelease>", validate_number_input)

    sage_level = ck.CTkEntry(master=healer_window, textvariable=sage_level_var, placeholder_text="Sage Level")
    sage_level.pack(pady=12, padx=10)
    sage_level.bind("<KeyRelease>", validate_number_input)

    healer_button = ck.CTkButton(master=healer_window, text="Submit", command=finish)
    healer_button.pack(pady=12, padx=10)

def finish():
    global count
    meleedps_window.destroy()
    root.deiconify()
    #count += 1

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
        open_tank_window()
    else:
        messagebox.showerror("Error", "Name cannot be empty")

def btn_exit():
    root.destroy()

def save_user_inputs():
    name = entry1.get()

    user_data = [
        name,
        int(paladin_level_var.get() or 0),
        int(warrior_level_var.get() or 0),
        int(dark_knight_level_var.get() or 0),
        int(gunbreaker_level_var.get() or 0),
        int(ninja_level_var.get() or 0),
        int(viper_level_var.get() or 0),
        int(bard_level_var.get() or 0),
        int(machinist_level_var.get() or 0),
        int(dancer_level_var.get() or 0),
        int(black_mage_level_var.get() or 0),
        int(summoner_level_var.get() or 0),
        int(red_mage_level_var.get() or 0),
        int(white_mage_level_var.get() or 0),
        int(scholar_level_var.get() or 0),
        int(astrologian_level_var.get() or 0),
        int(sage_level_var.get() or 0)
    ]

    user_inputs.append(user_data)    

def print_user_data():
    print("Currently saved users: ")
    for user_data in user_inputs:
        print(f"{user_data[0]}: {user_data}")
    
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

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

frame = ck.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

root.title("Final Fantasy XIV - Job Recommender")

entry1 = ck.CTkEntry(master=frame, placeholder_text="Input Your Name Here")
entry1.pack(pady=12, padx=10)

button = ck.CTkButton(master=frame, text="Continue", command=btn_continue)
button.pack(pady=12, padx=10)

exit_button = ck.CTkButton(master=frame, text="Exit", command=btn_exit, hover_color="red")
exit_button.pack(pady=12, padx=10)

root.mainloop()