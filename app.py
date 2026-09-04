import os
import json
import time
import threading
import customtkinter as ctk
from pypresence import Presence

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "client_id": "",
    "details": "",
    "state": "",
    "large_image": "",
    "large_text": "",
    "small_image": "",
    "small_text": "",
    "button1_label": "",
    "button1_url": "",
    "button2_label": "",
    "button2_url": "",
    "show_time": True
}

class DiscordRPCApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple Discord RPC")
        self.geometry("520x680")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.config_data = self.load_config()

        self.rpc = None
        self.is_running = False
        self.start_time = None

        self.create_widgets()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    config = DEFAULT_CONFIG.copy()
                    config.update(data)
                    return config
            except Exception as e:
                print(f"Config read error : {e}")
        return DEFAULT_CONFIG.copy()

    def save_config(self):
        data = {
            "client_id": self.entries["client_id"].get().strip(),
            "details": self.entries["details"].get().strip(),
            "state": self.entries["state"].get().strip(),
            "large_image": self.entries["large_image"].get().strip(),
            "large_text": self.entries["large_text"].get().strip(),
            "small_image": self.entries["small_image"].get().strip(),
            "small_text": self.entries["small_text"].get().strip(),
            "button1_label": self.entries["button1_label"].get().strip(),
            "button1_url": self.entries["button1_url"].get().strip(),
            "button2_label": self.entries["button2_label"].get().strip(),
            "button2_url": self.entries["button2_url"].get().strip(),
            "show_time": bool(self.time_switch.get())
        }
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("Configuration saved.")
        except Exception as e:
            print(f"Save error : {e}")

    def create_widgets(self):
        scroll = ctk.CTkScrollableFrame(self)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        self.entries = {}

        fields = [
            ("client_id", "Discord Application ID :"),
            ("details", "Détails (Ligne 1) :"),
            ("state", "État (Ligne 2) :"),
            ("large_image", "Clé Grande Image (Large Image) :"),
            ("large_text", "Texte Grande Image :"),
            ("small_image", "Clé Petite Image (Small Image) :"),
            ("small_text", "Texte Petite Image :"),
            ("button1_label", "Bouton 1 - Libellé :"),
            ("button1_url", "Bouton 1 - Lien URL :"),
            ("button2_label", "Bouton 2 - Libellé :"),
            ("button2_url", "Bouton 2 - Lien URL :"),
        ]

        for key, label_text in fields:
            lbl = ctk.CTkLabel(scroll, text=label_text, anchor="w")
            lbl.pack(fill="x", padx=5, pady=(5, 0))

            entry = ctk.CTkEntry(scroll, placeholder_text=label_text)
            entry.insert(0, self.config_data.get(key, ""))
            entry.pack(fill="x", padx=5, pady=(0, 5))
            self.entries[key] = entry

        self.time_switch = ctk.CTkSwitch(scroll, text="Afficher le temps écoulé")
        if self.config_data.get("show_time", True):
            self.time_switch.select()
        else:
            self.time_switch.deselect()
        self.time_switch.pack(anchor="w", padx=5, pady=10)

        self.status_label = ctk.CTkLabel(scroll, text="Statut : Inactif", text_color="gray")
        self.status_label.pack(pady=5)

        self.start_btn = ctk.CTkButton(scroll, text="Start Rich Presence", command=self.start_rpc, fg_color="green", hover_color="darkgreen")
        self.start_btn.pack(fill="x", padx=5, pady=5)

        self.stop_btn = ctk.CTkButton(scroll, text="Stop Rich Presence", command=self.stop_rpc, fg_color="red", hover_color="darkred", state="disabled")
        self.stop_btn.pack(fill="x", padx=5, pady=5)

    def start_rpc(self):
        self.save_config()
        client_id = self.entries["client_id"].get().strip()

        if not client_id:
            self.status_label.configure(text="Error : Client ID missing", text_color="red")
            return

        try:
            self.rpc = Presence(client_id)
            self.rpc.connect()
            self.is_running = True
            self.start_time = time.time()

            self.start_btn.configure(state="disabled")
            self.stop_btn.configure(state="normal")
            self.status_label.configure(text="Status : Connected to Discord", text_color="green")

            threading.Thread(target=self.update_loop, daemon=True).start()
        except Exception as e:
            self.status_label.configure(text=f"Connexion error : {e}", text_color="red")

    def update_loop(self):
        while self.is_running:
            try:
                payload = {}

                details = self.entries["details"].get().strip()
                if details: payload["details"] = details

                state = self.entries["state"].get().strip()
                if state: payload["state"] = state

                if self.time_switch.get():
                    payload["start"] = self.start_time

                large_img = self.entries["large_image"].get().strip()
                if large_img:
                    payload["large_image"] = large_img
                    large_txt = self.entries["large_text"].get().strip()
                    if large_txt: payload["large_text"] = large_txt

                small_img = self.entries["small_image"].get().strip()
                if small_img:
                    payload["small_image"] = small_img
                    small_txt = self.entries["small_text"].get().strip()
                    if small_txt: payload["small_text"] = small_txt

                buttons = []
                b1_label = self.entries["button1_label"].get().strip()
                b1_url = self.entries["button1_url"].get().strip()
                if b1_label and b1_url:
                    buttons.append({"label": b1_label, "url": b1_url})

                b2_label = self.entries["button2_label"].get().strip()
                b2_url = self.entries["button2_url"].get().strip()
                if b2_label and b2_url:
                    buttons.append({"label": b2_label, "url": b2_url})

                if buttons:
                    payload["buttons"] = buttons

                self.rpc.update(**payload)
            except Exception as e:
                print(f"RPC Update error : {e}")

            time.sleep(15)

    def stop_rpc(self):
        self.is_running = False
        if self.rpc:
            try:
                self.rpc.close()
            except Exception:
                pass
            self.rpc = None

        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_label.configure(text="Status : Inactive", text_color="gray")

    def on_closing(self):
        self.save_config()
        self.stop_rpc()
        self.destroy()

if __name__ == "__main__":
    app = DiscordRPCApp()
    app.mainloop()
