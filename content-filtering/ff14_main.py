import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import numpy as np
from numpy.linalg import norm
import os

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

root = ck.CTk()
root.geometry("400x300")

# count = 0

user_inputs = [
    ["User1", 45, 0, 78, 22, 0, 63, 0, 81, 0, 92, 0, 71, 0, 87, 0, 96, 0, 53, 0, 61],
    ["User2", 0, 42, 0, 65, 0, 83, 0, 99, 0, 25, 0, 43, 0, 67, 0, 82, 0, 73, 0, 55],
    ["User3", 33, 0, 52, 0, 74, 0, 91, 0, 15, 0, 35, 0, 54, 0, 72, 0, 64, 0, 45],
    ["User4", 0, 24, 0, 47, 0, 68, 0, 85, 0, 100, 0, 23, 0, 41, 0, 66, 0, 57, 0, 38],
    ["User5", 12, 0, 34, 0, 56, 0, 77, 0, 93, 0, 14, 0, 32, 0, 51, 0, 48, 0, 29],
    ["User6", 0, 61, 0, 79, 0, 98, 0, 21, 0, 44, 0, 62, 0, 84, 0, 97, 0, 91, 0, 72],
    ["User7", 73, 0, 89, 0, 13, 0, 31, 0, 53, 0, 75, 0, 88, 0, 19, 0, 81, 0, 63],
    ["User8", 0, 55, 0, 71, 0, 94, 0, 17, 0, 36, 0, 58, 0, 76, 0, 95, 0, 99, 0, 83],
    ["User9", 27, 0, 49, 0, 67, 0, 86, 0, 100, 0, 22, 0, 46, 0, 65, 0, 74, 0, 52],
    ["User10", 0, 37, 0, 59, 0, 80, 0, 92, 0, 11, 0, 33, 0, 50, 0, 69, 0, 47, 0, 28]
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

    # List of job names
job_names = [
        "Paladin", "Warrior", "Dark Knight", "Gunbreaker",
        "Dragoon", "Reaper", "Monk", "Samurai", "Ninja", "Viper",
        "Bard", "Machinist", "Dancer", "Black Mage", "Summoner",
        "Red Mage", "White Mage", "Scholar", "Astrologian", "Sage"
    ]

script_dir = os.path.dirname(os.path.abspath(__file__))

tank_base_dir = os.path.join(script_dir, "JobIcons/01_TANK/Job")
dps_base_dir = os.path.join(script_dir, "JobIcons/03_DPS/Job")
healer_base_dir = os.path.join(script_dir, "JobIcons/02_Healer/Job")

paladin_path = os.path.join(tank_base_dir, "Paladin.png")
warrior_path = os.path.join(tank_base_dir, "Warrior.png")
dark_knight_path = os.path.join(tank_base_dir, "DarkKnight.png")
gunbreaker_path = os.path.join(tank_base_dir, "Gunbreaker.png")

dragoon_path = os.path.join(dps_base_dir, "Dragoon.png")
reaper_path = os.path.join(dps_base_dir, "Reaper.png")
monk_path = os.path.join(dps_base_dir, "Monk.png")
samurai_path = os.path.join(dps_base_dir, "Samurai.png")
ninja_path = os.path.join(dps_base_dir, "Ninja.png")
viper_path = os.path.join(dps_base_dir, "Viper.png")
bard_path = os.path.join(dps_base_dir, "Bard.png")
machinist_path = os.path.join(dps_base_dir, "Machinist.png")
dancer_path = os.path.join(dps_base_dir, "Dancer.png")
black_mage_path = os.path.join(dps_base_dir, "BlackMage.png")
summoner_path = os.path.join(dps_base_dir, "Summoner.png")
red_mage_path = os.path.join(dps_base_dir, "RedMage.png")
white_mage_path = os.path.join(healer_base_dir, "WhiteMage.png")

scholar_path = os.path.join(healer_base_dir, "Scholar.png")
astrologian_path = os.path.join(healer_base_dir, "Astrologian.png")
sage_path = os.path.join(healer_base_dir, "Sage.png")

def validate_number_input(event):
    entry = event.widget
    value = entry.get()
    if not value.isdigit() and value != "":
        entry.delete(0, tk.END)
        entry.insert(0, ''.join(filter(str.isdigit, value)))

def load_image(image_path, size=(30, 30)):
    image = Image.open(image_path)
    image = image.resize(size, Image.Resampling.LANCZOS)
    return ck.CTkImage(light_image=image, dark_image=image, size=size)

def create_input_frame(master, image_path, textvariable):
    bg_color = master.cget("bg")
    frame = tk.Frame(master, bg=bg_color)
    frame.pack(pady=12, padx=100, fill='x', expand=True, anchor='center')
    image = load_image(image_path)
    label = ck.CTkLabel(master=frame, image=image, text="", bg_color=bg_color)
    label.image = image
    label.pack(side='left')
    entry = ck.CTkEntry(master=frame, textvariable=textvariable, width=200, bg_color=bg_color)
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

    create_input_frame(tank_window, paladin_path, paladin_level_var)
    create_input_frame(tank_window, warrior_path, warrior_level_var)
    create_input_frame(tank_window, dark_knight_path, dark_knight_level_var)
    create_input_frame(tank_window, gunbreaker_path, gunbreaker_level_var)

    tank_button = ck.CTkButton(master=tank_window, text="Continue", command=open_meleedps_window)
    tank_button.pack(pady=12, padx=10)

def open_meleedps_window():
    global meleedps_window
    tank_window.destroy()
    meleedps_window = ck.CTkToplevel(root)
    window_width = 400
    window_height = 500
    screen_width = meleedps_window.winfo_screenwidth()
    screen_height = meleedps_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    meleedps_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    meleedps_window.title("Melee DPS Levels")

    label = ck.CTkLabel(master=meleedps_window, text="Input your Warrior of Light's Melee DPS Levels")
    label.pack(pady=12, padx=10)

    create_input_frame(meleedps_window, dragoon_path, dragoon_level_var)
    create_input_frame(meleedps_window, reaper_path, reaper_level_var)
    create_input_frame(meleedps_window, monk_path, monk_level_var)
    create_input_frame(meleedps_window, samurai_path, samurai_level_var)
    create_input_frame(meleedps_window, ninja_path, ninja_level_var)
    create_input_frame(meleedps_window, viper_path, viper_level_var)

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

    create_input_frame(physrange_window, bard_path, bard_level_var)
    create_input_frame(physrange_window, machinist_path, machinist_level_var)
    create_input_frame(physrange_window, dancer_path, dancer_level_var)

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

    create_input_frame(magirange_window, black_mage_path, black_mage_level_var)
    create_input_frame(magirange_window, summoner_path, summoner_level_var)
    create_input_frame(magirange_window, red_mage_path, red_mage_level_var)

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

    create_input_frame(healer_window, white_mage_path, white_mage_level_var)
    create_input_frame(healer_window, scholar_path, scholar_level_var)
    create_input_frame(healer_window, astrologian_path, astrologian_level_var)
    create_input_frame(healer_window, sage_path, sage_level_var)

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
    button1 = ck.CTkButton(master=new_frame, text="Recommend me a Job", hover_color="green", command=lambda: recommend_next_job(entry2.get()))
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
    
def calculate_cosine_similarity(user_name):
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
        return []
    
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

    return similarity_scores

def recommend_next_job(user_name):
    # Find the target user data
    target_user_data = None
    for user_data in user_inputs:
        if user_data[0] == user_name:
            target_user_data = user_data
            break
    
    if target_user_data is None:
        print(f"No data found for user: {user_name}")
        return
    
    # Calculate cosine similarity
    similarity_scores = calculate_cosine_similarity(user_name)
    
    # Find jobs with level 0 in the target user's data
    zero_level_jobs = [i for i, level in enumerate(target_user_data[1:], start=1) if level == 0]
    
    # Calculate recommended ratings for each job with level 0
    recommended_jobs = []
    for job_index in zero_level_jobs:
        numerator = 0
        denominator = 0
        for name, similarity in similarity_scores:
            for user_data in user_inputs:
                if user_data[0] == name:
                    if len(user_data) > job_index + 1 and user_data[job_index + 1] > 0:  # Adjust index to account for the user name
                        numerator += similarity * user_data[job_index + 1] 
                        denominator += similarity
        if denominator > 0:
            recommended_rating = numerator / denominator
            recommended_jobs.append((job_index, recommended_rating))
    
    # Sort recommended jobs by rating in descending order
    recommended_jobs.sort(key=lambda x: x[1], reverse=True)
    
    # Print recommended jobs with names
    for job_index, rating in recommended_jobs:
        job_name = job_names[job_index - 1]  # Adjust index if needed
        print(f"{job_name}: Recommended rating {rating}")
    
    # Create a frame to the right of the root window
    right_frame = ck.CTkFrame(master=root)
    right_frame.pack(side="right", pady=10, padx=10, fill="both", expand=True)

    # Display top 3 closest similarity users
    top_users_label = ck.CTkLabel(master=right_frame, text="Top 3 Closest Similarity Users")
    top_users_label.pack(pady=5, padx=5)

    # Get the top 3 users
    top_users = [(name, round(score, 2)) for name, score in similarity_scores[:3]]
    for user, score in top_users:
        user_label = ck.CTkLabel(master=right_frame, text=f"{user}: Similarity score {score}")
        user_label.pack(pady=2, padx=5)

    # Display top 3 suggested jobs
    top_jobs_label = ck.CTkLabel(master=right_frame, text="Top 3 Suggested Jobs")
    top_jobs_label.pack(pady=5, padx=5)

    # Get the top 3 recommended jobs
    top_jobs = [(job_names[job_index - 1], round(rating, 2)) for job_index, rating in recommended_jobs[:3]]
    for job_name, rating in top_jobs:
        job_label = ck.CTkLabel(master=right_frame, text=f"{job_name}: Recommended rating {rating}")
        job_label.pack(pady=2, padx=5)

    root.geometry("400x650")

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