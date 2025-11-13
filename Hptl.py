# Hospital Management System
# Author: Aman Kumar
# Language: Python 3

class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Disease: {self.disease}"


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"


class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # Add patient
    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        self.patients.append(Patient(pid, name, age, gender, disease))
        print(" Patient added successfully!")

    # Add doctor
    def add_doctor(self):
        did = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        specialization = input("Enter Specialization: ")
        self.doctors.append(Doctor(did, name, specialization))
        print(" Doctor added successfully!")

    # Display all patients
    def show_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            print("\n--- Patient List ---")
            for p in self.patients:
                print(p)

    # Display all doctors
    def show_doctors(self):
        if not self.doctors:
            print(" No doctors found.")
        else:
            print("\n--- Doctor List ---")
            for d in self.doctors:
                print(d)

    # Schedule appointment
    def schedule_appointment(self):
        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")

        patient = next((p for p in self.patients if p.patient_id == pid), None)
        doctor = next((d for d in self.doctors if d.doctor_id == did), None)

        if patient and doctor:
            appointment = f"Patient {patient.name} with Dr. {doctor.name} ({doctor.specialization})"
            self.appointments.append(appointment)
            print(f"Appointment scheduled: {appointment}")
        else:
            print("Invalid patient or doctor ID!")

    # Display appointments
    def show_appointments(self):
        if not self.appointments:
            print(" No appointments found.")
        else:
            print("\n--- Appointments ---")
            for a in self.appointments:
                print(a)

    # Search patient by ID
    def search_patient(self):
        pid = input("Enter Patient ID to search: ")
        for p in self.patients:
            if p.patient_id == pid:
                print(" Patient Found:", p)
                return
        print(" Patient not found!")

    # Delete patient by ID
    def delete_patient(self):
        pid = input("Enter Patient ID to delete: ")
        for p in self.patients:
            if p.patient_id == pid:
                self.patients.remove(p)
                print(" Patient deleted successfully!")
                return
        print("Patient not found!")


def main():
    hms = HospitalManagementSystem()

    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")

