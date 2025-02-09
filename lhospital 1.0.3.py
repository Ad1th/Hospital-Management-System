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

# Placeholder for admin page
class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

class Appointment:
    def __init__(self, date, time):
        self.date = date
        self.time = time

patients = []
appointments = []

def admin_page():
    def go_back():
        admin_window.destroy()

    # Create an admin window
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Page")
    admin_window.geometry("800x600")

    admin_frame = tk.Frame(admin_window)
    admin_frame.pack(expand=True, fill='both')
    admin_frame.configure(bg="#FFFACD")

    admin_label = tk.Label(admin_frame, text="Admin Page", font=("Arial", 20))
    admin_label.pack(pady=20)

    # Add admin page content and functionality here

    back_button = tk.Button(admin_frame, text="Back", command=go_back)
    back_button.pack()

    #windowbg = "#89CFF0"

    # Implement your admin-specific content here...

    def register_patient():
        name = patient_name_entry.get()
        if name:
            patient_id = len(patients) + 1
            patient = Patient(name, patient_id)
            patients.append(patient)
            messagebox.showinfo("Patient Registered", f"Patient {name} registered with ID {patient_id}")
        else:
            messagebox.showerror("Error", "Please enter a valid name.")

    def book_appointment():
        try:
            patient_id = int(patient_id_entry.get())
            if 1 <= patient_id <= len(patients):
                date = appointment_date_combobox.get()
                time = appointment_time_entry.get()
                appointment = Appointment(date, time)
                patients[patient_id - 1].add_appointment(appointment)
                appointments.append(appointment)
                messagebox.showinfo("Appointment Booked", f"Appointment booked for patient {patients[patient_id - 1].name}")
            else:
                messagebox.showerror("Error", "Invalid patient ID")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid patient ID.")

    def view_all_appointments():
        appointment_text.delete(1.0, tk.END)
        for idx, appointment in enumerate(appointments, 1):
            appointment_text.insert(tk.END, f"Appointment {idx}: Date: {appointment.date}, Time: {appointment.time}\n")

    def view_all_patients():
        patient_text.delete(1.0, tk.END)
        for patient in patients:
            patient_text.insert(tk.END, f"Patient ID: {patient.patient_id}, Name: {patient.name}\n")

    # Create tabs
    notebook = ttk.Notebook(admin_frame)
    notebook.pack(expand=True, fill='both')

    # Create patient registration tab
    patient_tab = ttk.Frame(notebook)
    notebook.add(patient_tab, text="Register Patient")

    patient_name_label = tk.Label(patient_tab, text="Patient Name:")
    patient_name_label.pack(pady=10)
    patient_name_entry = tk.Entry(patient_tab)
    patient_name_entry.pack()

    register_button = tk.Button(patient_tab, text="Register", command=register_patient)
    register_button.pack(pady=10)

    # Create appointment booking tab
    appointment_tab = ttk.Frame(notebook)
    notebook.add(appointment_tab, text="Book Appointment")

    # ... Rest of your GUI setup, including the date selection

    # Create appointment and patient lists tab
    lists_tab = ttk.Frame(notebook)
    notebook.add(lists_tab, text="View Appointments/Patients")

    appointment_text = tk.Text(lists_tab, height=10, width=60)
    appointment_text.pack(pady=10, padx=10)
    view_appointments_button = tk.Button(lists_tab, text="View All Appointments", command=view_all_appointments)
    view_appointments_button.pack(pady=10)

    patient_text = tk.Text(lists_tab, height=10, width=40)
    patient_text.pack(pady=10, padx=10)
    view_patients_button = tk.Button(lists_tab, text="View All Patients", command=view_all_patients)
    view_patients_button.pack(pady=10)

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
