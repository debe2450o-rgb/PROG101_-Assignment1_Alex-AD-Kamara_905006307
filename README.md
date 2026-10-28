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

## Pseudocode
1. START 

2. Set `MAX_PATIENTS = 100` and create six parallel arrays: `patientID`, `fullName`, `age`, `gender`, `contactNumber`, and `diagnosisHistory`.
3. Set `recordCount = 0` and `isSystemRunning = TRUE`.
4. While `isSystemRunning == TRUE`:
   1. Display the menu: Register, Search, Update, or Exit.
   2. Read `menuChoice`.
   3. If `menuChoice == 1`, call `RegisterPatient`.
   4. Else if `menuChoice == 2`, call `SearchPatient`.
   5. Else if `menuChoice == 3`, call `UpdateRecord`.
   6. Else if `menuChoice == 4`, set `isSystemRunning = FALSE` and print the closure message.
   7. Otherwise, print an invalid-selection message.
5. **ValidatePatientInput** returns `TRUE` only when the patient ID and name are not blank and the age is between 0 and 130 inclusive.
6. **FindPatientIndex** loops from index `0` to `recordCount - 1`; it returns the matching index or `-1` when no patient is found.
7. **RegisterPatient**:
   1. If `recordCount >= MAX_PATIENTS`, print a storage-full error and stop.
   2. Read the patient ID, name, age, gender, contact number, and diagnosis.
   3. If validation fails, print an error and stop.
   4. If the patient ID already exists, print a duplicate-ID error and stop.
   5. Store the values at index `recordCount`, increment `recordCount`, and print a success message.
   8. **SearchPatient** reads a target patient ID, finds its index, and either prints the complete record or prints `Patient record not found.`.
   9. **UpdateRecord** reads a target   patient ID, finds its index, and either  appends a diagnosis/treatment note or prints `Patient ID does not exist.`.
  10. When the loop ends, **end the program**.
11. END



## Structure of the Flowchart 

<img width="943" height="1024" alt="image_84485a4b-2e61-4c58-9bcb-0b600e5ef2aa" src="https://github.com/user-attachments/assets/a4ff7c6f-7f15-46eb-901e-52ab8caeac42" />

