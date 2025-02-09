import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql123",
    database="lhospital"
)

# Function to handle doctor login
def doctor_login():
    def check_login():
        username = "doc05"
        password = "pass5"

        cursor = db.cursor()
        cursor.execute("SELECT * FROM DoctorDetails WHERE Username = %s AND Password = %s", (username, password))
        doctor_data = cursor.fetchone()
        cursor.close()

        if doctor_data:
            # Redirect to the doctor's page with their ID
            doctor_page(doctor_data[0])
    check_login()

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
        doctor_name_label.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

        # Create a frame for doctor details
        details_frame = tk.Frame(doctor_frame, bg="#FFFACD")
        details_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='w')

        details_label = tk.Label(details_frame, text="Doctor Details", font=("Arial", 14), bg="#FFFACD")
        details_label.grid(row=0, column=0, pady=10, sticky='w')

        dept1_label = tk.Label(details_frame, text=f"Department 1: {doctor_data[2]}", font=("Arial", 10), bg="#FFFACD")
        dept1_label.grid(row=1, column=0, sticky='w')

        dept2_label = tk.Label(details_frame, text=f"Department 2: {doctor_data[3]}", font=("Arial", 10), bg="#FFFACD")
        dept2_label.grid(row=2, column=0, sticky='w')

        dept3_label = tk.Label(details_frame, text=f"Department 3: {doctor_data[4]}", font=("Arial", 10), bg="#FFFACD")
        dept3_label.grid(row=3, column=0, sticky='w')

        address_label = tk.Label(details_frame, text=f"Address: {doctor_data[5]}", font=("Arial", 10), bg="#FFFACD")
        address_label.grid(row=4, column=0, sticky='w')

        phone1_label = tk.Label(details_frame, text=f"Phone Number 1: {doctor_data[6]}", font=("Arial", 10), bg="#FFFACD")
        phone1_label.grid(row=5, column=0, sticky='w')

        phone2_label = tk.Label(details_frame, text=f"Phone Number 2: {doctor_data[7]}", font=("Arial", 10), bg="#FFFACD")
        phone2_label.grid(row=6, column=0, sticky='w')

        qualifications_label = tk.Label(details_frame, text=f"Qualifications: {doctor_data[8]}", font=("Arial", 10), bg="#FFFACD")
        qualifications_label.grid(row=7, column=0, sticky='w')

        gender_label = tk.Label(details_frame, text=f"Gender: {doctor_data[9]}", font=("Arial", 10), bg="#FFFACD")
        gender_label.grid(row=8, column=0, sticky='w')

        pat = tk.Label(details_frame, text=f"Patients: {doctor_data[9]}", font=("Arial", 10), bg="#FFFACD")
        pat.grid(row=1, column=1, sticky='w')


        back_button = tk.Button(doctor_frame, text="Back", command=go_back, font=("Arial", 16))
        back_button.grid(row=2, column=0, pady=50, sticky='w')


windowbg = "#89CFF0"
# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1660x720")  # Set the initial window size
root.configure(bg=windowbg)  # Set background color to baby blue

# Create a button for doctor login
doctor_login_button = tk.Button(root, text="Doctor Login", command=doctor_login)
doctor_login_button.pack()

root.mainloop()
