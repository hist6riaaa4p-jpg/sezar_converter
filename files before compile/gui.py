from fan3 import encrypt, decrypt
import customtkinter as ctk

app = ctk.CTk()

app.configure( fg_color='#FFD6E8')
app.geometry("720x480")
app.title("Encryption and Decryption Tool")

def window():
    def perform_action():
        mode = mode_var.get()
        key = int(key_entry.get())
        text = text_entry.get("1.0", "end-1c")

        if mode == 1:
            result = encrypt(text, key)
            result_label.delete("1.0", "end")
            result_label.insert("1.0", "Result: " + result)
        else:
            result = decrypt(text, key)
            result_label.delete("1.0", "end")
            result_label.insert("1.0", "Result: " + result)

    mode_var = ctk.IntVar(value=1)

    mode_frame = ctk.CTkFrame(app, fg_color='#FFFFFF', corner_radius=10)
    mode_frame.pack(pady=10)

    encrypt_radio = ctk.CTkRadioButton(
        mode_frame, text="Encrypt", variable=mode_var, value=1,
        fg_color='#FF1493', hover_color='#FF69B4', text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    encrypt_radio.pack(side="left", padx=10)

    decrypt_radio = ctk.CTkRadioButton(
        mode_frame, text="Decrypt", variable=mode_var, value=2,
        fg_color='#FF1493', hover_color='#FF69B4', text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    decrypt_radio.pack(side="left", padx=10)

    key_label = ctk.CTkLabel(app, text="Enter the key (1-26):", 
        text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    key_label.pack(pady=5)

    key_entry = ctk.CTkEntry(app, fg_color='#FFFFFF', text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    key_entry.pack(pady=5)

    text_label = ctk.CTkLabel(app, text="Enter the text:", 
         text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    text_label.pack(pady=5)

    text_entry = ctk.CTkTextbox(app, height=5,
                                fg_color='#FFFFFF', text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    text_entry.pack(pady=5)

    action_button = ctk.CTkButton(
        app, text="Perform Action", command=perform_action,
        fg_color='#FF1493', hover_color='#FF69B4', text_color='#FFFFFF',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    action_button.pack(pady=10)

    result_label = ctk.CTkTextbox(app, height=5,
                                  fg_color='#FFFFFF', text_color='#000000',
        font=ctk.CTkFont(size=14, weight="bold")
        )
    result_label.pack(pady=5)

window()
app.mainloop()
