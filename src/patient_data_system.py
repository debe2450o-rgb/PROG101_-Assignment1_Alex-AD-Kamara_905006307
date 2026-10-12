"""DHPDMS classroom reference implementation.

This program uses in-memory records only and contains synthetic-data logic for
PROG101. It is not suitable for real clinical use.
"""

from dataclasses import dataclass

MAX_PATIENTS = 100


@dataclass
class Patient:
    patient_id: str
    full_name: str
    age: int
    gender: str
    contact_number: str
    diagnosis_history: str


def validate_patient_input(patient_id: str, name: str, age: int) -> bool:
    return bool(patient_id.strip()) and bool(name.strip()) and 0 <= age <= 130


def find_patient_index(records: list[Patient], target_id: str) -> int:
    for index, patient in enumerate(records):
        if patient.patient_id == target_id:
            return index
    return -1


def register_patient(records: list[Patient], patient: Patient) -> str:
    if len(records) >= MAX_PATIENTS:
        return "ERROR: Patient storage is full."
    if not validate_patient_input(patient.patient_id, patient.full_name, patient.age):
        return "ERROR: Invalid patient information. Record not saved."
    if find_patient_index(records, patient.patient_id) != -1:
        return "ERROR: Patient ID already exists."
    records.append(patient)
    return f"Patient record successfully saved for ID: {patient.patient_id}"


def update_record(records: list[Patient], target_id: str, new_entry: str) -> str:
    position = find_patient_index(records, target_id)
    if position == -1:
        return "ERROR: Patient ID does not exist."
    records[position].diagnosis_history += f" | {new_entry}"
    return "Medical record updated successfully."


def main() -> None:
    records: list[Patient] = []
    running = True
    while running:
        print("\nSIERRA LEONE DIGITAL HEALTH SYSTEM")
        print("1. Register New Patient")
        print("2. Search Patient Record")
        print("3. Add Diagnosis / Treatment")
        print("4. Exit System")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            try:
                patient = Patient(
                    input("Patient ID: ").strip(),
                    input("Full name: ").strip(),
                    int(input("Age: ")),
                    input("Gender: ").strip(),
                    input("Contact number: ").strip(),
                    input("Diagnosis/history: ").strip(),
                )
                print(register_patient(records, patient))
            except ValueError:
                print("ERROR: Age must be a whole number.")
        elif choice == "2":
            position = find_patient_index(records, input("Patient ID: ").strip())
            print("Patient record not found." if position == -1 else records[position])
        elif choice == "3":
            print(update_record(records, input("Patient ID: ").strip(), input("New entry: ").strip()))
        elif choice == "4":
            running = False
            print("System closed successfully.")
        else:
            print("Invalid selection. Please choose 1 to 4.")


if __name__ == "__main__":
    main()
