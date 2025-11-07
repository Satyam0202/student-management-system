import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
from datetime import date, datetime
import csv
import json
from PIL import Image, ImageTk
import os

class StudentManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.load_initial_data()
        
    def setup_window(self):
        """Configure main window properties"""
        self.root.title("College Student Management System - Professional Edition")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)
        self.root.config(bg="#f8f9fa")
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")
        
    def setup_styles(self):
        """Configure ttk styles for professional appearance"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom styles
        self.style.configure('Header.TLabel', 
                           font=('Segoe UI', 20, 'bold'),
                           background='#2c3e50',
                           foreground='white')
        
        self.style.configure('Custom.TButton',
                           font=('Segoe UI', 10),
                           padding=10)
        
        self.style.configure('Treeview.Heading',
                           font=('Segoe UI', 10, 'bold'))
        
    def connect_db(self):
        """Establish database connection with error handling"""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="0202",
                database="project_sql"
            )
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Connection failed: {str(e)}")
            return None
            
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        self.create_header()
        self.create_notebook()
        self.create_student_form()
        self.create_records_view()
        self.create_analytics_tab()
        self.create_settings_tab()
        self.create_footer()
        
    def create_header(self):
        """Create application header"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame,
                              text="COLLEGE STUDENT MANAGEMENT SYSTEM",
                              font=("Segoe UI", 20, "bold"),
                              bg="#2c3e50",
                              fg="white")
        title_label.pack(pady=20)
        
    def create_notebook(self):
        """Create tabbed interface"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create tabs
        self.student_tab = ttk.Frame(self.notebook)
        self.records_tab = ttk.Frame(self.notebook)
        self.analytics_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.student_tab, text="Student Management")
        self.notebook.add(self.records_tab, text="Records & Search")
        self.notebook.add(self.analytics_tab, text="Analytics")
        self.notebook.add(self.settings_tab, text="Settings") 
       
    def create_student_form(self):
        """Create student form in the first tab"""
        # Main container
        main_frame = tk.Frame(self.student_tab, bg="#f8f9fa")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Form frame
        form_frame = tk.LabelFrame(main_frame, 
                                  text="Student Information", 
                                  font=("Segoe UI", 12, "bold"),
                                  bg="#ffffff",
                                  relief="solid",
                                  bd=1,
                                  padx=20,
                                  pady=15)
        form_frame.pack(fill="x", pady=(0, 20))
        
        # Form fields - match your database structure
        fields = [
            ("Name:", "name"),
            ("Roll Number:", "roll"),
            ("Course:", "course"),
            ("Semester:", "semester"),
            ("Fees Paid:", "fees"),
            ("Phone:", "phone"),
            ("Email:", "email"),
            ("Address:", "address")
        ]
        
        self.entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            row = i // 2
            col = (i % 2) * 3
            
            tk.Label(form_frame, 
                    text=label_text, 
                    font=("Segoe UI", 10),
                    bg="#ffffff").grid(row=row, column=col, sticky="e", padx=(0, 10), pady=8)
            
            if field_name == "address":
                entry = tk.Text(form_frame, width=25, height=3, font=("Segoe UI", 10))
            else:
                entry = tk.Entry(form_frame, width=25, font=("Segoe UI", 10))
            
            entry.grid(row=row, column=col+1, pady=8, padx=(0, 20))
            self.entries[field_name] = entry
        
        # Buttons frame
        button_frame = tk.Frame(form_frame, bg="#ffffff")
        button_frame.grid(row=len(fields)//2 + 1, column=0, columnspan=6, pady=20)
        
        buttons = [
            ("Add Student", self.insert_student, "#27ae60"),
            ("Update Student", self.update_student, "#3498db"),
            ("Delete Student", self.delete_student, "#e74c3c"),
            ("Clear Fields", self.clear_fields, "#95a5a6")
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(button_frame,
                           text=text,
                           command=command,
                           bg=color,
                           fg="white",
                           font=("Segoe UI", 10, "bold"),
                           width=12,
                           relief="flat",
                           cursor="hand2")
            btn.pack(side="left", padx=10)
            
    def create_records_view(self):
        """Create records view in the second tab"""
        # Search frame
        search_frame = tk.LabelFrame(self.records_tab,
                                   text="Search & Filter",
                                   font=("Segoe UI", 12, "bold"),
                                   bg="#ffffff",
                                   relief="solid",
                                   bd=1,
                                   padx=15,
                                   pady=10)
        search_frame.pack(fill="x", padx=20, pady=20)
        
        # Search controls
        tk.Label(search_frame, text="Search:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=30, font=("Segoe UI", 10))
        search_entry.grid(row=0, column=1, padx=5, pady=5)
        search_entry.bind('<KeyRelease>', lambda e: self.search_student())
        
        # Filter by course
        tk.Label(search_frame, text="Course:", font=("Segoe UI", 10), bg="#ffffff").grid(row=0, column=2, padx=5, pady=5)
        
        self.course_filter = ttk.Combobox(search_frame, width=15, font=("Segoe UI", 10))
        self.course_filter.grid(row=0, column=3, padx=5, pady=5)
        self.course_filter.bind('<<ComboboxSelected>>', lambda e: self.filter_by_course())
        
        # Action buttons
        btn_frame = tk.Frame(search_frame, bg="#ffffff")
        btn_frame.grid(row=0, column=4, padx=20)
        
        tk.Button(btn_frame, text="Refresh", command=self.refresh_data,
                 bg="#3498db", fg="white", font=("Segoe UI", 9), width=8).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Export CSV", command=self.export_to_csv,
                 bg="#27ae60", fg="white", font=("Segoe UI", 9), width=8).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Import CSV", command=self.import_from_csv,
                 bg="#f39c12", fg="white", font=("Segoe UI", 9), width=8).pack(side="left", padx=2)
        
        # Treeview frame
        tree_frame = tk.Frame(self.records_tab, bg="#ffffff", relief="solid", bd=1)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Scrollbars
        v_scroll = ttk.Scrollbar(tree_frame, orient="vertical")
        h_scroll = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Treeview - match your actual database structure
        columns = ("ID", "Name", "Roll", "Course", "Semester", "Fees", "Phone", "Email", "Address", "Date", "Created")
        self.tree = ttk.Treeview(tree_frame, 
                                columns=columns, 
                                show="headings",
                                yscrollcommand=v_scroll.set,
                                xscrollcommand=h_scroll.set)
        
        # Configure scrollbars
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)
        
        # Pack scrollbars and treeview
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        self.tree.pack(fill="both", expand=True)
        
        # Configure columns to match your database
        column_widths = {"ID": 50, "Name": 120, "Roll": 80, "Course": 120, 
                        "Semester": 80, "Fees": 80, "Phone": 100, "Email": 140, 
                        "Address": 120, "Date": 100, "Created": 120}
        
        for col in columns:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, anchor="center", width=column_widths.get(col, 100))
        
        # Bind double-click event
        self.tree.bind("<Double-1>", self.on_record_select)   
     
    def create_analytics_tab(self):
        """Create analytics dashboard"""
        analytics_frame = tk.Frame(self.analytics_tab, bg="#f8f9fa")
        analytics_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Statistics frame
        stats_frame = tk.LabelFrame(analytics_frame,
                                  text="Statistics Overview",
                                  font=("Segoe UI", 12, "bold"),
                                  bg="#ffffff",
                                  relief="solid",
                                  bd=1,
                                  padx=15,
                                  pady=15)
        stats_frame.pack(fill="x", pady=(0, 20))
        
        # Create statistics cards
        self.create_stat_cards(stats_frame)
        
        # Charts frame (placeholder for future implementation)
        charts_frame = tk.LabelFrame(analytics_frame,
                                   text="Visual Analytics",
                                   font=("Segoe UI", 12, "bold"),
                                   bg="#ffffff",
                                   relief="solid",
                                   bd=1,
                                   padx=15,
                                   pady=15)
        charts_frame.pack(fill="both", expand=True)
        
        tk.Label(charts_frame, 
                text="📊 Charts and graphs will be displayed here\n(Future implementation with matplotlib)",
                font=("Segoe UI", 12),
                bg="#ffffff",
                fg="#7f8c8d").pack(expand=True)
        
    def create_stat_cards(self, parent):
        """Create statistics cards"""
        cards_frame = tk.Frame(parent, bg="#ffffff")
        cards_frame.pack(fill="x")
        
        # Statistics data
        self.stat_labels = {}
        stats = [
            ("Total Students", "total_students", "#3498db"),
            ("Total Courses", "total_courses", "#27ae60"),
            ("Fees Collected", "total_fees", "#f39c12"),
            ("This Month", "monthly_admissions", "#e74c3c")
        ]
        
        for i, (title, key, color) in enumerate(stats):
            card = tk.Frame(cards_frame, bg=color, relief="solid", bd=1)
            card.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            
            tk.Label(card, text=title, font=("Segoe UI", 10, "bold"), 
                    bg=color, fg="white").pack(pady=(10, 5))
            
            value_label = tk.Label(card, text="0", font=("Segoe UI", 16, "bold"), 
                                 bg=color, fg="white")
            value_label.pack(pady=(0, 10))
            
            self.stat_labels[key] = value_label
            
    def create_settings_tab(self):
        """Create settings and configuration tab"""
        settings_frame = tk.Frame(self.settings_tab, bg="#f8f9fa")
        settings_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Database settings
        db_frame = tk.LabelFrame(settings_frame,
                               text="Database Configuration",
                               font=("Segoe UI", 12, "bold"),
                               bg="#ffffff",
                               relief="solid",
                               bd=1,
                               padx=15,
                               pady=15)
        db_frame.pack(fill="x", pady=(0, 20))
        
        # Database connection test
        tk.Button(db_frame, text="Test Database Connection", 
                 command=self.test_db_connection,
                 bg="#3498db", fg="white", font=("Segoe UI", 10)).pack(pady=10)
        
        # Backup and restore
        backup_frame = tk.LabelFrame(settings_frame,
                                   text="Backup & Restore",
                                   font=("Segoe UI", 12, "bold"),
                                   bg="#ffffff",
                                   relief="solid",
                                   bd=1,
                                   padx=15,
                                   pady=15)
        backup_frame.pack(fill="x", pady=(0, 20))
        
        tk.Button(backup_frame, text="Backup Database", 
                 command=self.backup_database,
                 bg="#27ae60", fg="white", font=("Segoe UI", 10)).pack(side="left", padx=10, pady=10)
        
        tk.Button(backup_frame, text="Restore Database", 
                 command=self.restore_database,
                 bg="#e74c3c", fg="white", font=("Segoe UI", 10)).pack(side="left", padx=10, pady=10)
        
    def create_footer(self):
        """Create application footer"""
        footer_frame = tk.Frame(self.root, bg="#2c3e50", height=40)
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)
        
        tk.Label(footer_frame,
                text="Developed by Satyam Kumar (25MCA20346) | Professional Student Management System",
                bg="#2c3e50",
                fg="white",
                font=("Segoe UI", 9)).pack(pady=10) 
   # ============== DATABASE OPERATIONS ==============
    
    def insert_student(self):
        """Insert new student with validation"""
        # Get values from form
        values = self.get_form_values()
        
        # Validate required fields
        required_fields = ['name', 'roll', 'course', 'semester', 'fees']
        for field in required_fields:
            if not values[field].strip():
                messagebox.showerror("Validation Error", f"{field.title()} is required!")
                return
        
        # Validate fees (should be numeric)
        try:
            float(values['fees'])
        except ValueError:
            messagebox.showerror("Validation Error", "Fees must be a valid number!")
            return
        
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                # Use enhanced table structure
                query = """INSERT INTO students (name, roll, course, semester, fees, phone, email, address, date) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                cur.execute(query, (
                    values['name'], values['roll'], values['course'], 
                    values['semester'], values['fees'], values['phone'],
                    values['email'], values['address'], date.today()
                ))
                
                con.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                self.clear_fields()
                self.show_students()
                self.update_statistics()
                
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Roll number already exists!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to insert student: {str(e)}")
            finally:
                con.close()
    
    def update_student(self):
        """Update selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to update!")
            return
        
        # Get ID from selected row (ID is at index 0)
        student_id = self.tree.item(selected[0])['values'][0]
        values = self.get_form_values()
        
        # Validate required fields
        required_fields = ['name', 'roll', 'course', 'semester', 'fees']
        for field in required_fields:
            if not values[field].strip():
                messagebox.showerror("Validation Error", f"{field.title()} is required!")
                return
        
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                query = """UPDATE students SET 
                          name=%s, roll=%s, course=%s, semester=%s, fees=%s, 
                          phone=%s, email=%s, address=%s 
                          WHERE id=%s"""
                
                cur.execute(query, (
                    values['name'], values['roll'], values['course'],
                    values['semester'], values['fees'], values['phone'],
                    values['email'], values['address'], student_id
                ))
                
                con.commit()
                messagebox.showinfo("Success", "Student updated successfully!")
                self.clear_fields()
                self.show_students()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update student: {str(e)}")
            finally:
                con.close()
    
    def delete_student(self):
        """Delete selected student"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a student to delete!")
            return
        
        # Confirm deletion
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?"):
            student_id = self.tree.item(selected[0])['values'][0]  # ID is at index 0
            
            con = self.connect_db()
            if con:
                try:
                    cur = con.cursor()
                    cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
                    con.commit()
                    messagebox.showinfo("Success", "Student deleted successfully!")
                    self.show_students()
                    self.update_statistics()
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete student: {str(e)}")
                finally:
                    con.close()
    
    def show_students(self):
        """Display all students in treeview"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                # Check if table has id column, if not use roll as identifier
                cur.execute("DESCRIBE students")
                columns = [row[0] for row in cur.fetchall()]
                
                if 'id' in columns:
                    cur.execute("SELECT * FROM students ORDER BY id DESC")
                else:
                    cur.execute("SELECT * FROM students ORDER BY roll")
                
                for row in cur.fetchall():
                    self.tree.insert("", "end", values=row)
                
                # Update course filter
                self.update_course_filter()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load students: {str(e)}")
            finally:
                con.close()
    
    def search_student(self):
        """Search students by name or roll number"""
        query = self.search_var.get().strip()
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                if query:
                    cur.execute("""SELECT * FROM students 
                                  WHERE name LIKE %s OR roll LIKE %s OR course LIKE %s
                                  ORDER BY roll""", 
                               (f"%{query}%", f"%{query}%", f"%{query}%"))
                else:
                    cur.execute("SELECT * FROM students ORDER BY roll")
                
                for row in cur.fetchall():
                    self.tree.insert("", "end", values=row)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Search failed: {str(e)}")
            finally:
                con.close()    

    def filter_by_course(self):
        """Filter students by selected course"""
        course = self.course_filter.get()
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                if course and course != "All Courses":
                    cur.execute("SELECT * FROM students WHERE course=%s ORDER BY roll", (course,))
                else:
                    cur.execute("SELECT * FROM students ORDER BY roll")
                
                for row in cur.fetchall():
                    self.tree.insert("", "end", values=row)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Filter failed: {str(e)}")
            finally:
                con.close()
    
    # ============== UTILITY FUNCTIONS ==============
    
    def get_form_values(self):
        """Get all form field values"""
        values = {}
        for field, entry in self.entries.items():
            if field == "address":
                values[field] = entry.get("1.0", tk.END).strip()
            else:
                values[field] = entry.get().strip()
        return values
    
    def clear_fields(self):
        """Clear all form fields"""
        for field, entry in self.entries.items():
            if field == "address":
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)
    
    def refresh_data(self):
        """Refresh all data"""
        self.search_var.set("")
        self.course_filter.set("")
        self.show_students()
        self.update_statistics()
    
    def on_record_select(self, event):
        """Handle record selection in treeview"""
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            
            # Switch to student management tab
            self.notebook.select(0)
            
            # Populate form fields - match database structure (skip ID at index 0)
            fields = ['name', 'roll', 'course', 'semester', 'fees', 'phone', 'email', 'address']
            for i, field in enumerate(fields):
                if i + 1 < len(values):  # Skip ID field at index 0
                    if field == "address":
                        self.entries[field].delete("1.0", tk.END)
                        self.entries[field].insert("1.0", str(values[i + 1]) if values[i + 1] else "")
                    else:
                        self.entries[field].delete(0, tk.END)
                        self.entries[field].insert(0, str(values[i + 1]) if values[i + 1] else "")
    
    def update_course_filter(self):
        """Update course filter dropdown"""
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                cur.execute("SELECT DISTINCT course FROM students ORDER BY course")
                courses = ["All Courses"] + [row[0] for row in cur.fetchall()]
                self.course_filter['values'] = courses
                if not self.course_filter.get():
                    self.course_filter.set("All Courses")
            except Exception as e:
                print(f"Failed to update course filter: {str(e)}")
            finally:
                con.close()
    
    def update_statistics(self):
        """Update statistics in analytics tab"""
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                
                # Total students
                cur.execute("SELECT COUNT(*) FROM students")
                total_students = cur.fetchone()[0]
                self.stat_labels['total_students'].config(text=str(total_students))
                
                # Total courses
                cur.execute("SELECT COUNT(DISTINCT course) FROM students")
                total_courses = cur.fetchone()[0]
                self.stat_labels['total_courses'].config(text=str(total_courses))
                
                # Total fees collected
                cur.execute("SELECT SUM(fees) FROM students")
                total_fees = cur.fetchone()[0] or 0
                self.stat_labels['total_fees'].config(text=f"₹{total_fees:,.0f}")
                
                # Monthly admissions
                cur.execute("""SELECT COUNT(*) FROM students 
                              WHERE MONTH(date) = MONTH(CURDATE()) 
                              AND YEAR(date) = YEAR(CURDATE())""")
                monthly = cur.fetchone()[0]
                self.stat_labels['monthly_admissions'].config(text=str(monthly))
                
            except Exception as e:
                print(f"Failed to update statistics: {str(e)}")
            finally:
                con.close()
    
    # ============== IMPORT/EXPORT FUNCTIONS ==============
    
    def export_to_csv(self):
        """Export student data to CSV file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Save student data as CSV"
            )
            
            if filename:
                con = self.connect_db()
                if con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM students")
                    
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        # Write header
                        writer.writerow(['ID', 'Name', 'Roll', 'Course', 'Semester', 
                                       'Fees', 'Phone', 'Email', 'Address', 'Date'])
                        # Write data
                        writer.writerows(cur.fetchall())
                    
                    con.close()
                    messagebox.showinfo("Success", f"Data exported successfully to {filename}")
                    
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export data: {str(e)}")
    
    def import_from_csv(self):
        """Import student data from CSV file"""
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Select CSV file to import"
            )
            
            if filename:
                con = self.connect_db()
                if con:
                    cur = con.cursor()
                    imported_count = 0
                    
                    with open(filename, 'r', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        
                        for row in reader:
                            try:
                                cur.execute("""INSERT INTO students 
                                              (name, roll, course, semester, fees, phone, email, address, date) 
                                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                           (row.get('Name', ''), row.get('Roll', ''), 
                                            row.get('Course', ''), row.get('Semester', ''),
                                            row.get('Fees', 0), row.get('Phone', ''),
                                            row.get('Email', ''), row.get('Address', ''),
                                            row.get('Date', date.today())))
                                imported_count += 1
                            except mysql.connector.IntegrityError:
                                continue  # Skip duplicate roll numbers
                    
                    con.commit()
                    con.close()
                    
                    messagebox.showinfo("Success", f"Imported {imported_count} students successfully!")
                    self.show_students()
                    self.update_statistics()
                    
        except Exception as e:
            messagebox.showerror("Import Error", f"Failed to import data: {str(e)}")  
  
    # ============== SETTINGS FUNCTIONS ==============
    
    def test_db_connection(self):
        """Test database connection"""
        con = self.connect_db()
        if con:
            try:
                cur = con.cursor()
                cur.execute("SELECT 1")
                messagebox.showinfo("Connection Test", "Database connection successful!")
                con.close()
            except Exception as e:
                messagebox.showerror("Connection Test", f"Connection failed: {str(e)}")
        else:
            messagebox.showerror("Connection Test", "Failed to connect to database!")
    
    def backup_database(self):
        """Backup database to JSON file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Save database backup"
            )
            
            if filename:
                con = self.connect_db()
                if con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM students")
                    
                    # Convert data to JSON format
                    columns = [desc[0] for desc in cur.description]
                    data = []
                    for row in cur.fetchall():
                        row_dict = {}
                        for i, value in enumerate(row):
                            if isinstance(value, date):
                                row_dict[columns[i]] = value.isoformat()
                            else:
                                row_dict[columns[i]] = value
                        data.append(row_dict)
                    
                    # Save to file
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump({
                            'backup_date': datetime.now().isoformat(),
                            'total_records': len(data),
                            'data': data
                        }, f, indent=2, ensure_ascii=False)
                    
                    con.close()
                    messagebox.showinfo("Backup", f"Database backed up successfully to {filename}")
                    
        except Exception as e:
            messagebox.showerror("Backup Error", f"Failed to backup database: {str(e)}")
    
    def restore_database(self):
        """Restore database from JSON backup"""
        if messagebox.askyesno("Confirm Restore", 
                              "This will replace all existing data. Are you sure?"):
            try:
                filename = filedialog.askopenfilename(
                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                    title="Select backup file to restore"
                )
                
                if filename:
                    con = self.connect_db()
                    if con:
                        cur = con.cursor()
                        
                        # Clear existing data
                        cur.execute("DELETE FROM students")
                        
                        # Load backup data
                        with open(filename, 'r', encoding='utf-8') as f:
                            backup_data = json.load(f)
                        
                        # Insert data
                        restored_count = 0
                        for record in backup_data['data']:
                            try:
                                cur.execute("""INSERT INTO students 
                                              (name, roll, course, semester, fees, phone, email, address, date) 
                                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                           (record.get('name', ''), record.get('roll', ''),
                                            record.get('course', ''), record.get('semester', ''),
                                            record.get('fees', 0), record.get('phone', ''),
                                            record.get('email', ''), record.get('address', ''),
                                            record.get('date', date.today())))
                                restored_count += 1
                            except Exception:
                                continue
                        
                        con.commit()
                        con.close()
                        
                        messagebox.showinfo("Restore", f"Restored {restored_count} records successfully!")
                        self.show_students()
                        self.update_statistics()
                        
            except Exception as e:
                messagebox.showerror("Restore Error", f"Failed to restore database: {str(e)}")
    
    def load_initial_data(self):
        """Load initial data when application starts"""
        self.show_students()
        self.update_statistics()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# ============== DATABASE SETUP ==============
def setup_database():
    """Create database and table if they don't exist"""
    try:
        # Connect without specifying database
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0202"
        )
        
        cur = con.cursor()
        
        # Create database if not exists
        cur.execute("CREATE DATABASE IF NOT EXISTS project_sql")
        cur.execute("USE project_sql")
        
        # Create table with enhanced structure
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                roll VARCHAR(20) UNIQUE NOT NULL,
                course VARCHAR(50) NOT NULL,
                semester VARCHAR(10) NOT NULL,
                fees DECIMAL(10,2) NOT NULL,
                phone VARCHAR(15),
                email VARCHAR(100),
                address TEXT,
                date DATE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)
        
        con.commit()
        con.close()
        print("Database setup completed successfully!")
        
    except Exception as e:
        print(f"Database setup failed: {str(e)}")

# ============== MAIN EXECUTION ==============
if __name__ == "__main__":
    # Setup database first
    setup_database()
    
    # Create and run application
    app = StudentManagementSystem()
    app.run()