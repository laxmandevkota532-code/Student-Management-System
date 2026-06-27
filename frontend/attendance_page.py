import customtkinter as ctk
from datetime import datetime

class AttendancePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#F8F9FC")
        
        # Configure page grid layout as required
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        # Sample Attendance Data
        self.attendance_data = [
            {"id": "STU001", "name": "Alice Johnson", "course": "Computer Science 101", "date": "2026-03-30", "status": "Present"},
            {"id": "STU002", "name": "Bob Smith", "course": "Computer Science 101", "date": "2026-03-30", "status": "Absent"},
            {"id": "STU003", "name": "Charlie Brown", "course": "Mathematics II", "date": "2026-03-30", "status": "Late"},
            {"id": "STU004", "name": "Diana Prince", "course": "Physics I", "date": "2026-03-30", "status": "Present"},
            {"id": "STU005", "name": "Ethan Hunt", "course": "Computer Science 101", "date": "2026-03-30", "status": "Present"},
        ]
        
        self.create_header()
        self.create_summary_cards()
        self.create_controls()
        self.create_attendance_table()
        
    def create_header(self):
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, padx=30, pady=(30, 20), sticky="ew")
        header_frame.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(
            header_frame, 
            text="Attendance Management", 
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"), 
            text_color="#1E293B"
        )
        title.grid(row=0, column=0, sticky="w")
        
    def create_summary_cards(self):
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.grid(row=1, column=0, padx=30, pady=10, sticky="ew")
        
        for i in range(4):
            cards_frame.grid_columnconfigure(i, weight=1)
            
        metrics = [
            {"title": "Total Students", "value": "124", "color": "#4F46E5"},
            {"title": "Present Today", "value": "112", "color": "#10B981"},
            {"title": "Absent Today", "value": "8", "color": "#EF4444"},
            {"title": "Late Today", "value": "4", "color": "#F59E0B"}
        ]
        
        for idx, metric in enumerate(metrics):
            card = ctk.CTkFrame(cards_frame, fg_color="#FFFFFF", corner_radius=10, border_width=1, border_color="#E2E8F0")
            card.grid(row=0, column=idx, padx=(0 if idx==0 else 10, 0 if idx==3 else 10), sticky="nsew")
            card.grid_columnconfigure(0, weight=1)
            
            lbl_title = ctk.CTkLabel(card, text=metric["title"], font=ctk.CTkFont(family="Arial", size=13), text_color="#64748B")
            lbl_title.grid(row=0, column=0, padx=15, pady=(15, 5), sticky="w")
            
            lbl_val = ctk.CTkLabel(card, text=metric["value"], font=ctk.CTkFont(family="Arial", size=22, weight="bold"), text_color=metric["color"])
            lbl_val.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")
            
    def create_controls(self):
        controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        controls_frame.grid(row=2, column=0, padx=30, pady=20, sticky="ew")
        controls_frame.grid_columnconfigure(0, weight=1)
        
        self.search_bar = ctk.CTkEntry(
            controls_frame, 
            placeholder_text="Search student by name or ID...", 
            width=300, 
            height=38, 
            fg_color="#FFFFFF", 
            border_color="#CBD5E1", 
            text_color="#1E293B"
        )
        self.search_bar.grid(row=0, column=0, sticky="w")
        
        right_controls = ctk.CTkFrame(controls_frame, fg_color="transparent")
        right_controls.grid(row=0, column=1, sticky="e")
        
        self.course_dropdown = ctk.CTkComboBox(
            right_controls, 
            values=["All Courses", "Computer Science 101", "Mathematics II", "Physics I"],
            width=180, 
            height=38, 
            fg_color="#FFFFFF", 
            border_color="#CBD5E1", 
            text_color="#1E293B"
        )
        self.course_dropdown.grid(row=0, column=0, padx=10)
        
        self.date_field = ctk.CTkEntry(
            right_controls, 
            width=120, 
            height=38, 
            fg_color="#FFFFFF", 
            border_color="#CBD5E1", 
            text_color="#1E293B"
        )
        self.date_field.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.date_field.grid(row=0, column=1, padx=10)
        
        self.mark_attendance_btn = ctk.CTkButton(
            right_controls, 
            text="Mark Attendance", 
            height=38, 
            fg_color="#4F46E5", 
            hover_color="#4338CA", 
            font=ctk.CTkFont(family="Arial", size=13, weight="bold")
        )
        self.mark_attendance_btn.grid(row=0, column=2, padx=(10, 0))
        
    def create_attendance_table(self):
        table_container = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=10, border_width=1, border_color="#E2E8F0")
        table_container.grid(row=3, column=0, padx=30, pady=(0, 30), sticky="nsew")
        table_container.grid_columnconfigure(0, weight=1)
        table_container.grid_rowconfigure(1, weight=1)
        
        headers_frame = ctk.CTkFrame(table_container, fg_color="#F1F5F9", height=40, corner_radius=0)
        headers_frame.grid(row=0, column=0, sticky="ew")
        headers_frame.grid_propagate(False)
        
        headers = ["Student ID", "Name", "Course", "Date", "Status", "Actions"]
        widths = [120, 200, 220, 120, 120, 100]
        
        for idx, header in enumerate(headers):
            lbl = ctk.CTkLabel(
                headers_frame, 
                text=header, 
                font=ctk.CTkFont(family="Arial", size=13, weight="bold"), 
                text_color="#475569"
            )
            lbl.grid(row=0, column=idx, padx=15, pady=8, sticky="w")
            
        for idx, width in enumerate(widths):
            headers_frame.grid_columnconfigure(idx, minsize=width)
            
        self.scrollable_table = ctk.CTkScrollableFrame(table_container, fg_color="transparent", corner_radius=0)
        self.scrollable_table.grid(row=1, column=0, sticky="nsew")
        
        for idx, width in enumerate(widths):
            self.scrollable_table.grid_columnconfigure(idx, minsize=width)
            
        self.populate_table_data()
        
    def populate_table_data(self):
        for row_idx, record in enumerate(self.attendance_data):
            row_bg = "#FFFFFF" if row_idx % 2 == 0 else "#F8FAFC"
            
            row_frame = ctk.CTkFrame(self.scrollable_table, fg_color=row_bg, corner_radius=0, height=45)
            row_frame.grid(row=row_idx, column=0, columnspan=6, sticky="ew")
            row_frame.grid_propagate(False)
            
            widths = [120, 200, 220, 120, 120, 100]
            for idx, width in enumerate(widths):
                row_frame.grid_columnconfigure(idx, minsize=width)
                
            ctk.CTkLabel(row_frame, text=record["id"], font=ctk.CTkFont(family="Arial", size=13), text_color="#1E293B").grid(row=0, column=0, padx=15, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=record["name"], font=ctk.CTkFont(family="Arial", size=13, weight="bold"), text_color="#1E293B").grid(row=0, column=1, padx=15, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=record["course"], font=ctk.CTkFont(family="Arial", size=13), text_color="#475569").grid(row=0, column=2, padx=15, pady=10, sticky="w")
            ctk.CTkLabel(row_frame, text=record["date"], font=ctk.CTkFont(family="Arial", size=13), text_color="#475569").grid(row=0, column=3, padx=15, pady=10, sticky="w")
            
            status_colors = {
                "Present": {"bg": "#DCFCE7", "txt": "#15803D"},
                "Absent": {"bg": "#FEE2E2", "txt": "#B91C1C"},
                "Late": {"bg": "#FEF3C7", "txt": "#B45309"}
            }
            colors = status_colors.get(record["status"], {"bg": "#E2E8F0", "txt": "#475569"})
            
            status_badge = ctk.CTkLabel(
                row_frame, 
                text=record["status"], 
                font=ctk.CTkFont(family="Arial", size=11, weight="bold"),
                fg_color=colors["bg"], 
                text_color=colors["txt"],
                corner_radius=6,
                width=75,
                height=24
            )
            status_badge.grid(row=0, column=4, padx=15, pady=10, sticky="w")
            
            edit_btn = ctk.CTkButton(
                row_frame, 
                text="Edit", 
                width=60, 
                height=26, 
                fg_color="#F1F5F9", 
                hover_color="#E2E8F0", 
                text_color="#475569",
                font=ctk.CTkFont(family="Arial", size=12)
            )
            edit_btn.grid(row=0, column=5, padx=15, pady=10, sticky="w")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x700")
    page = AttendancePage(root)
    page.pack(fill="both", expand=True)
    root.mainloop()