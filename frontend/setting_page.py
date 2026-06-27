import customtkinter as ctk
import sys

# Set appearance mode and default color theme
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class SettingsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#F8F9FC")
        
        # --- Color Palette ---
        self.PRIMARY_BLUE = "#4F5BD5"
        self.HOVER_BLUE = "#3F4ACB"
        self.BACKGROUND = "#F8F9FC"
        self.PANEL_BG = "#EEF2FF"
        self.TEXT_DARK = "#111827"
        self.TEXT_GRAY = "#6B7280"
        self.WHITE = "#FFFFFF"
        self.SUCCESS_GREEN = "#10B981"

        # Configure page grid layout as required
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.create_main_content()

    def create_main_content(self):
        """Builds responsive scrollable layout framework for system settings."""
        
        # 1. Top Bar Container Setup
        top_bar = ctk.CTkFrame(self, height=70, corner_radius=0, fg_color=self.WHITE)
        top_bar.grid(row=0, column=0, sticky="ew")
        top_bar.grid_columnconfigure(0, weight=1)
        top_bar.grid_propagate(False)
        
        page_title = ctk.CTkLabel(top_bar, text="Settings", font=ctk.CTkFont(size=20, weight="bold"), text_color=self.TEXT_DARK)
        page_title.grid(row=0, column=0, padx=30, pady=20, sticky="w")
        
        user_profile = ctk.CTkLabel(top_bar, text="Admin User", font=ctk.CTkFont(size=14), text_color=self.TEXT_GRAY)
        user_profile.grid(row=0, column=1, padx=30, pady=20, sticky="e")

        # Scrollable Form Content Area
        scroll_content = ctk.CTkScrollableFrame(self, fg_color="transparent", corner_radius=0)
        scroll_content.grid(row=1, column=0, padx=30, pady=20, sticky="nsew")
        scroll_content.grid_columnconfigure(0, weight=1)

        # --- SECTION 1 - Profile Settings ---
        profile_section = ctk.CTkFrame(scroll_content, fg_color=self.WHITE, corner_radius=8)
        profile_section.grid(row=0, column=0, pady=(0, 20), sticky="ew")
        profile_section.grid_columnconfigure((0, 1), weight=1)

        p_sec_title = ctk.CTkLabel(profile_section, text="Profile Settings", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.TEXT_DARK)
        p_sec_title.grid(row=0, column=0, columnspan=2, padx=24, pady=(20, 15), sticky="w")

        # Fields Setup
        fields = [
            ("Full Name", "Admin User", 1, 0),
            ("Username", "admin", 1, 1),
            ("Email Address", "admin@edumanager.com", 2, 0),
            ("Phone Number", "+1 234 567 890", 2, 1)
        ]

        for label_text, default_val, r, c in fields:
            f_frame = ctk.CTkFrame(profile_section, fg_color="transparent")
            f_frame.grid(row=r, column=c, padx=24, pady=10, sticky="ew")
            f_frame.grid_columnconfigure(0, weight=1)
            
            lbl = ctk.CTkLabel(f_frame, text=label_text, font=ctk.CTkFont(size=13, weight="normal"), text_color=self.TEXT_GRAY)
            lbl.grid(row=0, column=0, sticky="w", pady=(0, 5))
            
            entry = ctk.CTkEntry(f_frame, height=40, fg_color=self.WHITE, border_color=self.PANEL_BG, text_color=self.TEXT_DARK)
            entry.insert(0, default_val)
            entry.grid(row=1, column=0, sticky="ew")

        # Buttons Group
        p_btn_frame = ctk.CTkFrame(profile_section, fg_color="transparent")
        p_btn_frame.grid(row=3, column=0, columnspan=2, padx=24, pady=(15, 20), sticky="e")
        
        p_update_btn = ctk.CTkButton(p_btn_frame, text="Update Profile", font=ctk.CTkFont(size=13, weight="bold"), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, text_color=self.WHITE, height=36, corner_radius=6, command=lambda: print("Profile Updated"))
        p_update_btn.grid(row=0, column=0, padx=(0, 10))
        
        p_reset_btn = ctk.CTkButton(p_btn_frame, text="Reset Changes", font=ctk.CTkFont(size=13), fg_color="#F3F4F6", hover_color="#E5E7EB", text_color=self.TEXT_DARK, height=36, corner_radius=6, command=lambda: print("Profile Reset"))
        p_reset_btn.grid(row=0, column=1)

        # --- SECTION 2 - Change Password ---
        password_section = ctk.CTkFrame(scroll_content, fg_color=self.WHITE, corner_radius=8)
        password_section.grid(row=1, column=0, pady=(0, 20), sticky="ew")
        password_section.grid_columnconfigure((0, 1, 2), weight=1)

        pass_sec_title = ctk.CTkLabel(password_section, text="Change Password", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.TEXT_DARK)
        pass_sec_title.grid(row=0, column=0, columnspan=3, padx=24, pady=(20, 15), sticky="w")

        pass_fields = [
            ("Current Password", 0),
            ("New Password", 1),
            ("Confirm Password", 2)
        ]

        for label_text, c in pass_fields:
            f_frame = ctk.CTkFrame(password_section, fg_color="transparent")
            f_frame.grid(row=1, column=c, padx=24, pady=10, sticky="ew")
            f_frame.grid_columnconfigure(0, weight=1)
            
            lbl = ctk.CTkLabel(f_frame, text=label_text, font=ctk.CTkFont(size=13, weight="normal"), text_color=self.TEXT_GRAY)
            lbl.grid(row=0, column=0, sticky="w", pady=(0, 5))
            
            entry = ctk.CTkEntry(f_frame, show="•", height=40, fg_color=self.WHITE, border_color=self.PANEL_BG, text_color=self.TEXT_DARK)
            entry.grid(row=1, column=0, sticky="ew")

        p_change_btn = ctk.CTkButton(password_section, text="Change Password", font=ctk.CTkFont(size=13, weight="bold"), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, text_color=self.WHITE, height=36, corner_radius=6, command=lambda: print("Password Changed"))
        p_change_btn.grid(row=2, column=2, padx=24, pady=(15, 20), sticky="e")

        # --- SECTION 3 - System Information ---
        sys_section = ctk.CTkFrame(scroll_content, fg_color="transparent")
        sys_section.grid(row=2, column=0, pady=(0, 20), sticky="ew")
        
        sys_sec_title = ctk.CTkLabel(sys_section, text="System Information", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.TEXT_DARK)
        sys_sec_title.grid(row=0, column=0, columnspan=5, pady=(0, 12), sticky="w")

        for i in range(5):
            sys_section.grid_columnconfigure(i, weight=1, uniform="sys_equal")

        sys_data = [
            {"title": "Application Name", "value": "Student Management System"},
            {"title": "Version", "value": "1.0"},
            {"title": "Developer", "value": "Laxman"},
            {"title": "Database", "value": "SQLite"},
            {"title": "Status", "value": "Active"}
        ]

        for idx, card in enumerate(sys_data):
            card_box = ctk.CTkFrame(sys_section, fg_color=self.WHITE, height=85, corner_radius=8)
            card_box.grid(row=1, column=idx, padx=(0 if idx == 0 else 8, 0 if idx == 4 else 8), sticky="ew")
            card_box.grid_propagate(False)
            card_box.grid_columnconfigure(0, weight=1)
            
            title_lbl = ctk.CTkLabel(card_box, text=card["title"], font=ctk.CTkFont(size=12, weight="normal"), text_color=self.TEXT_GRAY, anchor="w")
            title_lbl.grid(row=0, column=0, padx=16, pady=(14, 2), sticky="ew")
            
            if card["title"] == "Status":
                val_lbl = ctk.CTkLabel(card_box, text=card["value"], font=ctk.CTkFont(size=15, weight="bold"), text_color=self.SUCCESS_GREEN, anchor="w")
            else:
                val_lbl = ctk.CTkLabel(card_box, text=card["value"], font=ctk.CTkFont(size=15, weight="bold"), text_color=self.TEXT_DARK, anchor="w")
            val_lbl.grid(row=1, column=0, padx=16, pady=(0, 10), sticky="ew")

        # --- SECTION 4 - Preferences ---
        pref_section = ctk.CTkFrame(scroll_content, fg_color=self.WHITE, corner_radius=8)
        pref_section.grid(row=3, column=0, pady=(0, 10), sticky="ew")
        pref_section.grid_columnconfigure(0, weight=1)

        pref_sec_title = ctk.CTkLabel(pref_section, text="Preferences", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.TEXT_DARK)
        pref_sec_title.grid(row=0, column=0, padx=24, pady=(20, 10), sticky="w")

        # Checkboxes arrangement
        chk_frame = ctk.CTkFrame(pref_section, fg_color="transparent")
        chk_frame.grid(row=1, column=0, padx=24, pady=10, sticky="w")

        cb_notif = ctk.CTkCheckBox(chk_frame, text="Enable Notifications", text_color=self.TEXT_DARK, font=ctk.CTkFont(size=13), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, border_color=self.TEXT_GRAY)
        cb_notif.select()
        cb_notif.grid(row=0, column=0, padx=(0, 30), sticky="w")

        cb_dark = ctk.CTkCheckBox(chk_frame, text="Enable Dark Mode", text_color=self.TEXT_DARK, font=ctk.CTkFont(size=13), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, border_color=self.TEXT_GRAY)
        cb_dark.select()
        cb_dark.grid(row=0, column=1, padx=(0, 30), sticky="w")

        cb_rem = ctk.CTkCheckBox(chk_frame, text="Remember Login", text_color=self.TEXT_DARK, font=ctk.CTkFont(size=13), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, border_color=self.TEXT_GRAY)
        cb_rem.select()
        cb_rem.grid(row=0, column=2, sticky="w")

        pref_save_btn = ctk.CTkButton(pref_section, text="Save Settings", font=ctk.CTkFont(size=13, weight="bold"), fg_color=self.PRIMARY_BLUE, hover_color=self.HOVER_BLUE, text_color=self.WHITE, height=36, corner_radius=6, command=lambda: print("Preferences Saved"))
        pref_save_btn.grid(row=2, column=0, padx=24, pady=(15, 20), sticky="e")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x700")
    page = SettingsPage(root)
    page.pack(fill="both", expand=True)
    root.mainloop()