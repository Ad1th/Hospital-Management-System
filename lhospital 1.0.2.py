import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

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

# Placeholder for admin page
def admin_page():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Page")
    admin_window.geometry("800x600")
    admin_frame = tk.Frame(admin_window)
    admin_frame.pack(expand=True, fill='both')
    admin_frame.configure(bg="#FFFACD")
    admin_label = tk.Label(admin_frame, text="Admin Page", font=("Arial", 20))
    admin_label.pack(pady=20)

    # Implement your admin-specific content here...

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

admin_button = tk.Button(root, text="Admin Login", command=admin_page, font=("Arial", 16), bg=windowbg)
admin_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
db.close()
