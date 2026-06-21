import customtkinter as ctk
import tkinter as tk

# --- Color Palette Constants ---
PRIMARY_BLUE = "#4F5BD5"
HOVER_BLUE = "#3F4ACB"
BACKGROUND = "#F8F9FC"
PANEL_BG = "#EEF2FF"
TEXT_DARK = "#111827"
TEXT_GRAY = "#6B7280"
WHITE = "#FFFFFF"

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        
        # Set theme and window configuration
        ctk.set_appearance_mode("light")
        self.root.geometry("1280x720")
        self.root.after(100, lambda: self.root.state("zoomed"))

        
        
        # Maximize window (cross-platform handling)
        try:
            self.root.state('zoomed')
        except tk.TclError:
            self.root.attributes('-zoomed', True)

        self.root.configure(fg_color=BACKGROUND)

        # --- Main Grid Layout ---
        # Divide screen into two equal columns
        self.root.grid_columnconfigure(0, weight=1, uniform="group1")
        self.root.grid_columnconfigure(1, weight=1, uniform="group1")
        self.root.grid_rowconfigure(0, weight=1)

        # Create main left and right panels
        self._create_left_panel()
        self._create_right_panel()

    def _create_left_panel(self):
        """Creates the left panel containing the login form."""
        self.left_frame = ctk.CTkFrame(self.root, fg_color=BACKGROUND, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        # Container to center the login form vertically and horizontally
        login_container = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        login_container.place(relx=0.5, rely=0.5, anchor="center")

        # --- Header Section ---
        # Logo / Title
        logo_label = ctk.CTkLabel(
            login_container, 
            text="🎓 Student Management System",
            font=("Segoe UI", 18, "bold"),
            text_color=PRIMARY_BLUE
        )
        logo_label.pack(anchor="w", pady=(0, 40))

        # Welcome Back Heading
        welcome_label = ctk.CTkLabel(
            login_container, 
            text="Welcome Back",
            font=("Segoe UI", 36, "bold"),
            text_color=TEXT_DARK
        )
        welcome_label.pack(anchor="w", pady=(0, 5))

        # Subtitle
        subtitle_label = ctk.CTkLabel(
            login_container, 
            text="Login to continue to your account",
            font=("Segoe UI", 14),
            text_color=TEXT_GRAY
        )
        subtitle_label.pack(anchor="w", pady=(0, 40))

        # --- Form Section ---
        # Username Entry
        username_label = ctk.CTkLabel(login_container, text="Username", font=("Segoe UI", 12, "bold"), text_color=TEXT_DARK)
        username_label.pack(anchor="w", pady=(0, 5))
        
        self.username_entry = ctk.CTkEntry(
            login_container, 
            width=400, 
            height=45, 
            corner_radius=8,
            font=("Segoe UI", 14),
            fg_color=WHITE,
            border_color="#E5E7EB",
            text_color=TEXT_DARK,
            placeholder_text="Enter your username"
        )
        self.username_entry.pack(anchor="w", pady=(0, 20))

        # Password Entry
        password_label = ctk.CTkLabel(login_container, text="Password", font=("Segoe UI", 12, "bold"), text_color=TEXT_DARK)
        password_label.pack(anchor="w", pady=(0, 5))
        
        self.password_entry = ctk.CTkEntry(
            login_container, 
            width=400, 
            height=45, 
            corner_radius=8,
            font=("Segoe UI", 14),
            fg_color=WHITE,
            border_color="#E5E7EB",
            text_color=TEXT_DARK,
            show="*",
            placeholder_text="Enter your password"
        )
        self.password_entry.pack(anchor="w", pady=(0, 15))

        # --- Options Section (Checkbox & Forgot Password) ---
        options_frame = ctk.CTkFrame(login_container, fg_color="transparent", width=400)
        options_frame.pack(fill="x", pady=(0, 30))

        # Show Password Checkbox
        self.show_password_var = ctk.BooleanVar(value=False)
        show_password_cb = ctk.CTkCheckBox(
            options_frame, 
            text="Show Password",
            font=("Segoe UI", 13),
            text_color=TEXT_GRAY,
            border_color="#D1D5DB",
            hover_color=HOVER_BLUE,
            fg_color=PRIMARY_BLUE,
            variable=self.show_password_var,
            command=self._toggle_password_visibility
        )
        show_password_cb.pack(side="left")

        # Forgot Password Link
        forgot_password_btn = ctk.CTkButton(
            options_frame, 
            text="Forgot Password?",
            font=("Segoe UI", 13, "bold"),
            text_color=PRIMARY_BLUE,
            fg_color="transparent",
            hover_color=BACKGROUND,
            command=self._forgot_password_clicked
        )
        forgot_password_btn.pack(side="right")

        # --- Action Buttons Section ---
        # Login Button
        login_btn = ctk.CTkButton(
            login_container, 
            text="Login",
            width=400,
            height=45,
            corner_radius=8,
            font=("Segoe UI", 14, "bold"),
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            command=self._login_clicked
        )
        login_btn.pack(anchor="w", pady=(0, 30))

        # Sign Up Link Area
        signup_frame = ctk.CTkFrame(login_container, fg_color="transparent")
        signup_frame.pack(anchor="center")

        signup_label = ctk.CTkLabel(
            signup_frame, 
            text="Don't have an account?",
            font=("Segoe UI", 14),
            text_color=TEXT_GRAY
        )
        signup_label.pack(side="left", padx=(0, 5))

        signup_btn = ctk.CTkButton(
            signup_frame, 
            text="Sign Up",
            font=("Segoe UI", 14, "bold"),
            text_color=PRIMARY_BLUE,
            fg_color="transparent",
            hover_color=BACKGROUND,
            width=0,
            command=self._signup_clicked
        )
        signup_btn.pack(side="left")

    def _create_right_panel(self):
        """Creates the right panel showing the dashboard preview."""
        self.right_frame = ctk.CTkFrame(self.root, fg_color=PANEL_BG, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        # Dashboard Preview Container
        preview_container = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        preview_container.place(relx=0.5, rely=0.5, anchor="center")

        # Mockup App Window
        app_mockup = ctk.CTkFrame(
            preview_container, 
            fg_color=BACKGROUND, 
            corner_radius=16,
            width=500,
            height=400
        )
        app_mockup.pack_propagate(False)
        app_mockup.pack(padx=20, pady=20)

        # Mockup Header
        mockup_header = ctk.CTkLabel(
            app_mockup,
            text="Dashboard Overview",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT_DARK
        )
        mockup_header.pack(anchor="w", padx=30, pady=(30, 20))

        # Mockup Stats Grid
        stats_frame = ctk.CTkFrame(app_mockup, fg_color="transparent")
        stats_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
        stats_frame.grid_columnconfigure(0, weight=1, pad=15)
        stats_frame.grid_columnconfigure(1, weight=1, pad=15)
        stats_frame.grid_rowconfigure(0, weight=1, pad=15)
        stats_frame.grid_rowconfigure(1, weight=1, pad=15)

        # Define stat cards data
        cards_data = [
            ("Students", "1250", 0, 0),
            ("Courses", "24", 0, 1),
            ("Teachers", "45", 1, 0),
            ("Attendance", "92%", 1, 1)
        ]

        # Generate Statistic Cards
        for title, value, row, col in cards_data:
            card = ctk.CTkFrame(stats_frame, fg_color=WHITE, corner_radius=12)
            card.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
            
            # Card contents
            title_lbl = ctk.CTkLabel(card, text=title, font=("Segoe UI", 13), text_color=TEXT_GRAY)
            title_lbl.pack(anchor="w", padx=20, pady=(15, 0))
            
            val_lbl = ctk.CTkLabel(card, text=value, font=("Segoe UI", 28, "bold"), text_color=TEXT_DARK)
            val_lbl.pack(anchor="w", padx=20, pady=(0, 15))

    # --- Button Callbacks and Logic ---
    def _toggle_password_visibility(self):
        """Toggles the password entry show character."""
        if self.show_password_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def _login_clicked(self):
        """Handles login button click event."""
        print("Login Clicked")

    def _forgot_password_clicked(self):
        """Handles forgot password link click event."""
        print("Forgot Password Clicked")

    def _signup_clicked(self):
        """Handles sign up link click event."""
        print("Sign Up Clicked")


if __name__ == "__main__":
    # Initialize the application
    root = ctk.CTk()
    app = LoginPage(root)
    root.mainloop()