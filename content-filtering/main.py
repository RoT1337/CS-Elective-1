import customtkinter as ck

ck.set_appearance_mode("dark")
ck.set_default_color_theme("dark-blue")

root = ck.CTk()
root.geometry("800x600")

def test():
    print("Hello Python GUI using ck!")

frame = ck.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ck.CTkLabel(master=frame, text="This is my first Python GUI", font=("Helvetica", 24))
label.pack(pady=12, padx=10)

entry1 = ck.CTkEntry(master=frame, placeholder_text="Test your keyboard here")
entry1.pack(pady=12, padx=10)
entry2 = ck.CTkEntry(master=frame, placeholder_text="Banana Here 2", show=":)")
entry2.pack(pady=12, padx=10)

button = ck.CTkButton(master=frame, text="Submit!", command=wah)
button.pack(pady=12, padx=10)

checkbox = ck.CTkCheckBox(master=frame, text="These Nutz?")
checkbox.pack(pady=12, padx=10)

root.mainloop()