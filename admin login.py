import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

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

# Function to register a patient
def register_patient():
    name = patient_name_entry.get()
    if name:
        patient_id = len(patients) + 1
        patient = Patient(name, patient_id)
        patients.append(patient)
        messagebox.showinfo("Patient Registered", f"Patient {name} registered with ID {patient_id}")
    else:
        messagebox.showerror("Error", "Please enter a valid name.")

# Function to book an appointment
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

# Function to view all appointments
def view_all_appointments():
    appointment_text.delete(1.0, tk.END)
    for idx, appointment in enumerate(appointments, 1):
        appointment_text.insert(tk.END, f"Appointment {idx}: Date: {appointment.date}, Time: {appointment.time}\n")

# Function to view all patients
def view_all_patients():
    patient_text.delete(1.0, tk.END)
    for patient in patients:
        patient_text.insert(tk.END, f"Patient ID: {patient.patient_id}, Name: {patient.name}\n")

# Create the main window
root = tk.Tk()
root.title("Patient Management System")
root.geometry("800x600")

# Create tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create patient registration tab
patient_tab = ttk.Frame(notebook)
notebook.add(patient_tab, text="Register Patient")

# Create patient registration form
patient_name_label = tk.Label(patient_tab, text="Patient Name:")
patient_name_label.pack(pady=10)
patient_name_entry = tk.Entry(patient_tab)
patient_name_entry.pack()

register_button = tk.Button(patient_tab, text="Register", command=register_patient)
register_button.pack(pady=10)

# Create appointment booking tab
appointment_tab = ttk.Frame(notebook)
notebook.add(appointment_tab, text="Book Appointment")

# Create appointment booking form
patient_id_label = tk.Label(appointment_tab, text="Patient ID:")
patient_id_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
patient_id_entry = tk.Entry(appointment_tab)
patient_id_entry.grid(row=0, column=1, pady=10, padx=10)

date_frame = tk.Frame(appointment_tab)
date_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Labels for date selection
day_label = tk.Label(date_frame, text="Day:")
day_label.grid(row=0, column=0, padx=5)
month_label = tk.Label(date_frame, text="Month:")
month_label.grid(row=0, column=1, padx=5)
year_label = tk.Label(date_frame, text="Year:")
year_label.grid(row=0, column=2, padx=5)

# Create dropdowns for days, months, and years
day_combobox = ttk.Combobox(date_frame, values=list(range(1, 32)), width=2)
day_combobox.set(datetime.now().strftime("%d"))
day_combobox.grid(row=1, column=0, padx=5)
month_combobox = ttk.Combobox(date_frame, values=list(range(1, 13)), width=2)
month_combobox.set(datetime.now().strftime("%m"))
month_combobox.grid(row=1, column=1, padx=5)
year_combobox = ttk.Combobox(date_frame, values=list(range(2000, 2031)), width=4)
year_combobox.set(datetime.now().strftime("%Y"))
year_combobox.grid(row=1, column=2, padx=5)

# Create a Combobox to display the selected date
appointment_date_combobox = ttk.Combobox(appointment_tab, width=12, state="readonly")
appointment_date_combobox.set(datetime.now().strftime("%d %m %Y"))
appointment_date_combobox.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

def get_selected_date():
    selected_date = f"{day_combobox.get()} {month_combobox.get()} {year_combobox.get()}"
    appointment_date_combobox.set(selected_date)

update_date_button = tk.Button(appointment_tab, text="Update Date", command=get_selected_date)
update_date_button.grid(row=3, column=0, columnspan=2, pady=10)

appointment_time_label = tk.Label(appointment_tab, text="Appointment Time:")
appointment_time_label.grid(row=4, column=0, pady=10, padx=10)
appointment_time_entry = tk.Entry(appointment_tab)
appointment_time_entry.grid(row=4, column=1, pady=10, padx=10)

book_appointment_button = tk.Button(appointment_tab, text="Book Appointment", command=book_appointment)
book_appointment_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create appointment and patient lists tab
lists_tab = ttk.Frame(notebook)
notebook.add(lists_tab, text="View Appointments/Patients")

# Create list boxes to display appointments and patients
appointment_text = tk.Text(lists_tab, height=10, width=60)
appointment_text.pack(pady=10, padx=10)
view_appointments_button = tk.Button(lists_tab, text="View All Appointments", command=view_all_appointments)
view_appointments_button.pack(pady=10)

patient_text = tk.Text(lists_tab, height=10, width=40)
patient_text.pack(pady=10, padx=10)
view_patients_button = tk.Button(lists_tab, text="View All Patients", command=view_all_patients)
view_patients_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
