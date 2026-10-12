# PROG101 — Digital Healthcare Patient Data Management System

Project: Digital Healthcare Patient Data Management System (DHPDMS)  
Student: Alex Alimamy Debe Kamara
Student ID: 905006307  
Course: PROG101 — Principles of Programming Logic and Design  
Institution: Limkokwing University of Creative Technology, Sierra Leone  
Examiner: Elijah Fullah  

## Overview

DHPDMS is a classroom logic prototype for a lightweight, offline-first digital patient-record workflow in Sierra Leone. It supports patient registration, record search, diagnosis/treatment updates, input validation, and a repeating menu. It is designed to demonstrate sequence, selection, repetition, functions, modularity, and array searching.

This project contains **no real patient data**. It is not a clinical system. Any real deployment would require authorization, privacy safeguards, role-based access, encryption, audit logs, consent and data-retention rules, clinical validation, backups, and interoperability with approved health systems.

## SDG alignment

- SDG 3 — Good Health and Well-being: supports faster retrieval and continuity of health information.
- SDG 9 — Industry, Innovation and Infrastructure: demonstrates adaptable, open digital infrastructure for public services.

## Modules

- `Main` — controls the menu loop.
- `RegisterPatient` — validates and stores new demographic and medical information.
- `SearchPatient` — searches the patient-ID array and displays a matching record.
- `UpdateRecord` — locates a patient and appends a diagnosis/treatment note.
- `FindPatientIndex` — reusable sequential-search function.
- `ValidatePatientInput` — prevents blank IDs, impossible ages, and empty names.

## Optional runnable reference

`src/patient_data_system.py` is a small Python implementation of the submitted
logic. It stores synthetic records in memory and is included for demonstration
and testing only; it is not a clinical application.

Run it with:

```bash
python3 src/patient_data_system.py
```

Run the automated checks with:

```bash
python3 -m pytest -q
```

## Structure

```text
├── README.md
├── Documentation/Report.pdf
├── Documentation/Report.docx
├── Documentation/Report.md
├── Flowcharts/dhpdm_system.mmd
├── Flowcharts/dhpdm_system.fprg
├── Flowcharts/dhpdm_system.png
├── Pseudocode/dhpdm_pseudocode.txt
├── src/patient_data_system.py
├── tests/test_patient_data_system.py
├── References/sources.md
├── Screenshots/README.md
└── DHPDMS_Project.zip
```
