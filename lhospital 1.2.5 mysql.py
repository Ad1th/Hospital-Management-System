#Grade 12 SSE Project - Hospital management software 
#By- Adith Manikonda, Nitigya Khaneja, Debayan Ghose, 12A

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


db = mysql.connector.connect( host="localhost", user="root", password="adith666", database="lhospital")


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
    login_window.geometry("800x600")  # Setting the window size to fullscreen

    login_frame = tk.Frame(login_window)
    login_frame.pack(expand=True, fill='both')
    login_frame.configure(bg="#FFFACD")  # Setting background color to light cream

    login_label = tk.Label(login_frame, text="Doctor Login", font=("Arial", 20))
    login_label.pack(pady=20)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_frame)
    username_entry.pack()

    password_label = tk.Label(login_frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_frame, show="*")  # To show asterisks for password input for privacy
    password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command=check_login)
    login_button.pack()

def admin_login():
    def check_admin_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "lhospital" and password == "admin":
            
            admin_menu()
            login_window.destroy()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

   
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

def admin_menu():
    admin_window = tk.Toplevel(root)
    admin_window.title("ADMIN MAIN MENU")
    admin_window.geometry("1660x720")
    admin_bg = "#bfe7bf"
    
    admin_frame =tk.Frame(admin_window)
    admin_frame.pack(expand = True, fill = 'both')
    admin_frame.configure(bg=admin_bg)


    menu_label = tk.Label(admin_frame, text="LHOSPITAL ADMIN MENU", font=("Arial", 24), bg=admin_bg)
    menu_label.pack(pady=20)

    reg_pat_button = tk.Button(admin_frame, text="REGISTER NEW PATIENT", command=reg_pat, font=("Arial", 16),bg=admin_bg)
    reg_pat_button.pack(pady=20, padx = 30, anchor='w')

    get_pat_button = tk.Button(admin_frame, text="GET PATIENT DETAILS", command=get_pat, font=("Arial", 16),bg=admin_bg)
    get_pat_button.pack(pady=20, padx = 30, anchor='w')

    reg_doc_button = tk.Button(admin_frame, text="REGISTER NEW  DOCTOR", command=reg_doc, font=("Arial", 16),bg=admin_bg)
    reg_doc_button.pack(pady=20, padx = 30, anchor='w')

    get_docs_button = tk.Button(admin_frame, text="VIEW ALL DOCTORS", command=view_all_docs, font=("Arial", 16),bg=admin_bg)
    get_docs_button.pack(pady=20, padx = 30, anchor='w')
    
    search_doc_button = tk.Button(admin_frame, text="SEARCH DOCTOR", command=search_doc, font=("Arial", 16),bg=admin_bg)
    search_doc_button.pack(pady=20, padx = 30, anchor='w')

    book_apt_button = tk.Button(admin_frame, text="BOOK APPOINTMENT", command=book_apt, font=("Arial", 16),bg=admin_bg)
    book_apt_button.pack(pady=20, padx = 30, anchor='w')

    show_apt_button = tk.Button(admin_frame, text="SHOW APPOINTMENTS", command=show_apt, font=("Arial", 16),bg=admin_bg)
    show_apt_button.pack(pady=20, padx = 30, anchor='w')



def reg_pat():
    def add_patient_details():
        # Retrieve data from the input fields
        patient_id = patient_id_entry.get()
        name = name_entry.get()
        dob = dob_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        address = address_entry.get()
        phone_number = phone_entry.get()
        blood_group = blood_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        cursor = db.cursor()

        # Insert data into the database
        query = "INSERT INTO patientdetails (patientid, name, DOB, Age, Gender, Address, Phonenumber, Bloodgroup, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (patient_id, name, dob, age, gender, address, phone_number, blood_group, username, password)

        cursor.execute(query, data)
        db.commit()


        # Clear the input fields after adding data
        clear_entries()

        # Show a success message or perform any other necessary action
        success_label.config(text="Patient details added successfully!")

    def clear_entries():
        # Clear all input fields
        patient_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        blood_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    # Create the main window
    root = tk.Tk()
    root.title("Add Patient Details")

    # Create frames
    input_frame = tk.Frame(root)
    input_frame.pack(padx=20, pady=20)

    success_label = tk.Label(root, fg="green")
    success_label.pack()

    # Create labels and entry fields for input
    labels = ['Patient ID', 'Name', 'DOB (YYYY-MM-DD)', 'Age', 'Gender', 'Address', 'Phone Number', 'Blood Group', 'Username', 'Password']
    entries = []

    for i in range(len(labels)):
        label = tk.Label(input_frame, text=labels[i])
        label.grid(row=i, column=0, padx=5, pady=5)

        entry = tk.Entry(input_frame)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    # Assigning each entry to a specific variable
    patient_id_entry, name_entry, dob_entry, age_entry, gender_entry, address_entry, phone_entry, blood_entry, username_entry, password_entry = entries

    # Button to add patient details
    add_button = tk.Button(root, text="Add Patient Details", command=add_patient_details)
    add_button.pack(pady=10)

    root.mainloop()

def get_pat():
    def fetch_patient_details():
        patient_id = patient_id_entry.get()


        cursor = db.cursor()

        # Fetch data from the database based on the patient id
        query = "SELECT * FROM patientdetails WHERE patientid = %s"
        cursor.execute(query, (patient_id,))
        patient_data = cursor.fetchone()

        # Display the patient details
        if patient_data:
            # Clear previous details
            for widget in details_frame.winfo_children():
                widget.destroy()

            labels = ['Patient ID', 'Name', 'DOB', 'Age', 'Gender', 'Address', 'Phone Number', 'Blood Group', 'Username', 'Password']
            for i in range(len(labels)):
                label = tk.Label(details_frame, text=f"{labels[i]}: {patient_data[i]}")
                label.pack()

    

    # Create the main window
    root = tk.Tk()
    root.title("Admin Panel")

    # Create frames
    input_frame = tk.Frame(root)
    input_frame.pack(padx=20, pady=20)

    details_frame = tk.Frame(root)
    details_frame.pack(padx=20, pady=10)

    # Create input elements
    patient_id_label = tk.Label(input_frame, text="Enter Patient ID:")
    patient_id_label.grid(row=0, column=0)

    patient_id_entry = tk.Entry(input_frame)
    patient_id_entry.grid(row=0, column=1)

    fetch_button = tk.Button(input_frame, text="Fetch Details", command=fetch_patient_details)
    fetch_button.grid(row=0, column=2, padx=5)

    root.mainloop()

def reg_doc():

    def add_doctor_details():
        # Retrieve data from the input fields
        doctor_no = doctor_no_entry.get()
        name = name_entry.get()
        dept_1 = dept1_entry.get()
        dept_2 = dept2_entry.get()
        dept_3 = dept3_entry.get()
        address = address_entry.get()
        phone_number1 = phone1_entry.get()
        phone_number2 = phone2_entry.get()
        qualifications = qualifications_entry.get()
        gender = gender_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        cursor = db.cursor()

        # Insert data into the database
        query = "INSERT INTO doctordetails (DoctorNo, Name, `Dept 1`, `Dept 2`, `Dept 3`, Address, `Phone number1`, `Phone number 2`, Qualifications, Gender, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (doctor_no, name, dept_1, dept_2, dept_3, address, phone_number1, phone_number2, qualifications, gender, username, password)

        cursor.execute(query, data)
        db.commit()

        
        
        clear_entries()
        success_label.config(text="Doctor details added successfully!")

    def clear_entries():
        # Clear all input fields
        doctor_no_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        dept1_entry.delete(0, tk.END)
        dept2_entry.delete(0, tk.END)
        dept3_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone1_entry.delete(0, tk.END)
        phone2_entry.delete(0, tk.END)
        qualifications_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    # main window
    root = tk.Tk()
    root.title("Add Doctor Details")

    # Create frames
    input_frame = tk.Frame(root)
    input_frame.pack(padx=20, pady=20)

    success_label = tk.Label(root, fg="green")
    success_label.pack()

    # Create labels and entry fields for input
    labels = ['Doctor No', 'Name', 'Dept 1', 'Dept 2', 'Dept 3', 'Address', 'Phone Number 1', 'Phone Number 2', 'Qualifications', 'Gender', 'Username', 'Password']
    entries = []

    for i in range(len(labels)):
        label = tk.Label(input_frame, text=labels[i])
        label.grid(row=i, column=0, padx=5, pady=5)

        entry = tk.Entry(input_frame)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    # Assigning each entry to a specific variable
    doctor_no_entry, name_entry, dept1_entry, dept2_entry, dept3_entry, address_entry, phone1_entry, phone2_entry, qualifications_entry, gender_entry, username_entry, password_entry = entries

    # Button to add doctor details
    add_button = tk.Button(root, text="Add Doctor Details", command=add_doctor_details)
    add_button.pack(pady=10)

    root.mainloop()

def view_all_docs():
    def view_doctor_details():
        cursor = db.cursor()

        # Fetch all doctor details from the database
        query = "SELECT * FROM doctordetails"
        cursor.execute(query)
        doctor_data = cursor.fetchall()

        # Display doctor details in a separate window
        doctor_window = tk.Tk()
        doctor_window.title("Doctor Details")

        details_frame = tk.Frame(doctor_window)
        details_frame.pack(padx=20, pady=20)

        labels = ['Doctor No', 'Name', 'Dept 1', 'Dept 2', 'Dept 3', 'Address', 'Phone Number 1', 'Phone Number 2', 'Qualifications', 'Gender', 'Username', 'Password']

        for i, label in enumerate(labels):
            label = tk.Label(details_frame, text=label)
            label.grid(row=0, column=i, padx=5, pady=5)

        for row_num, doctor in enumerate(doctor_data, start=1):
            for col_num, detail in enumerate(doctor):
                label = tk.Label(details_frame, text=detail)
                label.grid(row=row_num, column=col_num, padx=5, pady=5)

        
        doctor_window.mainloop()

    # Create the main window
    root = tk.Tk()
    root.title("View Doctor Details")

    # Button to view doctor details
    view_button = tk.Button(root, text="View Doctor Details", command=view_doctor_details)
    view_button.pack(padx=20, pady=10)

    root.mainloop()

def search_doc():
    def search_doctor():
        search_term = '%' + search_entry.get() + '%'  # Search term with wildcards for partial matching

        cursor = db.cursor()

        # Search doctor details based on doctor number or partial match for other fields
        query = "SELECT * FROM doctordetails WHERE DoctorNo = %s OR Name LIKE %s OR `Dept 1` LIKE %s OR `Dept 2` LIKE %s OR `Dept 3` LIKE %s"
        cursor.execute(query, (search_entry.get(), search_term, search_term, search_term, search_term))
        doctor_data = cursor.fetchall()

        # Display doctor details in a separate window
        doctor_window = tk.Tk()
        doctor_window.title("Doctor Details")

        details_frame = tk.Frame(doctor_window)
        details_frame.pack(padx=20, pady=20)

        labels = ['Doctor No', 'Name', 'Dept 1', 'Dept 2', 'Dept 3', 'Address', 'Phone Number 1', 'Phone Number 2', 'Qualifications', 'Gender', 'Username', 'Password']

        for i, label in enumerate(labels):
            label = tk.Label(details_frame, text=label)
            label.grid(row=0, column=i, padx=5, pady=5)

        for row_num, doctor in enumerate(doctor_data, start=1):
            for col_num, detail in enumerate(doctor):
                label = tk.Label(details_frame, text=detail)
                label.grid(row=row_num, column=col_num, padx=5, pady=5)



    # Create the main window
    root = tk.Tk()
    root.title("Search Doctor Details")

    # Search entry and button
    search_label = tk.Label(root, text="Search by Doctor No, Name, or Department:")
    search_label.pack(padx=20, pady=5)

    search_entry = tk.Entry(root)
    search_entry.pack(padx=20, pady=5)

    search_button = tk.Button(root, text="Search", command=search_doctor)
    search_button.pack(padx=20, pady=5)

    root.mainloop()

def book_apt():
    def book_appointment():
        doctor_id = doctor_entry.get()
        patient_id = patient_entry.get()
        appointment_date = date_entry.get()
        appointment_time = time_entry.get()
        brief_note = note_entry.get()


        cursor = db.cursor()

        cursor.execute("SELECT COUNT(*) FROM doctordetails WHERE DoctorNo = %s", (doctor_id,))
        doctor_exists = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM patientdetails WHERE patientid = %s", (patient_id,))
        patient_exists = cursor.fetchone()[0]

        if doctor_exists and patient_exists:
            booking_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            insert_query = "INSERT INTO appointments (DoctorNo, PatientID, AppointmentDate, AppointmentTime, BriefNote, BookingTime) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (doctor_id, patient_id, appointment_date, appointment_time, brief_note, booking_time))
            db.commit()
            success_label.config(text="Appointment booked successfully!")
        else:
            success_label.config(text="Doctor or patient does not exist. Appointment booking failed.")

        

    # Create the main window
    root = tk.Tk()
    root.title("Book Appointment")
    root.geometry("400x300")

    # Labels and Entry fields
    doctor_label = tk.Label(root, text="Doctor ID:")
    doctor_label.pack()

    doctor_entry = tk.Entry(root)
    doctor_entry.pack()

    patient_label = tk.Label(root, text="Patient ID:")
    patient_label.pack()

    patient_entry = tk.Entry(root)
    patient_entry.pack()

    date_label = tk.Label(root, text="Appointment Date:")
    date_label.pack()

    date_entry = tk.Entry(root)
    date_entry.pack()

    time_label = tk.Label(root, text="Appointment Time:")
    time_label.pack()

    time_entry = tk.Entry(root)
    time_entry.pack()

    note_label = tk.Label(root, text="Brief Note:")
    note_label.pack()

    note_entry = tk.Entry(root)
    note_entry.pack()

    success_label = tk.Label(root, fg="green")
    success_label.pack()

    # Book Appointment button
    book_button = tk.Button(root, text="Book Appointment", command=book_appointment)
    book_button.pack()

    root.mainloop()

def show_apt():
    def view_appointments():
        
        cursor = db.cursor()

        query = "SELECT * FROM appointments"
        cursor.execute(query)
        appointments_data = cursor.fetchall()

        # Create a new window for displaying appointments
        appointments_window = tk.Tk()
        appointments_window.title("Appointments")
        appointments_window.geometry("900x400")

        appointments_frame = tk.Frame(appointments_window)
        appointments_frame.pack(expand=True, fill='both')

        labels = ['AppointmentID', 'DoctorNo', 'PatientID', 'AppointmentDate', 'AppointmentTime', 'BriefNote', 'BookingTime']

        for i, label in enumerate(labels):
            label = tk.Label(appointments_frame, text=label)
            label.grid(row=0, column=i, padx=5, pady=5)

        for row_num, appointment in enumerate(appointments_data, start=1):
            for col_num, detail in enumerate(appointment):
                label = tk.Label(appointments_frame, text=detail)
                label.grid(row=row_num, column=col_num, padx=5, pady=5)


    # Create the main window
    root = tk.Tk()
    root.title("View Appointments")
    root.geometry("400x200")

    # Button to view appointments
    view_button = tk.Button(root, text="View Appointments", command=view_appointments)
    view_button.pack(padx=20, pady=10)

    root.mainloop()

def doctor_page(doctor_id):
    def go_back():
        doctor_window.destroy()

    
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Doctor's Page")
    doctor_window.geometry("1660x720") 

    doctor_frame = tk.Frame(doctor_window)
    doctor_frame.pack(expand=True, fill='both')
    doctor_frame.configure(bg="#f1c87b") 

    cursor = db.cursor()
    cursor.execute("SELECT * FROM DoctorDetails WHERE DoctorNo = %s", (doctor_id,))
    doctor_data = cursor.fetchone()

    cursor.execute("SELECT AppointmentID, PatientID, name, AppointmentDate, AppointmentTime, Age, gender, Bloodgroup, BriefNote, BookingTime FROM  appointments natural join patientdetails WHERE DoctorNo = %s", (doctor_id,))
    appointments = cursor.fetchall()
    cursor.close()

    if doctor_data:

        doctor_name_label = tk.Label(doctor_frame, text=f"Doctor: {doctor_data[1]}", font=("Arial", 24), bg="#FFFACD")
        doctor_name_label.pack(pady=20, padx=20, anchor='n')

        details_frame = tk.Frame(doctor_frame, bg="#FFFACD")
        details_frame.pack(  padx=20, pady=20, anchor='w')

        details_label = tk.Label(details_frame, text="Doctor Details", font=("Arial", 14), bg="#FFFACD")
        details_label.pack(pady=10, anchor='w')

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

        appt_frame = tk.Frame(doctor_frame, bg="#FFFACD")
        appt_frame.pack(padx=20, pady=20, anchor='w')

        appt_label = tk.Label(appt_frame, text="Appointments", font=("Arial", 20))
        appt_label.grid(row = 0, column = 0, padx=5, pady=5)

        labels = tk.Label(appt_frame, text="Appointment ID     Patient ID\t\tPatient Name \tAppointment Date\t    Appointment Time\t   Age\t     Gender \t Bloodgroup\t\tBrief Note \t\tBooking Time", font=("Arial", 10))
        labels.grid(row = 1, column = 0, padx=5, pady=5)

        """
        labels = ["Appointment ID", "Patient ID", "Patient Name", "Appointment Date", "Appointment Time", "Age", "Gender", "Bloodgroup", "Brief Note", "Booking Time"]
        for i, label_text in enumerate(labels):
            label = tk.Label(appt_frame, text=label_text, font=("Arial", 11))
            label.grid(row=1, column=i, padx=2, pady=1) 
        """

        appointments_list = tk.Listbox(appt_frame, font=("Arial", 9, ), selectbackground="#A6A6A6", selectmode="extended", height=7, width = 175)
        appointments_list.grid(row=2, column=0, columnspan=10, padx=30, pady=5)

        
        for appointmentid in appointments:
            details_string = "                "+"                          ".join(str(detail) for detail in appointmentid)
            appointments_list.insert("end", details_string)




        back_button = tk.Button(doctor_frame, text="Back", command=go_back, font=("Arial", 16))
        back_button.pack(pady=10, anchor='w')

windowbg = "#89CFF0"
# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1660x720")  
root.configure(bg=windowbg)  


menu_label = tk.Label(root, text="HOSPITECH", font=("Arial", 24), bg=windowbg)
menu_label.pack(pady=100)


doctor_button = tk.Button(root, text="Doctor Login", command=doctor_login, font=("Arial", 16), bg=windowbg)
doctor_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Login", command=admin_login, font=("Arial", 16), bg=windowbg)
admin_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when done
db.close()
