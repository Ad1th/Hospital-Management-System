import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adith666",
    database="lhospital"
)

# Function to handle doctor login
def doctor_login():
    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        cursor = db.cursor()
        cursor.execute("SELECT * FROM DoctorDetails WHERE Username = %s AND Password = %s", (username, password))
        doctor_data = cursor.fetchone()
        cursor.close()

        if doctor_data:
            # Redirect to doctor's page with their ID
            doctor_page(doctor_data[0])
            login_window.destroy()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    # Create a login window
    login_window = tk.Toplevel(root)
    login_window.title("Doctor Login")
    login_window.geometry("800x600")  # Set the window size to fullscreen

    login_frame = tk.Frame(login_window)
    login_frame.pack(expand=True, fill='both')
    login_frame.configure(bg="#FFFACD")  # Set background color to light cream

    login_label = tk.Label(login_frame, text="Doctor Login", font=("Arial", 20))
    login_label.pack(pady=20)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_frame)
    username_entry.pack()

    password_label = tk.Label(login_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_frame, show="*")  # Show asterisks for password input
    password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command=check_login)
    login_button.pack()

# Function to handle patient login
def patient_login():
    def check_patient_login():
        username = username_entry.get()
        password = password_entry.get()

        cursor = db.cursor()
        cursor.execute("SELECT * FROM PatientDetails WHERE Username = %s AND Password = %s", (username, password))
        patient_data = cursor.fetchone()
        cursor.close()

        if patient_data:
            # Redirect to patient's page with their ID
            patient_page(patient_data[0])
            login_window.destroy()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    # Create a login window
    login_window = tk.Toplevel(root)
    login_window.title("Patient Login")
    login_window.geometry("800x600")  # Set the window size to fullscreen

    login_frame = tk.Frame(login_window)
    login_frame.pack(expand=True, fill='both')
    login_frame.configure(bg="#FFFACD")  # Set background color to light cream

    login_label = tk.Label(login_frame, text="Patient Login", font=("Arial", 20))
    login_label.pack(pady=20)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_frame)
    username_entry.pack()

    password_label = tk.Label(login_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_frame, show="*")  # Show asterisks for password input
    password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command=check_patient_login)
    login_button.pack()
# Function to handle admin login
def admin_login():
    def check_admin_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "lhospital" and password == "admin":
            # Redirect to admin's page
            admin_page()
            login_window.destroy()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    # Create a login window
    login_window = tk.Toplevel(root)
    login_window.title("Admin Login")
    login_window.geometry("800x600")

    login_frame = tk.Frame(login_window)
    login_frame.pack(expand=True, fill='both')
    login_frame.configure(bg="#FFFACD")

    login_label = tk.Label(login_frame, text="Admin Login", font=("Arial", 20))
    login_label.pack(pady=20)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_frame)
    username_entry.pack()

    password_label = tk.Label(login_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command=check_admin_login)
    login_button.pack()





def admin_page():
    cursor = db.cursor()
    def register_patient_tab(parent):
        def register_patient():
            cursor.execute('''
                INSERT INTO patientdetail (name, DOB, age, gender, address, phonenumber, bloodgroup, username, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (name_entry.get(), dob_entry.get(), age_entry.get(), gender_entry.get(),
                  address_entry.get(), phone_entry.get(), blood_group_entry.get(),
                  username_entry.get(), password_entry.get()))

            db.commit()
            confirmation_label.config(text="Patient registered successfully!")

        register_frame = ttk.Frame(parent)
        register_frame.pack(padx=10, pady=10)

        labels = ["Name", "Date of Birth (YYYY-MM-DD)", "Age", "Gender", "Address", "Phone", "Blood Group", "Username", "Password"]
        entries = [ttk.Entry(register_frame) for _ in range(len(labels))]
        confirmation_label = ttk.Label(register_frame, text="")

        for i, label in enumerate(labels):
            ttk.Label(register_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="E")
            entries[i].grid(row=i, column=1, padx=5, pady=5, sticky="W")

        ttk.Button(register_frame, text="Register", command=register_patient).grid(row=len(labels), columnspan=2, pady=10)
        confirmation_label.grid(row=len(labels) + 1, columnspan=2)

    def doctor_registration_tab(parent):
        def register_doctor():
            cursor.execute('''
                INSERT INTO doctordetails (Name, Dept1, Dept2, Dept3, Address, Phone_number1, Phone_number2,
                                           Qualifications, Gender, Username, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (name_entry.get(), dept1_entry.get(), dept2_entry.get(), dept3_entry.get(),
                  address_entry.get(), phone1_entry.get(), phone2_entry.get(), qualifications_entry.get(),
                  gender_entry.get(), username_entry.get(), password_entry.get()))

            db.commit()
            confirmation_label.config(text="Doctor registered successfully!")

        doctor_frame = ttk.Frame(parent)
        doctor_frame.pack(padx=10, pady=10)

        labels = ["Name", "Dept 1", "Dept 2", "Dept 3", "Address", "Phone 1", "Phone 2", "Qualifications", "Gender", "Username", "Password"]
        entries = [ttk.Entry(doctor_frame) for _ in range(len(labels))]
        confirmation_label = ttk.Label(doctor_frame, text="")

        for i, label in enumerate(labels):
            ttk.Label(doctor_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="E")
            entries[i].grid(row=i, column=1, padx=5, pady=5, sticky="W")

        ttk.Button(doctor_frame, text="Register", command=register_doctor).grid(row=len(labels), columnspan=2, pady=10)
        confirmation_label.grid(row=len(labels) + 1, columnspan=2)

    def book_appointment_tab(parent):
        def book_appointment():
            cursor.execute('''
                INSERT INTO appointments (patientid, date, time, doctor, type, note)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (patient_id_entry.get(), date_entry.get(), time_entry.get(),
                  doctor_entry.get(), type_entry.get(), note_entry.get()))

            db.commit()
            confirmation_label.config(text="Appointment booked successfully!")

        appointment_frame = ttk.Frame(parent)
        appointment_frame.pack(padx=10, pady=10)

        labels = ["Patient ID", "Date (YYYY-MM-DD)", "Time", "Doctor", "Type", "Note"]
        entries = [ttk.Entry(appointment_frame) for _ in range(len(labels))]
        confirmation_label = ttk.Label(appointment_frame, text="")

        for i, label in enumerate(labels):
            ttk.Label(appointment_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="E")
            entries[i].grid(row=i, column=1, padx=5, pady=5, sticky="W")

        ttk.Button(appointment_frame, text="Book Appointment", command=book_appointment).grid(row=len(labels), columnspan=2, pady=10)
        confirmation_label.grid(row=len(labels) + 1, columnspan=2)

    def view_appointment_tab(parent):
        def view_appointments():
            id_type = id_type_var.get()
            search_value = search_entry.get()

            if id_type == "Doctor ID":
                cursor.execute('''
                    SELECT * FROM appointments WHERE doctor = %s
                ''', (search_value,))
            else:
                cursor.execute('''
                    SELECT * FROM appointments WHERE patientid = %s
                ''', (search_value,))

            appointments = cursor.fetchall()
            display_appointments(appointments)

        def display_appointments(appointments):
            for widget in result_frame.winfo_children():
                widget.destroy()

            if not appointments:
                ttk.Label(result_frame, text="No appointments found.").pack()
            else:
                headings = ["Appointment ID", "Patient ID", "Date", "Time", "Doctor", "Type", "Note"]
                for i, heading in enumerate(headings):
                    ttk.Label(result_frame, text=heading).grid(row=0, column=i, padx=5, pady=5, sticky="W")

                for i, appointment in enumerate(appointments, start=1):
                    for j, value in enumerate(appointment):
                        ttk.Label(result_frame, text=value).grid(row=i, column=j, padx=5, pady=5, sticky="W")

        view_frame = ttk.Frame(parent)
        view_frame.pack(padx=10, pady=10)

        id_type_var = tk.StringVar(value="Doctor ID")
        id_type_menu = ttk.OptionMenu(view_frame, id_type_var, "Doctor ID", "Patient ID")
        search_label = ttk.Label(view_frame, text="Search Value:")
        search_entry = ttk.Entry(view_frame, width=30)
        search_button = ttk.Button(view_frame, text="View Appointments", command=view_appointments)

        id_type_menu.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        search_label.grid(row=0, column=1, padx=5, pady=5, sticky="E")
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky="W")
        search_button.grid(row=0, column=3, padx=5, pady=5, sticky="W")

        result_frame = ttk.Frame(view_frame)
        result_frame.grid(row=1, columnspan=4, pady=10)

    def get_patient_details_tab(parent):
        def get_patient_details():
            patient_id = patient_id_entry.get()
            cursor.execute('''
                SELECT * FROM patientdetail WHERE id = %s
            ''', (patient_id,))

            patient_details = cursor.fetchone()
            display_patient_details(patient_details)

        def display_patient_details(patient_details):
            for widget in result_frame.winfo_children():
                widget.destroy()

            if not patient_details:
                ttk.Label(result_frame, text="Patient not found.").pack()
            else:
                headings = ["ID", "Name", "DOB", "Age", "Gender", "Address", "Phone", "Blood Group", "Username", "Password"]
                for i, heading in enumerate(headings):
                    ttk.Label(result_frame, text=heading).grid(row=0, column=i, padx=5, pady=5, sticky="W")

                for j, value in enumerate(patient_details):
                    ttk.Label(result_frame, text=value).grid(row=1, column=j, padx=5, pady=5, sticky="W")

        get_frame = ttk.Frame(parent)
        get_frame.pack(padx=10, pady=10)

        ttk.Label(get_frame, text="Enter Patient ID:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        patient_id_entry = ttk.Entry(get_frame)
        patient_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        ttk.Button(get_frame, text="Get Details", command=get_patient_details).grid(row=0, column=2, padx=5, pady=5, sticky="W")

        result_frame = ttk.Frame(get_frame)
        result_frame.grid(row=1, columnspan=3, pady=10)

    def get_doctor_details_tab(parent):
        def get_doctor_details():
            doctor_id = doctor_id_entry.get()
            cursor.execute('''
                SELECT * FROM doctordetails WHERE id = %s
            ''', (doctor_id,))

            doctor_details = cursor.fetchone()
            display_doctor_details(doctor_details)

        def display_doctor_details(doctor_details):
            for widget in result_frame.winfo_children():
                widget.destroy()

            if not doctor_details:
                ttk.Label(result_frame, text="Doctor not found.").pack()
            else:
                headings = ["ID", "Name", "Dept 1", "Dept 2", "Dept 3", "Address", "Phone 1", "Phone 2", "Qualifications", "Gender", "Username", "Password"]
                for i, heading in enumerate(headings):
                    ttk.Label(result_frame, text=heading).grid(row=0, column=i, padx=5, pady=5, sticky="W")

                for j, value in enumerate(doctor_details):
                    ttk.Label(result_frame, text=value).grid(row=1, column=j, padx=5, pady=5, sticky="W")

        get_frame = ttk.Frame(parent)
        get_frame.pack(padx=10, pady=10)

        ttk.Label(get_frame, text="Enter Doctor ID:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        doctor_id_entry = ttk.Entry(get_frame)
        doctor_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        ttk.Button(get_frame, text="Get Details", command=get_doctor_details).grid(row=0, column=2, padx=5, pady=5, sticky="W")

        result_frame = ttk.Frame(get_frame)
        result_frame.grid(row=1, columnspan=3, pady=10)

    # Create the main window
    root = tk.Tk()
    root.title("Admin Page")
    root.geometry("800x600")

    # Create the notebook
    tab_control = ttk.Notebook(root)

    tabs = [
        ("Register Patient", register_patient_tab),
        ("Doctor Registration", doctor_registration_tab),
        ("Book Appointment", book_appointment_tab),
        ("View Appointment", view_appointment_tab),
        ("Get Patient Details", get_patient_details_tab),
        ("Get Doctor Details", get_doctor_details_tab)
    ]

    for tab_name, tab_func in tabs:
        tab_frame = ttk.Frame(tab_control)
        tab_func(tab_frame)
        tab_control.add(tab_frame, text=tab_name)

    tab_control.pack(expand=1, fill="both")

    root.mainloop()







# Function to display the doctor's page
def doctor_page(doctor_id):
    def go_back():
        doctor_window.destroy()

    # Create a doctor's details window
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Doctor's Page")
    doctor_window.geometry("1660x720")  # Set the window size to fullscreen

    doctor_frame = tk.Frame(doctor_window)
    doctor_frame.pack(expand=True, fill='both')
    doctor_frame.configure(bg="#FFFACD")  # Set background color to light cream

    cursor = db.cursor()
    cursor.execute("SELECT * FROM DoctorDetails WHERE DoctorNo = %s", (doctor_id,))
    doctor_data = cursor.fetchone()
    cursor.close()

    if doctor_data:
        # Display doctor name at the top center with a larger font
        doctor_name_label = tk.Label(doctor_frame, text=f"Doctor: {doctor_data[1]}", font=("Arial", 24), bg="#FFFACD")
        doctor_name_label.pack(pady=20, padx=20, anchor='n')

        # Create a frame for doctor details
        details_frame = tk.Frame(doctor_frame, bg="#FFFACD")
        details_frame.pack(expand=True, fill='both', padx=20, pady=20, anchor='w')

        details_label = tk.Label(details_frame, text="Doctor Details", font=("Arial", 14), bg="#FFFACD")
        details_label.pack(pady=10, anchor='w')

        # Add a separator (border) after the "Doctor Details" section
        separator = ttk.Separator(doctor_frame, orient='horizontal')
        separator.pack(fill='x', padx=20, pady=100)
        separator = ttk.Separator(doctor_frame, orient='vertical')
        separator.pack(fill='x', padx=20, pady=10)

        dept1_label = tk.Label(details_frame, text=f"Department 1: {doctor_data[2]}", font=("Arial", 10), bg="#FFFACD")
        dept1_label.pack(anchor='w')

        dept2_label = tk.Label(details_frame, text=f"Department 2: {doctor_data[3]}", font=("Arial", 10), bg="#FFFACD")
        dept2_label.pack(anchor='w')

        dept3_label = tk.Label(details_frame, text=f"Department 3: {doctor_data[4]}", font=("Arial", 10), bg="#FFFACD")
        dept3_label.pack(anchor='w')

        address_label = tk.Label(details_frame, text=f"Address: {doctor_data[5]}", font=("Arial", 10), bg="#FFFACD")
        address_label.pack(anchor='w')

        phone1_label = tk.Label(details_frame, text=f"Phone Number 1: {doctor_data[6]}", font=("Arial", 10), bg="#FFFACD")
        phone1_label.pack(anchor='w')

        phone2_label = tk.Label(details_frame, text=f"Phone Number 2: {doctor_data[7]}", font=("Arial", 10), bg="#FFFACD")
        phone2_label.pack(anchor='w')

        qualifications_label = tk.Label(details_frame, text=f"Qualifications: {doctor_data[8]}", font=("Arial", 10), bg="#FFFACD")
        qualifications_label.pack(anchor='w')

        gender_label = tk.Label(details_frame, text=f"Gender: {doctor_data[9]}", font=("Arial", 10), bg="#FFFACD")
        gender_label.pack(anchor='w')

        back_button = tk.Button(doctor_frame, text="Back", command=go_back, font=("Arial", 16))
        back_button.pack(pady=10, anchor='w')

windowbg = "#89CFF0"
# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1660x720")  # Set the initial window size
root.configure(bg=windowbg)  # Set background color to baby blue

# Create labels for the main menu
menu_label = tk.Label(root, text="HOSPITECH", font=("Arial", 24), bg=windowbg)
menu_label.pack(pady=100)

# Buttons for choosing between patient, doctor, and admin login
patient_button = tk.Button(root, text="Patient Login", command=patient_login, font=("Arial", 16), bg=windowbg)
patient_button.pack(pady=10)

doctor_button = tk.Button(root, text="Doctor Login", command=doctor_login, font=("Arial", 16), bg=windowbg)
doctor_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Login", command=admin_login, font=("Arial", 16), bg=windowbg)
admin_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
db.close()
