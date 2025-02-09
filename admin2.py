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

def register_patient():
    name = input("Enter the patient's name: ")
    patient_id = len(patients) + 1
    patient = Patient(name, patient_id)
    patients.append(patient)
    print(f"Patient {name} registered with ID {patient_id}")

def book_appointment():
    patient_id = int(input("Enter patient ID: "))
    if 1 <= patient_id <= len(patients):
        date = input("Enter appointment date (MM/DD/YYYY): ")
        time = input("Enter appointment time: ")
        appointment = Appointment(date, time)
        patients[patient_id - 1].add_appointment(appointment)
        appointments.append(appointment)
        print(f"Appointment booked for patient {patients[patient_id - 1].name}")
    else:
        print("Invalid patient ID")

def view_all_appointments():
    for idx, appointment in enumerate(appointments, 1):
        print(f"Appointment {idx}: Date: {appointment.date}, Time: {appointment.time}")

def view_all_patients():
    for patient in patients:
        print(f"Patient ID: {patient.patient_id}, Name: {patient.name}")

def view_bill():
    print("hello")
while True:
    print("\nOptions:")
    print("1. Register Patient")
    print("2. Book Appointment")
    print("3. View All Appointments")
    print("4. View All Patients")
    print("5. View Bill for Each Patient")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        register_patient()
    elif choice == '2':
        book_appointment()
    elif choice == '3':
        view_all_appointments()
    elif choice == '4':
        view_all_patients()
    elif choice == '5':
        view_bill()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")
