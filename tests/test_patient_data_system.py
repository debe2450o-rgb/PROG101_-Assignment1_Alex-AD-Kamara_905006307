import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from patient_data_system import MAX_PATIENTS, Patient, find_patient_index, register_patient, update_record, validate_patient_input


def patient(patient_id="P102"):
    return Patient(patient_id, "Alex Kamara", 25, "Male", "076000000", "Initial consultation")


def test_validation_boundaries():
    assert validate_patient_input("P1", "Name", 0)
    assert validate_patient_input("P1", "Name", 130)
    assert not validate_patient_input("", "Name", 25)
    assert not validate_patient_input("P1", "", 25)
    assert not validate_patient_input("P1", "Name", -1)
    assert not validate_patient_input("P1", "Name", 131)


def test_register_find_and_update():
    records = []
    assert register_patient(records, patient()) == "Patient record successfully saved for ID: P102"
    assert find_patient_index(records, "P102") == 0
    assert update_record(records, "P102", "Follow-up completed") == "Medical record updated successfully."
    assert records[0].diagnosis_history.endswith(" | Follow-up completed")


def test_duplicate_and_missing_id_errors():
    records = [patient()]
    assert register_patient(records, patient()) == "ERROR: Patient ID already exists."
    assert update_record(records, "P999", "No record") == "ERROR: Patient ID does not exist."
    assert find_patient_index(records, "P999") == -1


def test_storage_limit():
    records = [patient(f"P{i}") for i in range(MAX_PATIENTS)]
    assert register_patient(records, patient("EXTRA")) == "ERROR: Patient storage is full."
