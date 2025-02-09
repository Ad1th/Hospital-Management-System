import tkinter as tk
import mysql.connector
from tkinter import messagebox

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
    login_window.geometry("400x300")  # Set the window size

    login_label = tk.Label(login_window, text="Doctor Login", font=("Arial", 20))
    login_label.pack(pady=20)

    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")  # Show asterisks for password input
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login", command=check_login)
    login_button.pack()

# Function to handle patient login
def patient_login():
    # Implement patient login logic here
    pass

# Function to handle admin login
def admin_login():
    # Implement admin login logic here
    pass

# Function to display the doctor's page
def doctor_page(doctor_id):
    def go_back():
        doctor_window.destroy()

    # Create a doctor's details window
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Doctor's Page")
    doctor_window.geometry("600x400")  # Set the window size

    cursor = db.cursor()
    cursor.execute("SELECT * FROM DoctorDetails WHERE DoctorNo = %s", (doctor_id,))
    doctor_data = cursor.fetchone()
    cursor.close()

    if doctor_data:
        doctor_label = tk.Label(doctor_window, text=f"Doctor Name: {doctor_data[1]}", font=("Arial", 16))
        doctor_label.pack(pady=10)

        dept1_label = tk.Label(doctor_window, text=f"Department 1: {doctor_data[2]}", font=("Arial", 16))
        dept1_label.pack()

        dept2_label = tk.Label(doctor_window, text=f"Department 2: {doctor_data[3]}", font=("Arial", 16))
        dept2_label.pack()

        dept3_label = tk.Label(doctor_window, text=f"Department 3: {doctor_data[4]}", font=("Arial", 16))
        dept3_label.pack()

        address_label = tk.Label(doctor_window, text=f"Address: {doctor_data[5]}", font=("Arial", 16))
        address_label.pack()

        phone1_label = tk.Label(doctor_window, text=f"Phone Number 1: {doctor_data[6]}", font=("Arial", 16))
        phone1_label.pack()

        phone2_label = tk.Label(doctor_window, text=f"Phone Number 2: {doctor_data[7]}", font=("Arial", 16))
        phone2_label.pack()

        qualifications_label = tk.Label(doctor_window, text=f"Qualifications: {doctor_data[8]}", font=("Arial", 16))
        qualifications_label.pack()

        gender_label = tk.Label(doctor_window, text=f"Gender: {doctor_data[9]}", font=("Arial", 16))
        gender_label.pack()

        back_button = tk.Button(doctor_window, text="Back", command=go_back, font=("Arial", 16))
        back_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600")  # Set the initial window size
root.configure(bg="#FFFACD")  # Set background color

# Create labels for the main menu
menu_label = tk.Label(root, text="Main Menu", font=("Arial", 24), bg="#FFFACD")
menu_label.pack(pady=20)

# Buttons for choosing between patient, doctor, and admin login
patient_button = tk.Button(root, text="Patient Login", command=patient_login, font=("Arial", 16))
patient_button.pack(pady=10)

doctor_button = tk.Button(root, text="Doctor Login", command=doctor_login, font=("Arial", 16))
doctor_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Login", command=admin_login, font=("Arial", 16))
admin_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
db.close()
