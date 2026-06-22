import customtkinter as ctk
from backend.auth import register_user
from tkinter import messagebox

# Color Palette
PRIMARY_BLUE = "#4F5BD5"
HOVER_BLUE = "#3F4ACB"
BACKGROUND = "#F8F9FC"
PANEL_BG = "#EEF2FF"
TEXT_DARK = "#111827"
TEXT_GRAY = "#6B7280"
WHITE = "#FFFFFF"

# Changed from ctk.CTk to ctk.CTkFrame to work inside a single shared window instance
class SignupPage(ctk.CTkFrame):
    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=BACKGROUND, corner_radius=0)
        self.on_back = on_back
        self.pack(fill="both", expand=True)

        # Layout Configuration (Two Columns)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Build UI Panels
        self.create_left_panel()
        self.create_right_panel()

    def create_left_panel(self):
        self.left_frame = ctk.CTkFrame(self, fg_color=BACKGROUND, corner_radius=0)
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        self.form_container = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        self.form_container.pack(expand=True, padx=50, pady=50)

        self.app_title = ctk.CTkLabel(
            self.form_container,
            text="🎓 Student Management System",
            font=("Helvetica", 16, "bold"),
            text_color=PRIMARY_BLUE
        )
        self.app_title.pack(anchor="w", pady=(0, 20))

        # Back Button
        self.back_btn = ctk.CTkButton(
            self.form_container,
            text="← Back to Login",
            fg_color="transparent",
            text_color=TEXT_GRAY,
            hover_color=BACKGROUND,
            font=("Helvetica", 14),
            anchor="w",
            width=0,
            command=self.open_login
        )
        self.back_btn.pack(anchor="w", pady=(0, 30))

        self.heading = ctk.CTkLabel(
            self.form_container,
            text="Create Your Account",
            font=("Helvetica", 32, "bold"),
            text_color=TEXT_DARK
        )
        self.heading.pack(anchor="w", pady=(0, 5))

        self.subtitle = ctk.CTkLabel(
            self.form_container,
            text="Join us and get started with Student Management System",
            font=("Helvetica", 14),
            text_color=TEXT_GRAY
        )
        self.subtitle.pack(anchor="w", pady=(0, 30))

        entry_style = {
            "height": 45,
            "fg_color": WHITE,
            "text_color": TEXT_DARK,
            "placeholder_text_color": TEXT_GRAY,
            "border_color": "#D1D5DB",
            "corner_radius": 8,
            "font": ("Helvetica", 14),
            "width": 400
        }

        self.fullname_entry = ctk.CTkEntry(self.form_container, placeholder_text="Full Name", **entry_style)
        self.fullname_entry.pack(pady=(0, 15))

        self.username_entry = ctk.CTkEntry(self.form_container, placeholder_text="Username", **entry_style)
        self.username_entry.pack(pady=(0, 15))

        self.email_entry = ctk.CTkEntry(self.form_container, placeholder_text="Email Address", **entry_style)
        self.email_entry.pack(pady=(0, 15))

        self.password_entry = ctk.CTkEntry(self.form_container, placeholder_text="Password", show="*", **entry_style)
        self.password_entry.pack(pady=(0, 15))

        self.confirm_password_entry = ctk.CTkEntry(self.form_container, placeholder_text="Confirm Password", show="*", **entry_style)
        self.confirm_password_entry.pack(pady=(0, 15))

        self.options_frame = ctk.CTkFrame(self.form_container, fg_color="transparent")
        self.options_frame.pack(fill="x", pady=(0, 20))

        self.show_pass_var = ctk.StringVar(value="off")
        self.show_password_cb = ctk.CTkCheckBox(
            self.options_frame,
            text="Show Password",
            variable=self.show_pass_var,
            onvalue="on",
            offvalue="off",
            command=self.toggle_password_visibility,
            text_color=TEXT_GRAY,
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            border_color="#D1D5DB",
            corner_radius=4,
            checkbox_height=20,
            checkbox_width=20
        )
        self.show_password_cb.pack(anchor="w", pady=(0, 10))

        self.terms_var = ctk.StringVar(value="off")
        self.terms_cb = ctk.CTkCheckBox(
            self.options_frame,
            text="I agree to Terms and Conditions",
            variable=self.terms_var,
            onvalue="on",
            offvalue="off",
            text_color=TEXT_DARK,
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            border_color="#D1D5DB",
            corner_radius=4,
            checkbox_height=20,
            checkbox_width=20
        )
        self.terms_cb.pack(anchor="w")

        # Sign Up Actions Route Trigger
        self.signup_btn = ctk.CTkButton(
            self.form_container,
            text="Sign Up",
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            text_color=WHITE,
            height=45,
            width=400,
            corner_radius=8,
            font=("Helvetica", 16, "bold"),
            command=self.signup_user
        )
        self.signup_btn.pack(pady=(15, 25))

        self.bottom_frame = ctk.CTkFrame(self.form_container, fg_color="transparent")
        self.bottom_frame.pack()

        self.acc_label = ctk.CTkLabel(
            self.bottom_frame,
            text="Already have an account? ",
            text_color=TEXT_GRAY,
            font=("Helvetica", 14)
        )
        self.acc_label.pack(side="left")

        self.login_link = ctk.CTkButton(
            self.bottom_frame,
            text="Login",
            fg_color="transparent",
            hover_color=BACKGROUND,
            text_color=PRIMARY_BLUE,
            font=("Helvetica", 14, "bold"),
            width=0,
            command=self.open_login
        )
        self.login_link.pack(side="left")

    def create_right_panel(self):
        self.right_frame = ctk.CTkFrame(self, fg_color=PANEL_BG, corner_radius=0)
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self.dash_container = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        self.dash_container.pack(expand=True, padx=50, pady=50)

        self.dash_title = ctk.CTkLabel(
            self.dash_container,
            text="Student Dashboard",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        self.dash_title.pack(anchor="w", pady=(0, 40))

        self.cards_frame = ctk.CTkFrame(self.dash_container, fg_color="transparent")
        self.cards_frame.pack(fill="both", expand=True)

        self.create_stat_card("Students", "1250", 0, 0)
        self.create_stat_card("Courses", "24", 0, 1)
        self.create_stat_card("Teachers", "45", 1, 0)
        self.create_stat_card("Attendance", "92%", 1, 1)

    def create_stat_card(self, title, value, row, col):
        card = ctk.CTkFrame(
            self.cards_frame,
            fg_color=WHITE,
            corner_radius=15,
            width=220,
            height=160
        )
        card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        card.pack_propagate(False)

        inner_frame = ctk.CTkFrame(card, fg_color="transparent")
        inner_frame.pack(expand=True)

        val_label = ctk.CTkLabel(
            inner_frame,
            text=value,
            font=("Helvetica", 36, "bold"),
            text_color=PRIMARY_BLUE
        )
        val_label.pack(pady=(0, 5))

        title_label = ctk.CTkLabel(
            inner_frame,
            text=title,
            font=("Helvetica", 16),
            text_color=TEXT_GRAY
        )
        title_label.pack()

    def toggle_password_visibility(self):
        if self.show_pass_var.get() == "on":
            self.password_entry.configure(show="")
            self.confirm_password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            self.confirm_password_entry.configure(show="*")

    def open_login(self):
        self.destroy()
        if self.on_back:
            self.on_back()

    def signup_user(self):
        # Read all form field values
        fullname = self.fullname_entry.get().strip()
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()  # FIX 1: was never read

        # Check 1: Empty fields
        if not fullname or not username or not email or not password or not confirm_password:
            messagebox.showwarning("Warning", "Please fill all required fields.")
            return

        # Check 2: Password match validation (FIX 2: was completely missing)
        if password != confirm_password:
            messagebox.showwarning("Warning", "Passwords do not match.")
            return

        # Check 3: Terms and Conditions must be accepted (FIX 3: checkbox had no variable, was never checked)
        if self.terms_var.get() != "on":
            messagebox.showwarning("Warning", "Please agree to Terms and Conditions.")
            return

        # Call backend registration handler
        result = register_user(fullname, username, email, password)

        # Check 4: Use truthiness check, not identity (FIX 4: "result is True" broke after DB code was added)
        if result:
            messagebox.showinfo("Success", "Registration Successful.")
            self.open_login()
        else:
            messagebox.showerror("Error", "Username already exists.")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1280x720")
    app = SignupPage(root)
    root.mainloop()