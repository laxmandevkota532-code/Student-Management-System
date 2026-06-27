import tkinter
from tkinter import messagebox
import customtkinter as ctk

PRIMARY_BLUE = "#4F5BD5"
HOVER_BLUE = "#3F4ACB"
BACKGROUND = "#F8F9FC"
PANEL_BG = "#EEF2FF"
TEXT_DARK = "#111827"
TEXT_GRAY = "#6B7280"
WHITE = "#FFFFFF"
BORDER_COLOR = "#D1D5DB"
LIGHT_GRAY = "#F3F4F6"
SUBTLE_BORDER = "#E5E7EB"

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class ForgotPasswordPage(ctk.CTkFrame):
    def __init__(self, master, on_back=None):
        super().__init__(master, fg_color=BACKGROUND)
        self.pack(fill="both", expand=True)

        self.on_back = on_back

        self._show_password = False
        self._show_confirm = False
        self._pw_var = tkinter.BooleanVar(value=False)
        self._confirm_var = tkinter.BooleanVar(value=False)

        self.grid_columnconfigure(0, weight=1, uniform="col")
        self.grid_columnconfigure(1, weight=1, uniform="col")
        self.grid_rowconfigure(0, weight=1)

        self._build_left_panel()
        self._build_right_panel()

    def _build_left_panel(self):
        left_outer = ctk.CTkFrame(self, fg_color=BACKGROUND, corner_radius=0)
        left_outer.grid(row=0, column=0, sticky="nsew")
        left_outer.grid_rowconfigure(0, weight=1)
        left_outer.grid_columnconfigure(0, weight=1)

        scroll_container = ctk.CTkFrame(left_outer, fg_color=BACKGROUND, corner_radius=0)
        scroll_container.grid(row=0, column=0, sticky="nsew", padx=64, pady=48)
        scroll_container.grid_columnconfigure(0, weight=1)
        scroll_container.grid_rowconfigure(1, weight=1)

        self._build_top_bar(scroll_container)
        self._build_form(scroll_container)
        self._build_footer(scroll_container)

    def _build_top_bar(self, parent):
        bar = ctk.CTkFrame(parent, fg_color="transparent")
        bar.grid(row=0, column=0, sticky="ew", pady=(0, 36))
        bar.grid_columnconfigure(1, weight=1)

        logo_label = ctk.CTkLabel(
            bar,
            text="🎓  College Management System",
            font=("Helvetica", 15, "bold"),
            text_color=PRIMARY_BLUE,
        )
        logo_label.grid(row=0, column=0, sticky="w")

        reset_top_btn = ctk.CTkButton(
            bar,
            text="Reset Password",
            font=("Helvetica", 13, "bold"),
            text_color=WHITE,
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            width=140,
            height=32,
            corner_radius=6,
            command=self.handle_reset_password,
        )
        reset_top_btn.grid(row=0, column=2, sticky="e")

    def _build_form(self, parent):
        form = ctk.CTkFrame(parent, fg_color="transparent")
        form.grid(row=1, column=0, sticky="nsew")
        form.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            form,
            text="Forgot Password?",
            font=("Helvetica", 30, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        title.grid(row=0, column=0, sticky="w", pady=(0, 8))

        subtitle = ctk.CTkLabel(
            form,
            text="Create a new password for your account.",
            font=("Helvetica", 14),
            text_color=TEXT_GRAY,
            anchor="w",
            wraplength=440,
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(0, 32))

        username_label = ctk.CTkLabel(
            form,
            text="Username",
            font=("Helvetica", 13, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        username_label.grid(row=2, column=0, sticky="w", pady=(0, 6))

        self.username_entry = ctk.CTkEntry(
            form,
            placeholder_text="Enter your username",
            font=("Helvetica", 14),
            height=48,
            corner_radius=8,
            border_color=BORDER_COLOR,
            fg_color=WHITE,
            text_color=TEXT_DARK,
            placeholder_text_color="#9CA3AF",
        )
        self.username_entry.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        pw_label = ctk.CTkLabel(
            form,
            text="New Password",
            font=("Helvetica", 13, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        pw_label.grid(row=4, column=0, sticky="w", pady=(0, 6))

        self.password_entry = ctk.CTkEntry(
            form,
            placeholder_text="Enter new password",
            font=("Helvetica", 14),
            height=48,
            corner_radius=8,
            border_color=BORDER_COLOR,
            fg_color=WHITE,
            text_color=TEXT_DARK,
            placeholder_text_color="#9CA3AF",
            show="•",
        )
        self.password_entry.grid(row=5, column=0, sticky="ew", pady=(0, 8))

        pw_toggle_frame = ctk.CTkFrame(form, fg_color="transparent")
        pw_toggle_frame.grid(row=6, column=0, sticky="w", pady=(0, 20))

        self.show_pw_check = ctk.CTkCheckBox(
            pw_toggle_frame,
            text="Show Password",
            font=("Helvetica", 13),
            text_color=TEXT_GRAY,
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            border_color=BORDER_COLOR,
            checkmark_color=WHITE,
            corner_radius=4,
            variable=self._pw_var,
            command=self.toggle_password_visibility,
        )
        self.show_pw_check.pack(side="left")

        confirm_label = ctk.CTkLabel(
            form,
            text="Confirm Password",
            font=("Helvetica", 13, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        confirm_label.grid(row=7, column=0, sticky="w", pady=(0, 6))

        self.confirm_entry = ctk.CTkEntry(
            form,
            placeholder_text="Re-enter new password",
            font=("Helvetica", 14),
            height=48,
            corner_radius=8,
            border_color=BORDER_COLOR,
            fg_color=WHITE,
            text_color=TEXT_DARK,
            placeholder_text_color="#9CA3AF",
            show="•",
        )
        self.confirm_entry.grid(row=8, column=0, sticky="ew", pady=(0, 8))

        confirm_toggle_frame = ctk.CTkFrame(form, fg_color="transparent")
        confirm_toggle_frame.grid(row=9, column=0, sticky="w", pady=(0, 28))

        self.show_confirm_check = ctk.CTkCheckBox(
            confirm_toggle_frame,
            text="Show Confirm Password",
            font=("Helvetica", 13),
            text_color=TEXT_GRAY,
            fg_color=PRIMARY_BLUE,
            hover_color=HOVER_BLUE,
            border_color=BORDER_COLOR,
            checkmark_color=WHITE,
            corner_radius=4,
            variable=self._confirm_var,
            command=self.toggle_confirm_password_visibility,
        )
        self.show_confirm_check.pack(side="left")

        notice = ctk.CTkFrame(
            form,
            fg_color=LIGHT_GRAY,
            corner_radius=8,
            border_width=1,
            border_color=SUBTLE_BORDER,
        )
        notice.grid(row=10, column=0, sticky="ew", pady=(0, 20))

        notice_title = ctk.CTkLabel(
            notice,
            text="⚠️  Security Notice",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        notice_title.pack(anchor="w", padx=16, pady=(12, 4))

        notice_body = ctk.CTkLabel(
            notice,
            text="Your new password must be at least 8 characters and different from your previous password.",
            font=("Helvetica", 12),
            text_color=TEXT_GRAY,
            anchor="w",
            wraplength=400,
        )
        notice_body.pack(anchor="w", padx=16, pady=(0, 12))

    def _build_footer(self, parent):
        footer = ctk.CTkFrame(parent, fg_color="transparent")
        footer.grid(row=2, column=0, sticky="ew", pady=(24, 0))
        footer.grid_columnconfigure(0, weight=1)

        inner = ctk.CTkFrame(footer, fg_color="transparent")
        inner.grid(row=0, column=0)

        remember_label = ctk.CTkLabel(
            inner,
            text="Remember your password?",
            font=("Helvetica", 14),
            text_color=TEXT_GRAY,
        )
        remember_label.pack(side="left")

        login_btn = ctk.CTkButton(
            inner,
            text=" Login",
            font=("Helvetica", 14, "bold"),
            text_color=PRIMARY_BLUE,
            fg_color="transparent",
            hover=False,
            width=54,
            height=28,
            command=self.handle_back_to_login,
        )
        login_btn.pack(side="left")

    def _build_right_panel(self):
        right_panel = ctk.CTkFrame(self, fg_color=PANEL_BG, corner_radius=0)
        right_panel.grid(row=0, column=1, sticky="nsew")
        right_panel.grid_rowconfigure(0, weight=1)
        right_panel.grid_columnconfigure(0, weight=1)

        content = ctk.CTkFrame(right_panel, fg_color="transparent")
        content.grid(row=0, column=0, sticky="nsew", padx=52, pady=60)
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(content, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 28))

        dash_title = ctk.CTkLabel(
            header_frame,
            text="Dashboard Overview",
            font=("Helvetica", 22, "bold"),
            text_color=TEXT_DARK,
            anchor="w",
        )
        dash_title.pack(anchor="w")

        dash_sub = ctk.CTkLabel(
            header_frame,
            text="Live snapshot of your institution",
            font=("Helvetica", 13),
            text_color=TEXT_GRAY,
            anchor="w",
        )
        dash_sub.pack(anchor="w", pady=(4, 0))

        cards_frame = ctk.CTkFrame(content, fg_color="transparent")
        cards_frame.grid(row=1, column=0, sticky="nsew")
        cards_frame.grid_columnconfigure(0, weight=1, uniform="card_col")
        cards_frame.grid_columnconfigure(1, weight=1, uniform="card_col")
        cards_frame.grid_rowconfigure(0, weight=1, uniform="card_row")
        cards_frame.grid_rowconfigure(1, weight=1, uniform="card_row")

        stat_data = [
            {"label": "Students",   "value": "1,250", "icon": "👥", "row": 0, "col": 0},
            {"label": "Courses",    "value": "24",    "icon": "📚", "row": 0, "col": 1},
            {"label": "Teachers",   "value": "45",    "icon": "🧑‍🏫", "row": 1, "col": 0},
            {"label": "Attendance", "value": "92%",   "icon": "📊", "row": 1, "col": 1},
        ]

        for s in stat_data:
            card = ctk.CTkFrame(
                cards_frame,
                fg_color=WHITE,
                corner_radius=14,
                border_width=1,
                border_color=SUBTLE_BORDER,
            )
            card.grid(row=s["row"], column=s["col"], padx=10, pady=10, sticky="nsew")
            card.grid_rowconfigure(0, weight=1)
            card.grid_columnconfigure(0, weight=1)

            card_inner = ctk.CTkFrame(card, fg_color="transparent")
            card_inner.grid(row=0, column=0, sticky="nsew", padx=22, pady=22)

            icon_label = ctk.CTkLabel(
                card_inner,
                text=s["icon"],
                font=("Helvetica", 26),
                text_color=PRIMARY_BLUE,
                anchor="w",
            )
            icon_label.pack(anchor="w", pady=(0, 10))

            value_label = ctk.CTkLabel(
                card_inner,
                text=s["value"],
                font=("Helvetica", 30, "bold"),
                text_color=TEXT_DARK,
                anchor="w",
            )
            value_label.pack(anchor="w", pady=(0, 4))

            name_label = ctk.CTkLabel(
                card_inner,
                text=s["label"],
                font=("Helvetica", 13),
                text_color=TEXT_GRAY,
                anchor="w",
            )
            name_label.pack(anchor="w")

        divider = ctk.CTkFrame(content, fg_color=SUBTLE_BORDER, height=1, corner_radius=0)
        divider.grid(row=2, column=0, sticky="ew", pady=(28, 20))

        info_row = ctk.CTkFrame(content, fg_color="transparent")
        info_row.grid(row=3, column=0, sticky="ew")
        info_row.grid_columnconfigure(0, weight=1)
        info_row.grid_columnconfigure(1, weight=1)

        info_items = [
            ("🏫  Campus",   "Main Campus"),
            ("📅  Semester", "2024 – Spring"),
        ]

        for idx, (key, val) in enumerate(info_items):
            item_frame = ctk.CTkFrame(info_row, fg_color="transparent")
            item_frame.grid(row=0, column=idx, sticky="w", padx=(0, 20))

            key_label = ctk.CTkLabel(
                item_frame,
                text=key,
                font=("Helvetica", 12),
                text_color=TEXT_GRAY,
                anchor="w",
            )
            key_label.pack(anchor="w")

            val_label = ctk.CTkLabel(
                item_frame,
                text=val,
                font=("Helvetica", 13, "bold"),
                text_color=TEXT_DARK,
                anchor="w",
            )
            val_label.pack(anchor="w", pady=(2, 0))

    def handle_reset_password(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()

        if not username or not password or not confirm:
            messagebox.showwarning(
                "Warning",
                "Please fill in all fields."
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        from backend.auth import reset_password
        success = reset_password(username, password)

        if not success:
            messagebox.showerror(
                "Error",
                "Username not found."
            )
            return

        messagebox.showinfo(
            "Success",
            "Password updated successfully."
        )
        self.handle_back_to_login()

    def handle_back_to_login(self):
        self.destroy()
        if self.on_back:
            self.on_back()

    def toggle_password_visibility(self):
        self._show_password = self._pw_var.get()
        self.password_entry.configure(show="" if self._show_password else "•")

    def toggle_confirm_password_visibility(self):
        self._show_confirm = self._confirm_var.get()
        self.confirm_entry.configure(show="" if self._show_confirm else "•")


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Student Management System – Forgot Password")
    root.configure(fg_color=BACKGROUND)
    root.after(100, lambda: root.state("zoomed"))
    app = ForgotPasswordPage(root)
    root.mainloop()
