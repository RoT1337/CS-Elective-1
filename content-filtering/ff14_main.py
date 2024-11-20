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

user_inputs = [
    ["User1", 50, 0, 75, 20, 0, 60, 0, 80, 0, 90, 0, 70, 0, 85, 0, 95, 0, 50, 0, 60],
    ["User2", 0, 40, 0, 60, 0, 80, 0, 100, 0, 20, 0, 40, 0, 60, 0, 80, 0, 70, 0, 50],
    ["User3", 30, 0, 50, 0, 70, 0, 90, 0, 10, 0, 30, 0, 50, 0, 70, 0, 60, 0, 40],
    ["User4", 0, 20, 0, 40, 0, 60, 0, 80, 0, 100, 0, 20, 0, 40, 0, 60, 0, 50, 0, 30],
    ["User5", 10, 0, 30, 0, 50, 0, 70, 0, 90, 0, 10, 0, 30, 0, 50, 0, 40, 0, 20],
    ["User6", 0, 60, 0, 80, 0, 100, 0, 20, 0, 40, 0, 60, 0, 80, 0, 100, 0, 90, 0, 70],
    ["User7", 70, 0, 90, 0, 10, 0, 30, 0, 50, 0, 70, 0, 90, 0, 10, 0, 80, 0, 60],
    ["User8", 0, 50, 0, 70, 0, 90, 0, 10, 0, 30, 0, 50, 0, 70, 0, 90, 0, 100, 0, 80],
    ["User9", 20, 0, 40, 0, 60, 0, 80, 0, 100, 0, 20, 0, 40, 0, 60, 0, 70, 0, 50],
    ["User10", 0, 30, 0, 50, 0, 70, 0, 90, 0, 10, 0, 30, 0, 50, 0, 60, 0, 40, 0, 20]
]

# 20 Jobs
paladin_level_var = tk.StringVar()
warrior_level_var = tk.StringVar()
dark_knight_level_var = tk.StringVar()
gunbreaker_level_var = tk.StringVar()
dragoon_level_var = tk.StringVar()
reaper_level_var = tk.StringVar()
monk_level_var = tk.StringVar()
samurai_level_var = tk.StringVar()
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

# ToDo: This PoS is putting out a white background and even bg_color cant fix.
# I might turn into a valve developer and start crashing out I swear
def create_input_frame(master, label_text, textvariable): 
    frame = tk.Frame(master)
    frame.pack(pady=12, padx=10, fill='x')
    label = ck.CTkLabel(master=frame, text=label_text, bg_color="black")
    label.pack(side='left')
    entry = ck.CTkEntry(master=frame, textvariable=textvariable, width=200, bg_color="black")
    entry.pack(side='left', padx=10)
    entry.bind("<KeyRelease>", validate_number_input)
    return entry

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

    create_input_frame(tank_window, "Paladin Level", paladin_level_var)
    create_input_frame(tank_window, "Warrior Level", warrior_level_var)
    create_input_frame(tank_window, "Dark Knight Level", dark_knight_level_var)
    create_input_frame(tank_window, "Gunbreaker Level", gunbreaker_level_var)

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

    create_input_frame(meleedps_window, "Dragoon Level", dragoon_level_var)
    create_input_frame(meleedps_window, "Reaper Level", reaper_level_var)
    create_input_frame(meleedps_window, "Monk Level", monk_level_var)
    create_input_frame(meleedps_window, "Samurai Level", samurai_level_var)
    create_input_frame(meleedps_window, "Ninja Level", ninja_level_var)
    create_input_frame(meleedps_window, "Viper Level", viper_level_var)

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

    create_input_frame(physrange_window, "Bard Level", bard_level_var)
    create_input_frame(physrange_window, "Machinist Level", machinist_level_var)
    create_input_frame(physrange_window, "Dancer Level", dancer_level_var)

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

    create_input_frame(magirange_window, "Black Mage Level", black_mage_level_var)
    create_input_frame(magirange_window, "Summoner Level", summoner_level_var)
    create_input_frame(magirange_window, "Red Mage Level", red_mage_level_var)

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

    create_input_frame(healer_window, "White Mage Level", white_mage_level_var)
    create_input_frame(healer_window, "Scholar Level", scholar_level_var)
    create_input_frame(healer_window, "Astrologian Level", astrologian_level_var)
    create_input_frame(healer_window, "Sage Level", sage_level_var)

    healer_button = ck.CTkButton(master=healer_window, text="Submit", command=finish)
    healer_button.pack(pady=12, padx=10)

def finish():
    global count
    healer_window.destroy()
    root.deiconify()
    #count += 1

    save_user_inputs()
    messagebox.showinfo("Info", "User data saved")

    print_user_data()

    # if count == 4:
    new_frame = ck.CTkFrame(master=root)
    new_frame.pack(pady=10, padx=10, fill="both", expand=True)
    label = ck.CTkLabel(master=new_frame, text="Look for your next Job to take!")
    label.pack(pady=12, padx=10)
    global entry2
    entry2 = ck.CTkEntry(master=new_frame, placeholder_text="Input Name")
    entry2.pack(pady=12, padx=10)
    button1 = ck.CTkButton(master=new_frame, text="Recommend me a Class", hover_color="green", command=calculate_cosine_similarity)
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
        int(dragoon_level_var.get() or 0),
        int(reaper_level_var.get() or 0),
        int(monk_level_var.get() or 0),
        int(samurai_level_var.get() or 0),
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
    
def calculate_cosine_similarity():
    user_name = entry2.get()

    # Convert user data to vectors
    user_vectors = []
    target_vector = None
    for user_data in user_inputs:
        vector = [val for val in user_data[1:]]
        user_vectors.append(vector)
        if user_data[0] == user_name:
            target_vector = vector
    
    if target_vector is None:
        print(f"No data found for user: {user_name}")
        return
    
    # Ensure all vectors have the same length
    max_length = max(len(vector) for vector in user_vectors)
    user_vectors = [vector + [0] * (max_length - len(vector)) for vector in user_vectors]
    target_vector += [0] * (max_length - len(target_vector))

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